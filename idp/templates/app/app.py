from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = {
                "status": "healthy"
            }
            status_code = 200
        else:
            response = {
                "application": os.getenv("APP_NAME", "my-application"),
                "environment": os.getenv("ENVIRONMENT", "development"),
                "message": "Hello from the self-service application!"
            }
            status_code = 200

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


server = HTTPServer(("0.0.0.0", 8080), AppHandler)
print("Application listening on port 8080")
server.serve_forever()
