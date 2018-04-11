from http.server import BaseHTTPRequestHandler, HTTPServer
from Model import Model
from View import View

model = Model()
view = View()

initialized = False


class RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):

        global model
        global view
        global initialized

        if initialized:
            model.update()

        else:
            initialized = True

        data = view.generateImage(model.game.gameBoard)

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'image/png')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.end_headers()

        # Write content as utf-8 data
        self.wfile.write(data)
        return


def run():

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Running Span...')
    httpd.serve_forever()


run()

