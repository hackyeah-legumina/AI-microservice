from flask import Flask
from flask import request

from service.ModelService import ModelService

# instance of flask application
app = Flask(__name__)

model_service = ModelService()


@app.route("/", methods = ['GET'])
def hello_world():
    return model_service.handle_conversation_request(request)


if __name__ == '__main__':
    app.run()