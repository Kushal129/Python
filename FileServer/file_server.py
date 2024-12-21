import os
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer

class FileExplorerHandler(SimpleHTTPRequestHandler):
    """
    A custom HTTP request handler to serve files and provide a file list in JSON format.
    """
    def list_files(self, directory):
        """
        Generate a list of files and directories in the specified directory.
        Each item includes its name and type (file or folder).
        """
        try:
            items = os.listdir(directory)  # Get all files and folders in the directory
            files = [{"name": item, "type": "folder" if os.path.isdir(os.path.join(directory, item)) else "file"} for item in items]
            return files
        except Exception as error:
            print(f"Error accessing directory: {error}")
            return []  # Return an empty list if there's an error

    def do_GET(self):
        """
        Handle GET requests. Serves JSON data for `/api/list` and static files otherwise.
        """
        if self.path == '/api/list':
            # Respond with a JSON list of files in the current directory
            files = self.list_files(".")
            self.send_response(200)  # HTTP OK
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(files).encode())
        else:
            # Serve regular files or directories
            super().do_GET()

def run_server(port=8000):
    """
    Starts the HTTP server on the specified port.
    """
    print(f"Starting server on port {port}...")
    httpd = HTTPServer(('', port), FileExplorerHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
