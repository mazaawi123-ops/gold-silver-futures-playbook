#!/usr/bin/env python3
"""Minimal static file server for previewing outputs/index.html.

Avoids `python -m http.server`, whose argparse default calls os.getcwd()
(denied by the sandbox here). We pass an explicit directory instead.
"""
import http.server
import socketserver

PORT = 8765
DIRECTORY = "/Users/mo/Desktop/Playbook/outputs"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, *args):
        pass


class Server(socketserver.TCPServer):
    allow_reuse_address = True


with Server(("127.0.0.1", PORT), Handler) as httpd:
    httpd.serve_forever()
