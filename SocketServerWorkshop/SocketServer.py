#Simple socket server using threads
from http.server import BaseHTTPRequestHandler, HTTPServer

requestString = ''

# Used for website example
number = 0

def getValue(key):

    paramString = requestString.split(" ")[1].strip("/")
    pairs = paramString.split("&")

    for i in range(len(pairs)):
        pair = pairs[i].split("=")

        if len(pair) == 1:
            return

        tempKey = pair[0]
        tempValue = pair[1]

        if tempKey == key:

            return tempValue


def createGUI():

    message = ""
    lines = open("resource.html", "r").readlines()

    for line in lines:

        if line.strip() == "*number*":
            message += "<h1>" + str(number) + "</h1>"

        else:
            message += line

    return message

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):

        global requestString
        global number

        requestString = self.requestline

        mode = getValue("mode")
        message = format("%s is not a mode") % mode

        if mode == "echo":

            # Send message back to client
            message = getValue("text")

        if mode == "add":

            name = getValue("name")
            id = getValue("id")
            type = getValue("type")

            file = open("database.txt", "a")
            file.write(name + "," + id + "," + type + "\n")
            file.close()

            message = "Added to Database"

        if mode == "retrieve":

            file = open("database.txt", "r")
            lines = file.readlines()

            index = int(getValue("index"))

            message = lines[index]

        if mode == "init":
            message = createGUI()

        if mode == "increment":
            number += 1
            message = createGUI()



        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        self.send_header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        self.end_headers()

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))

        return


def run():

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()