"""Committed size at HEAD of what imdbwatch ships. Prints web_bytes=<n> and worker_bytes=<n>.

web: web/src, web/public and web/index.html (the app that is built and served).
worker: src/*.js (the Cloudflare Worker).
"""
import subprocess

WEB_EXT = (".html", ".css", ".js", ".mjs", ".ts", ".tsx", ".svg", ".png", ".jpg", ".jpeg", ".webp",
           ".avif", ".gif", ".ico", ".woff", ".woff2", ".json", ".webmanifest", ".xml", ".txt", ".md")

listing = subprocess.run(["git", "ls-tree", "-r", "-l", "-z", "HEAD"], capture_output=True, check=True).stdout
web = 0
worker = 0
for entry in listing.split(b"\0"):
    if not entry:
        continue
    meta, path = entry.decode("utf-8", "replace").split("\t", 1)
    size = meta.split()[3]
    if size == "-":
        continue
    low = path.lower()
    if low.endswith(".d.ts"):
        continue
    if path.startswith("src/") and low.endswith(".js"):
        worker += int(size)
    elif (path.startswith("web/src/") or path.startswith("web/public/") or path == "web/index.html") and low.endswith(WEB_EXT):
        web += int(size)
print(f"web_bytes={web}")
print(f"worker_bytes={worker}")
