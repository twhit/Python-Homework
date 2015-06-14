from http.server import HTTPServer, BaseHTTPRequestHandler
import psutil, datetime

class MyHTTPHandler(BaseHTTPRequestHandler):
	def do_GET(self):
             self.send_response(200)
             self.end_headers()
             response = ""
             boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
             cpu_util = psutil.cpu_percent(interval=1, percpu=True)
             mem = psutil.virtual_memory()

             with self.wfile as f:
                     response="<table width='40%' border=0><tr bgcolor='#CEF6F5'><td>BOOT TIME</td><td>" + boot_time + "</td></tr>"
                     response += "<tr><td>CPU UTILIZATION</td><td><table border=0 width='100%'>"
                     i = 1
                     for cpu in cpu_util:
                         response += "<tr><td>CPU {}</td><td bgcolor='#E2A9F3'> {}%</td></tr>".format(i, cpu)
                         i = i+1
                     response += "</table></td></tr><tr bgcolor='#CEF6F5'><td>AVAILABLE MEMORY</td><td>" + str(mem.available) + "</td></tr>"
                     response += "<tr><td>USED MEMORY</td><td>" + str(mem.used) + "</td></tr>"
                     response += "<tr bgcolor='#CEF6F5'><td>USED PERCENTAGE</td><td>" + str(mem.percent) + "</td></tr></table></div>"
                     f.write(bytes(response, 'utf-8'))
             return

server = HTTPServer(("", 8000), MyHTTPHandler)
server.serve_forever()
