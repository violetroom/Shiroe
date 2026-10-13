# Home HTTPS control passed; LC certificate verification failed

- Date reported: 2026-10-13; exact execution time not supplied.
- Operator: user; evidence is pasted terminal output, not an assistant-run remote test.
- Destination: `https://192.0.2.10/health`.
- Client environments: personal laptop and an SSH session through `tuolumne.llnl.gov`. The actual login-node hostname was not reported; do not reuse the hostname from the earlier SSH probe.
- Trust configuration: the home endpoint's public `cert.pem` was copied to the laptop and then to LC using SCP. Both curl commands supplied that file with `--cacert`.

## Sanitized reported evidence

The laptop command returned the expected marker:

```text
shiroe-https-connectivity-ok
```

The LC command failed:

```text
curl: (60) SSL certificate problem: self signed certificate in certificate chain
More details here: https://curl.haxx.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the web page mentioned above.
```

Both used connect and total timeouts of 10 and 20 seconds, respectively, plus `--fail --silent --show-error`. The public certificate transfers reportedly completed (1188 bytes). No certificate fingerprints, curl/TLS versions, proxy details, HTTP status, or remote IP were supplied.

## Interpretation and limits

The home HTTPS endpoint responded with the expected marker over a certificate-verified laptop request. The laptop network location is unknown; this does not establish an independent external-network control or general internet reachability.

LC encountered a certificate-chain verification failure. There is no successful LC health response yet. The error does not identify whether the failed TLS peer was the origin, an inspecting intermediary, or an HTTPS proxy, and does not establish a firewall block. A mismatched copied certificate or client trust/backend behavior also remains possible.

[LC guidance](https://hpc.llnl.gov/services/green-collaboration-environment/guidelines-external-data-transfers) says external web traffic uses the institutional proxy by default. It does not prove TLS inspection for this request. [curl documentation](https://curl.se/docs/sslcerts.html) describes custom CA files and separate verification for HTTPS proxies. The supplied CA file may omit an institutional issuer; this is a hypothesis, not a confirmed cause.

## Next diagnostic

Try the same request using LC's default trust configuration, preserving its proxy settings and certificate verification. Record time, actual hostname, and curl version. Success requires the exact marker, HTTP 200, and successful verification. If verification still fails, compare the copied certificate fingerprints and collect filtered TLS/proxy diagnostics before choosing a CA bundle. Use an LC-provided trusted CA source if needed; do not promote an unverified peer certificate into a trust anchor.

No production TLS choice, routing change, or architecture decision follows from this failure. OAuth, MCP, Shiroe state access, and compute-node access remain untested.

## Subsequent result

The next user-run request from `LC_LOGIN_NODE_B` using default trust passed: exact marker, HTTP 200, and `ssl_verify_result=0`. See [the separate success record](2026-10-13-tuolumne-home-https.md). The statements above preserve the initial failed attempt; its precise certificate/proxy cause remains unconfirmed.

Privacy note: personal addresses, accounts, node identifiers, paths, precise times, and server fingerprints have been replaced or omitted where present. Placeholders preserve the reported test outcome; this document is not an unredacted transcript.
