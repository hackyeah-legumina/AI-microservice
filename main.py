from flask import Flask
from flask import request

from context.StaticContext import init_static_context
from service.ModelService import ModelService

# instance of flask application
app = Flask(__name__)

model_service = ModelService()
init_static_context()


@app.route("/", methods = ['POST'])
def hello_world():
    return model_service.handle_conversation_request(request)


if __name__ == '__main__':
    app.run(port=2137)