import http.server
import socketserver
import json
from lock import *
from json_functions import *
import urllib.parse

# Set the port you want to use (e.g., 8000)
port = 8000

# Define the handler for your server
class JSONHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        lock=GlobalLocks().global_lock
        parsed_url = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        key=None
        result={'result':False}
        if 'key' in query_params:
            key = query_params['key'][0]
        # Set the response headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        with lock:
        # Create a JSON response
            
            premium_dict=load_user_data(target_file='data_ninjatrader.json')
            if key and key in premium_dict:
                result = premium_dict[key]
            response_json = json.dumps(result)
            self.wfile.write(response_json.encode('utf-8'))

def start_server():
    global port
    # Create the server
    with socketserver.TCPServer(("", port), JSONHandler) as httpd:
        print(f"Serving at port {port}")
        httpd.serve_forever()