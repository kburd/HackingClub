import urllib.request

while True:
    link = input("Request: ")
    print(str(urllib.request.urlopen(link).read()))