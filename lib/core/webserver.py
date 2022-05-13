import json
from lib.utils.config import config
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from lib.core.db import dbEngine

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
        out = ""
        reqpath = self.path
        if self.path.find("city") > 0:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            out = self.loadResult()
            self.wfile.write(bytes(out, "utf-8"))
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>For result Trend click:</p> <a href='/city'>City raw result</a>", "utf-8"))
            self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))

    
    def do_POST(self):
        pass

    def loadResult(self) -> any:
        stmt = "Select * from city_trend order by point desc"
        db_persist = dbEngine()
        db_persist.exeuteQuery(stmt,None)
        result = []
        for res in db_persist.resu:
            item = {
                "id" : res[0],
                "name" : res[1],
                "lon" : res[2],
                "lat" : res[3],
                "point" : res[4]
            }
            result.append(item)
        return json.dumps(result)

        
