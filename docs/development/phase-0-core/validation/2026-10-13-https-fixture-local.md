# Local validation of the temporary HTTPS fixture

- Date: 2026-10-13
- Status: Passed locally; home/LC HTTPS route untested
- Tester: assistant-run checks in the shared development environment
- Fixture: [configuration and runbook](../../../../tools/https-probe/README.md)
- Server image: `nginx:1.30.5-alpine`
- Pulled image digest: `sha256:0985e772fb9f729e6fa0980da05fca5d9c468e870eed43071545afa9d2e27d94`
- Docker daemon: 29.5.2, local Colima instance
- Route: ephemeral host port bound to `127.0.0.1`, forwarded to container port 8443
- Certificate: disposable, self-signed, SAN `IP:127.0.0.1`, trusted explicitly by curl

## Checks performed

1. `nginx -t` accepted the repository configuration with the generated certificate/key.
2. Verified HTTPS returned exactly `shiroe-https-connectivity-ok` with its newline.
3. `/nginx.conf` returned HTTP 404 rather than exposing configuration content.
4. Curl without explicit trust rejected the self-signed certificate with exit code 60.
5. Curl trusting the certificate but requesting `localhost` rejected the hostname mismatch with exit code 60.

The disposable container and generated certificate/key were removed. The public Nginx image remains cached locally. The existing Docker credential configuration was left unchanged; the checks used an isolated temporary client configuration.

The local Docker installation has no Compose plugin, so these checks used direct Docker commands with the same image, mounts, and container port. Compose execution itself remains untested locally; the runbook includes `docker compose config --quiet` and `nginx -t` for the home setup. No home-server, router, LC, OAuth, or MCP changes/tests were performed.
