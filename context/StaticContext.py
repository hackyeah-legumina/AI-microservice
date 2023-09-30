import spacy
from keras.models import load_model
import json
import pickle

NLP_MODEL = spacy.load("chatbot_data/model-best")
CLASSIFICATION_MODEL = load_model('chatbot_data/chatbot_model.h5')
INTENTS = json.loads(open('chatbot_data/intents.json').read())
WORDS = pickle.load(open('chatbot_data/words.pkl', 'rb'))
CLASSES = pickle.load(open('chatbot_data/classes.pkl', 'rb'))


def init_static_context():
    pass
