
Mini File Explorer Instructions

This mini file explorer allows you to list and explore files and folders from a server running a Python HTTP server. The server exposes files and folders over a specific port, and users can view and download files through a simple web interface.

Steps to Use:

1. Folder Setup:
   - Place the Python file (file_explorer.py) and the HTML file (index.html) inside the folder you want to serve.
   - Ensure that your folder contains files or subfolders you want to display through the file explorer.

2. Run Python HTTP Server:
   - On the server (where the files are located), navigate to the folder where you placed the files.
   - Open a terminal and run the following command:
     python3 -m http.server 8000
   - This will start the server and expose the files in the folder over HTTP on port 8000.

3. Access from Another PC:
   - On another machine (client), open a web browser.
   - When the page loads, it will ask for the server's IP address and port number.
   - Enter the IP address and port of the server (e.g., 192.168.x.x:8000) when prompted.
   - Once entered, the file explorer will display all the files and folders in the server's directory.

Notes:
   - Make sure both the client and server machines are connected to the same network for IP address access to work.
   - This mini file explorer assumes the server is running the Python HTTP server on the specified port.
