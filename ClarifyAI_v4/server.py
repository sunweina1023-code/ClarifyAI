from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os

ROOT = Path(__file__).parent
os.chdir(ROOT)

if __name__ == "__main__":
    host, port = "127.0.0.1", 8000
    print(f"ClarifyAI v2 is running at http://{host}:{port}")
    print("Press Ctrl+C to stop the server.")
    ThreadingHTTPServer((host, port), SimpleHTTPRequestHandler).serve_forever()
