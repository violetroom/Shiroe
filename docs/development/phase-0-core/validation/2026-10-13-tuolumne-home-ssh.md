# Tuolumne to home server — SSH-port connectivity

- Status: Passed for TCP connection and receipt of an SSH banner only
- Execution time: [EXECUTION_TIME_REDACTED]
- Tester: user; result supplied in the development conversation
- Client host: `LC_LOGIN_NODE_A`
- Destination: `192.0.2.10:22`
- Method: [probe_ssh.py](../../../../scripts/probe_ssh.py), streamed into Python on Tuolumne through the user's normal SSH login
- Reported elapsed time: 0.18 seconds for the probe, not a measured round-trip latency
- Credentials sent to destination by probe: none
- Script hash, Python version, and routing configuration at execution: not captured

## Reported result

The user ran the previously supplied command from their personal machine with their LC username. The sanitized probe output was:

```text
client_host=LC_LOGIN_NODE_A
target=192.0.2.10:22
utc_time=[EXECUTION_TIME_REDACTED]
tcp_connected=yes
ssh_banner=b'SSH-2.0-[SERVER_VERSION_REDACTED]'
PASS: TCP connection and SSH banner received; no authentication attempted.
elapsed_seconds=0.18
```

## Interpretation and scope

This supplies personal-test evidence that a process on the named Tuolumne login node could establish a TCP connection to the specified address/port and receive an SSH identification line at the recorded time. The probe uses a raw socket, not an HTTP proxy or a script-configured SSH forward. The outer SSH connection carries the program into Tuolumne; the program initiates the tested destination connection from there.

The banner is reported peer text, not cryptographic verification of server identity or independently measured hardware/software provenance. Success does not establish authenticated home SSH access, HTTPS/443 reachability, OAuth/MCP operation, compute-node egress, other LC-node/zone access, or continuing availability. The result does not imply network-policy approval for additional routes or protocols.

## Next check

Provide a small HTTPS endpoint at home and test it from the same environment with certificate verification and a known harmless response. Keep PostgreSQL private. Record the hostname, port, certificate trust, actual node, proxy/route, response, and time separately. No HTTPS endpoint exists yet according to the user's prior clarification.

Related: [connectivity plan](../planning/lc-connectivity-notes.md), [deployment decision](../decisions/0008-lc-home-server-target.md), and [personal-validation requirement](../decisions/0010-personal-claim-validation.md).

Privacy note: personal addresses, accounts, node identifiers, paths, precise times, and server fingerprints have been replaced or omitted where present. Placeholders preserve the reported test outcome; this document is not an unredacted transcript.
