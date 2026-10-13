#!/usr/bin/env python3
"""Check a TCP connection and SSH banner without sending credentials."""

import argparse
import socket
import sys
import time


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("host", help="Home server's publicly reachable hostname or IP")
parser.add_argument("port", type=int, help="Public SSH port, for example 22")
args = parser.parse_args()
if not 1 <= args.port <= 65535:
    parser.error("port must be between 1 and 65535")

print(f"client_host={socket.gethostname()}")
print(f"target={args.host}:{args.port}")
print(f"utc_time={time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")
started = time.monotonic()
try:
    with socket.create_connection((args.host, args.port), timeout=10) as connection:
        print("tcp_connected=yes", flush=True)
        # Bound pre-identification lines and total wait from an untrusted peer.
        deadline = time.monotonic() + 10
        for _ in range(10):
            banner = bytearray()
            while len(banner) < 255:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise TimeoutError("timed out waiting for an SSH banner")
                connection.settimeout(remaining)
                byte = connection.recv(1)
                if not byte:
                    raise ValueError("connection closed without an SSH banner")
                banner.extend(byte)
                if byte == b"\n":
                    break
            else:
                raise ValueError("identification line exceeded 255 bytes")
            if banner.startswith(b"SSH-"):
                print(f"ssh_banner={bytes(banner).rstrip()!r}")
                print("PASS: TCP connection and SSH banner received; no authentication attempted.")
                break
        else:
            raise ValueError("no SSH banner within 10 bounded lines")
except (OSError, ValueError) as error:
    print(f"FAIL: {type(error).__name__}: {error}")
    print("This does not identify the cause or establish whether HTTPS works.")
    sys.exit(1)
finally:
    print(f"elapsed_seconds={time.monotonic() - started:.2f}")
