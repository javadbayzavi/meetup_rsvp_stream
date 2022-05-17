import codecs
from threading import Thread
import json
from lib.utils.config import config
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from lib.core.db import dbEngine

class serverManager(Thread):
    def run(self):
        webserver.startUp()

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
        if self.path.find("city") > 0:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header('Access-Control-Allow-Origin:' , '*')
            self.end_headers()
            out = self.loadResult()
            self.wfile.write(bytes(out, "utf-8"))

        elif self.path.find("summary") > 0:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header('Access-Control-Allow-Origin:' , '*')
            self.end_headers()
            out = self.renderSummary()
            self.wfile.write(bytes(out, "utf-8")) 

        elif self.path.find("summaries") > 0:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header('Access-Control-Allow-Origin:' , '*')
            self.end_headers()
            out = self.getSummary()
            self.wfile.write(bytes(out, "utf-8"))  

        elif self.path.find("meetup") > 0:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header('Access-Control-Allow-Origin:' , '*')
            self.end_headers()
            out = self.loadJson()
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

    def getSummary(self , limit = 0):
        db_persist = dbEngine()
        stmt = "SELECT SUM(`point`) FROM `city_trend`"
        db_persist.exeuteQuery(stmt,None)
        total = int(db_persist.resu[0][0])
        stmt = "SELECT name , (`point` / " + str(total) + " * 100) AS `percent` FROM `city_trend` order by `percent` desc"
        db_persist.exeuteQuery(stmt,None)
        result = []
        for res in db_persist.resu:
            item = {
                "x" : res[0],
                "y" : str(res[1])
            }
            result.append(item)
        if limit == 0:
            return json.dumps(result)
        else:
            limititem = []
            for x in range(limit):
                limititem.append(result.pop())
            return json.dumps(limititem)
        

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

    def loadJson(self):
        data = ""
        with open('meetup.json',mode="r+", encoding="utf8") as f:
            try:
                f.seek(0)
                line = f.readline()
                data = json.dumps(json.loads(line))
                lines = f.readlines()[1:]
                f.seek(0)
                f.truncate()
                f.writelines(lines)
            except Exception as error:
                pass
            finally:
                return data
 
    def renderSummary(self):
        f = codecs.open("summary.html", 'r')
        content = f.read()
        content = content.replace('piedata-bereplacedhere', self.getSummary(10))
        return content

