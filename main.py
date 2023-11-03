import time

from bottle import run, get
from TESAT import receiver


@get("/")
def listen():
    print("received request")
    receiver()
    return


if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)
