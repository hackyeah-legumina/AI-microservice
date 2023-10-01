from flask import Flask
from flask import request

from context.StaticContext import init_static_context
from service.ModelService import handle_conversation_request

app = Flask(__name__)

init_static_context()


@app.route("/", methods = ['POST'])
def hello_world():
    return handle_conversation_request(request)


if __name__ == '__main__':
    app.run(port=2137)