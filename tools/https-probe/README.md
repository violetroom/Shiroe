# Temporary home HTTPS endpoint

This Compose fixture serves `/health` with the fixed text `shiroe-https-connectivity-ok`. Other paths return 404. It mounts the Nginx configuration and test certificate directory only; no repository, research files, database, or Docker socket is exposed to the container.

Purpose: test verified HTTPS access to the home server from the actual LC client environment before deploying Shiroe. This is a disposable network test, not a selected production reverse proxy, a Shiroe API, or an OAuth implementation. The user reports home port 443 is unused. Router/firewall state has not been inspected.

## 1. Copy the fixture from the laptop

From the Shiroe repository, copy the fixture into a new test directory on the home server, then log in:

```bash
scp -r tools/https-probe HOME_SSH_USER@192.0.2.10:~/shiroe-https-probe
ssh HOME_SSH_USER@192.0.2.10
```

All addresses and accounts in this runbook are placeholders. Replace them before running commands; the documentation-only IP will not reach the home server.

The fixture has no generated certificate material in the repository. Generate the private key on the server in the next step. Do not copy a previously populated `certs/` directory between machines. Reuse the existing home SSH port configuration if it differs from the default.

## 2. Generate a short-lived test certificate on the home server

Prerequisites: Docker Compose, OpenSSL, and curl. The existing server reportedly has Compose. In the home-server shell:

```bash
cd ~/shiroe-https-probe
umask 077
mkdir -p certs
openssl req -x509 -newkey rsa:2048 -sha256 -nodes -days 7 \
  -keyout certs/key.pem -out certs/cert.pem \
  -subj '/CN=Shiroe connectivity probe' \
  -addext 'subjectAltName=IP:192.0.2.10,IP:127.0.0.1'
```

The certificate explicitly identifies the public IP and loopback test IP. Change the public IP before generation if the address changes. The certificate is self-signed and expires after seven days. Keep `key.pem` on the home server; distribute only the public `cert.pem` through the authenticated SSH connection. Certificate trust is explicit for each curl invocation and does not modify system trust stores.

## 3. Validate configuration, start, and check locally

```bash
docker compose config --quiet
docker compose run --rm --no-deps probe nginx -t
docker compose up -d
```

Check the exact response on the server:

```bash
test "$(curl --cacert certs/cert.pem --connect-timeout 10 --max-time 20 \
  --fail --silent --show-error https://127.0.0.1/health)" = \
  'shiroe-https-connectivity-ok' && echo 'PASS: verified local HTTPS and marker'
```

If startup fails, inspect `docker compose logs probe`. A port conflict should be resolved without stopping or replacing unrelated OMV services. This project has its own Compose name and does not modify other projects.

## 4. Make external TCP 443 reachable

If `192.0.2.10` is the router's WAN address, forward **external TCP 443 → home server LAN IP, TCP 443** in the router. Use the server's reserved/static LAN address, not loopback. Permit that port in any applicable server firewall. Do not change the working SSH forward, disable the firewall, or publish database ports. If the server itself owns the public address, the router forward is unnecessary.

The user's statement that port 443 is unused does not establish an existing forward or an open firewall. Test from outside the home network; a home-LAN test may fail because the router lacks hairpin NAT even when external access works.

## 5. Laptop control and Tuolumne test

On the laptop, copy **only the public certificate**:

```bash
scp HOME_SSH_USER@192.0.2.10:~/shiroe-https-probe/certs/cert.pem \
  /tmp/shiroe-probe-cert.pem
```

From an external network, test the home endpoint:

```bash
curl --cacert /tmp/shiroe-probe-cert.pem --connect-timeout 10 --max-time 20 \
  --fail --silent --show-error https://192.0.2.10/health
```

After the external control succeeds, copy the public certificate to LC and execute curl on the login node:

```bash
scp /tmp/shiroe-probe-cert.pem \
  YOUR_LC_USERNAME@tuolumne.llnl.gov:~/shiroe-probe-cert.pem
ssh YOUR_LC_USERNAME@tuolumne.llnl.gov \
  'curl --cacert ~/shiroe-probe-cert.pem --connect-timeout 10 --max-time 20 --fail --silent --show-error --write-out "\nhttp_status=%{http_code}\nremote_ip=%{remote_ip}\nssl_verify_result=%{ssl_verify_result}\n" https://192.0.2.10/health'
```

`192.0.2.10` is a documentation-only address; replace it with the actual home public IP everywhere, including the certificate SAN. Replace `HOME_SSH_USER` and `YOUR_LC_USERNAME` with the appropriate accounts. `LC_LOGIN_NODE_A/B` are redacted node identifiers. Use normal LC authentication. The HTTP request has no institutional research payload, and the probe needs no model credentials or home SSH key on LC. Leave the environment's permitted proxy configuration in effect; do not disable it as part of this test.

Success requires the exact marker, HTTP 200, and successful certificate verification. A proxy block page is not success. A timeout/refusal cannot by itself distinguish home forwarding problems from LC routing. A proxy may reject the self-signed origin certificate even though curl explicitly trusts it; such a failure does not establish that a publicly certified HTTPS endpoint would fail. Record the actual error before selecting another route.

### Certificate-chain failure on LC

On 2026-10-13, the user reported a successful laptop response but LC failed with `curl: (60) SSL certificate problem: self signed certificate in certificate chain`; see [the evidence record](../../docs/development/phase-0-core/validation/2026-10-13-home-https-lc-certificate-failure.md). LC's default web proxy may affect the presented chain, and a custom CA file may omit its issuer. Inspection is not confirmed.

First test LC's normal trust configuration. Log into Tuolumne using the existing SSH method, then run:

```bash
hostname
date -u
curl --version
curl --connect-timeout 10 --max-time 20 \
  --fail --silent --show-error \
  --write-out '\nhttp_status=%{http_code}\nssl_verify_result=%{ssl_verify_result}\n' \
  https://192.0.2.10/health
```

Omitting `--cacert` uses curl's configured default trust; it does not disable certificate checks. Preserve the environment's proxy settings. Success still requires the exact marker, HTTP 200, and verification success. If this fails, compare the copied certificate fingerprints and inspect TLS diagnostics before changing trust. An HTTPS proxy's own TLS verification uses separate `--proxy-cacert` configuration. Use trusted LC-provided CA material if required.

The follow-up command [passed from LC_LOGIN_NODE_B](../../docs/development/phase-0-core/validation/2026-10-13-tuolumne-home-https.md): exact marker, HTTP 200, and `ssl_verify_result=0`. This validates this probe request under the client's default trust configuration; the presented issuer/proxy path was not collected.

## 6. Cleanup and evidence

On the home server, stop this project after the test:

```bash
cd ~/shiroe-https-probe
docker compose down
```

Remove the test-only router/firewall rule if added, and delete the disposable certificate/key files when no longer needed. `compose down` leaves those files intact and stops only this project.

Save actual results with time, login node, destination, response, certificate fingerprint, proxy/route information (without credentials), and Nginx image/version. Return to [Phase 0 connectivity notes](../../docs/development/phase-0-core/planning/lc-connectivity-notes.md). HTTPS success does not validate OAuth, MCP, compute-node egress, or server availability over time.

## Sources

Local configuration/TLS checks passed; see [the validation record](../../docs/development/phase-0-core/validation/2026-10-13-https-fixture-local.md). After [home deployment, laptop HTTPS success, and an LC custom-certificate failure](../../docs/development/phase-0-core/validation/2026-10-13-home-https-lc-certificate-failure.md), [LC HTTPS passed using default trust](../../docs/development/phase-0-core/validation/2026-10-13-tuolumne-home-https.md). OAuth and Shiroe client integration remain untested.

- [Official Nginx image](https://hub.docker.com/_/nginx), [TLS configuration](https://nginx.org/en/docs/http/ngx_http_ssl_module.html), and [fixed HTTP responses](https://nginx.org/en/docs/http/ngx_http_rewrite_module.html#return).
- [Compose networking and port mappings](https://docs.docker.com/compose/how-tos/networking/).
- [OpenSSL certificate generation and subject alternative names](https://docs.openssl.org/3.0/man1/openssl-req/).
- [curl certificate verification](https://curl.se/docs/manpage.html#--cacert).

Privacy note: personal addresses, accounts, node identifiers, paths, precise times, and server fingerprints have been replaced or omitted where present. Placeholders preserve the reported test outcome; this document is not an unredacted transcript.
