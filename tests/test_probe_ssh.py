"""Local socket checks; these do not connect to LC or the home server."""

from pathlib import Path
import socket
import subprocess
import sys
import threading
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/probe_ssh.py"


class ProbeSSHTests(unittest.TestCase):
    def probe(self, lines):
        with socket.socket() as listener:
            listener.bind(("127.0.0.1", 0))
            listener.listen(1)
            listener.settimeout(15)
            port = listener.getsockname()[1]
            received = []

            def respond():
                with listener.accept()[0] as connection:
                    for line in lines:
                        connection.sendall(line)
                    connection.shutdown(socket.SHUT_WR)
                    # Wait for the client to close; it must send no credentials.
                    connection.settimeout(10)
                    try:
                        received.append(connection.recv(1024))
                    except ConnectionResetError:
                        # An early close with unread fixture bytes may reset TCP.
                        received.append(b"")

            thread = threading.Thread(target=respond)
            thread.start()
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "127.0.0.1", str(port)],
                capture_output=True, text=True, timeout=15,
            )
            thread.join(timeout=15)
            self.assertFalse(thread.is_alive())
            self.assertEqual(received, [b""], "probe must send no credentials or data")
            return result

    def test_banner_after_notice_and_fragmented_prefix(self):
        result = self.probe([b"Welcome\r\n", b"S", b"SH-2.0-local-test\r\n"])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS:", result.stdout)
        self.assertIn("tcp_connected=yes", result.stdout)

    def test_non_ssh_response_is_not_success(self):
        result = self.probe([b"HTTP/1.1 403 Forbidden\r\n"])
        self.assertEqual(result.returncode, 1)
        self.assertNotIn("PASS:", result.stdout)

    def test_closed_connection_is_not_success(self):
        result = self.probe([])
        self.assertEqual(result.returncode, 1)
        self.assertIn("without an SSH banner", result.stdout)

    def test_overlong_banner_is_not_success(self):
        result = self.probe([b"SSH-2.0-" + b"x" * 248 + b"\n"])
        self.assertEqual(result.returncode, 1)
        self.assertIn("exceeded 255 bytes", result.stdout)

    def test_invalid_port_is_rejected(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "127.0.0.1", "0"],
            capture_output=True, text=True, timeout=5,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("port must be", result.stderr)


if __name__ == "__main__":
    unittest.main()
