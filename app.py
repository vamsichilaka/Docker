from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 5000

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = "Build Version Running | Webserver Active"
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

if __name__ == "__main__":
    print(f"Server running on port {PORT}...")
    with HTTPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()
