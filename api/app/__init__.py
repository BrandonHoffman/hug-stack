import hug
import socket

host = socket.gethostname()

@hug.get("/")
def home():
    return "hello from %s" % (host)
