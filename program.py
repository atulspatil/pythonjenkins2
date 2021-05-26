from flask import Flask
server = Flask(__name__)


@server.route("/")
def jenkins_second():
    return "This is second Jenkins project ! Now adding new line..."


if __name__ == "__main__":
    server.run()

