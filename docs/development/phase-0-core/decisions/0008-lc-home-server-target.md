# 0008 — Target LLNL LC and retain the home-server deployment

- Date: 2026-10-13
- Phase / plan steps: 0 / 0.5, 0.6
- Status: Accepted direction; SSH and HTTPS probes passed; Shiroe integration untested
- Decision maker: user
- Refines: [0003 — User-hosted deployment](0003-user-hosted-deployment.md)

## Context and decision

The target HPC environment is LLNL Livermore Computing (LC), with Tuolumne the initial named system. Preserve the portable, user-hosted product design and prioritize making the user's home-hosted database/service work from LC.

The user confirms that keeping the database on their local server is acceptable from a data-storage perspective. Record this as user-provided confirmation, not an independently obtained institutional policy ruling. Oracle Cloud remains unselected.

The user currently logs into Tuolumne using SSH with a PIN and RSA token. No credential values are needed or recorded.

## Why and alternatives

Reuse the chosen home infrastructure and avoid an unnecessary cloud migration. First evaluate the LC-to-home service route. Moving only PostgreSQL would leave the client-facing home endpoint unchanged; a complete cloud deployment or an approved relay remains a fallback if the home route is infeasible and the user selects it.

## Consequences and validation

The intended direct flow is: user SSH login → OpenCode/CLI running on a Tuolumne login node → outbound authenticated HTTPS to Shiroe at home → private PostgreSQL. Application requests initiate the Shiroe connection; SSH login alone does not connect or authenticate the client to Shiroe. Responses return on the client-initiated connection. No Shiroe-initiated connection into LC is required for this design.

LC's public platform page lists Tuolumne in CZ. Published external-transfer guidance describes the institutional web proxy and outgoing-data procedures; it does not establish reachability or permission for this particular endpoint. Home storage confirmation and LC network access are separate facts. Apply the user's confirmation without claiming that all other transfers or cloud/inference uses are approved.

Test from the actual login node: DNS, HTTPS/TLS, response contents through the proxy, and Shiroe OAuth login/refresh. Do not assume compute nodes have the same route. Keep batch execution independent of a live Shiroe connection initially; later result registration can occur from a permitted client location. No node, home server, or endpoint has been contacted in this session.

## Evidence

User, 2026-10-13:

> the target hpc system/systems is LLNL's LC. Keeping the DB on my local is fine from a data storage perspective. I'd like to make that work if possible.

> Currently, I connect to tuolumne using ssh through my pin and an rsa token.

Public sources checked on 2026-10-13: [Tuolumne](https://hpc.llnl.gov/hardware/compute-platforms/tuolumne), [LC authentication](https://hpc.llnl.gov/accounts/accessing-lc-systems/authenticating), and [external data transfer guidance](https://hpc.llnl.gov/services/green-collaboration-environment/guidelines-external-data-transfers). See [connectivity notes](../planning/lc-connectivity-notes.md) for source limits and proposed checks.

## Subsequent validation — 2026-10-13

The user ran the preliminary probe on `LC_LOGIN_NODE_A`; TCP connection and receipt of an SSH banner from `192.0.2.10:22` passed at `[EXECUTION_TIME_REDACTED]`. [The sanitized validation record](../validation/2026-10-13-tuolumne-home-ssh.md) preserves reported outcomes and scope. Earlier untested statements describe the decision-time state. HTTPS, OAuth, MCP, and actual service access remained untested at that point.

Later that day, the user reported a verified laptop HTTPS response with the expected marker and an LC HTTPS failure (`curl: (60) SSL certificate problem: self signed certificate in certificate chain`). See [the HTTPS evidence](../validation/2026-10-13-home-https-lc-certificate-failure.md). The proxy/trust cause remains unresolved; this does not change the home-hosting decision. OAuth, MCP, and actual Shiroe access remain untested.

The subsequent request from `LC_LOGIN_NODE_B` using curl's default trust returned the exact marker, HTTP 200, and `ssl_verify_result=0`. [The passed HTTPS record](../validation/2026-10-13-tuolumne-home-https.md) preserves the command and scope. The home target has a working initial HTTPS route from this login node; the exact proxy/certificate path and authenticated Shiroe/client integration remain unverified.

Privacy note: personal addresses, accounts, node identifiers, paths, precise times, and server fingerprints have been replaced or omitted where present. Placeholders preserve the reported test outcome; this document is not an unredacted transcript.
