from lib.utils.config import config
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import time

class webserver(BaseHTTPRequestHandler):
    @staticmethod
    def startUp():
        #attache a server handler to this handler with specified host and port. 
        webServer = HTTPServer((config.WEBSERVER_HOST, config.WEBSERVER_PORT), webserver)

        # Make sure the server is created at current directory
        os.chdir('.')

        try:
            webServer.serve_forever()
        except KeyboardInterrupt:
            pass

    #TODO: get function must be expanded to handle requests from react based app. response shold be in json format
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
    
    def do_POST(self):
        pass

