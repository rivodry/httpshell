from http.server import BaseHTTPRequestHandler, HTTPServer
HTTP_STATUS_OK = 200
IP = '0.0.0.0'
PORT = 5000
class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        cmd = input(">")
        self.send_response(HTTP_STATUS_OK)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(cmd.encode())
if __name__== '__main__':
    ser = HTTPServer((IP,PORT),ServerHandler)
    try:
        print("Server started")
        ser.serve_forever()
    except:
        print("stopping")
        ser.server_close()
