# LLNL LC / Tuolumne connectivity notes

Date: 2026-10-13. Status: user-run SSH-port and LC HTTPS probes passed; authenticated Shiroe service connectivity untested.

## Target and intended flow

The user named LLNL LC, initially Tuolumne, and confirmed home database storage is acceptable. The server preference is recorded in [0008](../decisions/0008-lc-home-server-target.md).

```text
Personal machine -- SSH with LC authentication --> Tuolumne login node
                                                   |
                                             OpenCode / CLI
                                                   |
                                   outbound HTTPS, Shiroe OAuth
                                   (LC proxy/route as required)
                                                   |
                                      Home Shiroe API / MCP
                                                   |
                                            Private database
```

The client running on Tuolumne starts the Shiroe request. LC's PIN/RSA login authenticates access to LC; Shiroe separately authenticates its API/MCP caller. SSH login does not automatically create the outbound application connection. OAuth setup for a headless client requires its own check.

## Public evidence and its limits

- [Tuolumne platform page](https://hpc.llnl.gov/hardware/compute-platforms/tuolumne) lists CZ and distinguishes login from compute resources. It cautions against computationally intensive work on login nodes. This supports selecting a lightweight client on a login node, not an LC-hosted Shiroe database or heavy extraction process.
- [LC authentication guidance](https://hpc.llnl.gov/accounts/accessing-lc-systems/authenticating) documents PIN/RSA authentication for relevant LC access. It does not authenticate requests to the user's independent service.
- [External-transfer guidance](https://hpc.llnl.gov/services/green-collaboration-environment/guidelines-external-data-transfers) describes the institutional proxy for external web traffic, possible destination blocking, and procedures for large transfers and outgoing data. It is not an approval or tested network recipe for Shiroe's small API calls.

Tuolumne's public zone assignment does not establish unrestricted egress. No public page reviewed demonstrates that the home address, future Shiroe hostname, or OAuth issuer is reachable from the user's particular login node. Other LC systems/zones and compute nodes need separate checks if included later.

## Small checks before deployment selection

1. Choose a hostname/TLS endpoint at home using the existing ingress if suitable. Keep database access behind the application.
2. From the actual login node, request a non-sensitive health/capability endpoint. Record DNS/TLS success, proxy behavior, response type/content, and timing. A proxy block page is not a successful API response.
3. Verify OAuth discovery, initial login, token use/refresh, and read/write authorization with pinned OpenCode and CLI clients. Keep LC credentials and Shiroe credentials separate.
4. Demonstrate one fixture record written/read across machines; then test conflicts/retries and restart persistence.

Use the permitted LC route. If the direct HTTPS/proxy route fails, determine an approved alternative before changing topology; do not treat forwarding or a cloud relay as automatically permitted. Keep the initial batch workflow independent of compute-node internet access and register results through a permitted client location.

The list above defines the wider deployment checks. Preliminary SSH-port and HTTPS probe results are recorded below; OAuth and actual Shiroe state access remain untested. Connectivity probes contain no institutional research payload.

## Preliminary SSH-port probe

The user clarified that the home server currently has SSH access but no public HTTPS endpoint. Before setting up HTTPS, use [the diagnostic script](../../../../scripts/probe_ssh.py) to test the existing public SSH port from the actual Tuolumne login node. It uses Python's standard library, opens one TCP connection, waits for an SSH identification line, and closes without sending credentials or authenticating.

From the repository on the personal machine, substitute the actual LC username/SSH destination. This streams the script into Python running on Tuolumne; it does not install or copy a program there. Authenticate to LC using the normal SSH method:

```bash
ssh YOUR_LC_USERNAME@tuolumne.llnl.gov 'python3 - 192.0.2.10 22' < scripts/probe_ssh.py
```

Use the same public port used for the working home SSH connection; change `22` if necessary. Run the same script from the personal machine as a control if the LC attempt fails. Invoke the script on Tuolumne itself rather than against a laptop tunnel listener; a forwarded route is a different experiment.

- `PASS` establishes that this client connected to this port and received an SSH-style banner at the recorded time. It does not verify server identity cryptographically, prove general internet access, or test HTTPS, OAuth, or MCP.
- `tcp_connected=yes` followed by failure establishes a TCP connection but no accepted SSH banner.
- A timeout, refusal, or other failure does not by itself identify LC blocking. The home listener, router/forwarding, firewalls, and selected address/port are also possible causes.
- This raw TCP probe does not use HTTP proxy settings. Port 22 failure does not establish port 443 failure; HTTPS still needs a separate endpoint and test through the permitted LC web route.

The script's local checks use loopback socket fixtures and can be run with `python3 -m unittest discover -s tests -p 'test_probe_ssh.py'`. Five checks passed on 2026-10-13: SSH banner following a notice/fragmented prefix, non-SSH response, early disconnect, overlong identification line, and invalid port. They also check that the probe sends no data to the endpoint.

## User-run result — 2026-10-13

The probe passed from `LC_LOGIN_NODE_A` to `192.0.2.10:22` at `[EXECUTION_TIME_REDACTED]`, with a reported total probe time of 0.18 seconds and an SSH identification line. See [the sanitized validation record](../validation/2026-10-13-tuolumne-home-ssh.md) for reported output, provenance, and limits. The tested TCP/SSH-banner path worked; HTTPS, OAuth, MCP, and other client/node routes remained untested at that point.

## Temporary HTTPS fixture

The user reports port 443 is unused. [The HTTPS fixture and runbook](../../../../tools/https-probe/README.md) provide a one-container fixed-response endpoint and an explicitly trusted seven-day test certificate. This avoids requiring a domain for the initial check and preserves certificate verification. It is a diagnostic configuration, not selection of Nginx or a self-signed certificate for production Shiroe.

The fixture passed [local Nginx/TLS checks](../validation/2026-10-13-https-fixture-local.md). The user subsequently deployed it at home: [laptop HTTPS returned the marker, but LC custom-certificate verification failed](../validation/2026-10-13-home-https-lc-certificate-failure.md). A follow-up [request from LC_LOGIN_NODE_B using default trust passed](../validation/2026-10-13-tuolumne-home-https.md), returning the exact marker, HTTP 200, and verification result 0. Router/firewall and proxy configuration were not inspected. The test supports the home target while leaving production TLS and actual OAuth/API/MCP client behavior to validate.

Privacy note: personal addresses, accounts, node identifiers, paths, precise times, and server fingerprints have been replaced or omitted where present. Placeholders preserve the reported test outcome; this document is not an unredacted transcript.
