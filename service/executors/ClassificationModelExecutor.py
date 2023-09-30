from context.Context import Context
from context.StaticContext import CLASSES, WORDS, NLP_MODEL, INTENTS, CLASSIFICATION_MODEL
from service.executors.Executor import Executor
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import random

lemmatizer = WordNetLemmatizer()


class ClassificationModelExecutor(Executor):
    def execute(self, context: Context):
        context.response = self.chatbot_response(context.request["text"])

    def clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        return sentence_words

    def bow(self, sentence, words, show_details=True):
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0] * len(words)
        for s in sentence_words:
            for i, w in enumerate(words):
                if w == s:
                    bag[i] = 1
                    if show_details:
                        print("found in bag: %s" % w)

        return np.array(bag)

    def predict_class(self, sentence, model):
        p = self.bow(sentence, WORDS, show_details=False)
        res = model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({"intent": CLASSES[r[0]], "probability": str(r[1])})
        return return_list

    def getResponse(self, ints, intents_json):
        tag = ints[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag'] == tag:
                result = random.choice(i['responses'])
                break
        return result

    def chatbot_response(self, text):
        ints = self.predict_class(text, CLASSIFICATION_MODEL)
        res = self.getResponse(ints, INTENTS)
        return res
