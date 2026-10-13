# Tuolumne-to-home HTTPS probe passed

- Date reported: 2026-10-13; exact execution time not supplied.
- Operator: user; evidence is pasted terminal output, not an assistant-run remote test.
- Client hostname: `LC_LOGIN_NODE_B`, as shown in the shell prompt.
- Destination: `https://192.0.2.10/health`.
- Trust: curl's configured default trust; no explicit `--cacert`, verification-disabling option, or proxy override in the reported command.

## Command and sanitized output

```text
[YOUR_LC_USERNAME@LC_LOGIN_NODE_B:~]$ curl --connect-timeout 10 --max-time 20 \
>   --fail --silent --show-error \
>   --write-out '\nhttp_status=%{http_code}\nssl_verify_result=%{ssl_verify_result}\n' \
>   https://192.0.2.10/health
shiroe-https-connectivity-ok

http_status=200
ssl_verify_result=0
[YOUR_LC_USERNAME@LC_LOGIN_NODE_B:~]$
```

## Result and scope

PASS: this Tuolumne login-node request received the exact probe marker, HTTP 200, and certificate verification result 0. The configured HTTPS route can reach the home probe. This supports retaining the accepted home-hosting target; moving the database to Oracle is not necessary to resolve this initial connectivity check.

The [previous attempt with the copied home certificate](2026-10-13-home-https-lc-certificate-failure.md) failed certificate-chain verification. The successful default-trust request is consistent with an institutional certificate/trust path omitted by the custom file. It does not conclusively identify TLS inspection: no peer certificate, issuer, fingerprint, proxy configuration, curl/TLS version, or client configuration was supplied. The test verifies the chain accepted by LC's client configuration, not an independently compared home certificate fingerprint. [curl's trust documentation](https://curl.se/docs/sslcerts.html) explains default/custom CA trust and separate HTTPS-proxy verification; [LC guidance](https://hpc.llnl.gov/services/green-collaboration-environment/guidelines-external-data-transfers) describes its default external web proxy.

This is one user-run probe from one login node. It does not test DNS for a future hostname, other LC nodes, compute-node egress, uptime, OAuth, API writes, MCP streaming, OpenCode's HTTP/TLS behavior, or persistent shared state. Those clients must respect the applicable proxy and trust configuration; curl success alone does not validate them.

## Follow-up

Return to plan step 0.2, defining core identity, revision, provenance (including system/hardware), and personal claim-validation contracts. The service prototype will need a maintained TLS endpoint and separate OAuth/client integration checks. The disposable probe can be stopped using the [cleanup instructions](../../../../tools/https-probe/README.md#6-cleanup-and-evidence).

Privacy note: personal addresses, accounts, node identifiers, paths, precise times, and server fingerprints have been replaced or omitted where present. Placeholders preserve the reported test outcome; this document is not an unredacted transcript.
