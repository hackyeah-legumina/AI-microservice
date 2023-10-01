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
        (context.classification_tag, context.response) = self.chatbot_response(context.request["text"])

    def lemmatize_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        return sentence_words

    def bow(self, sentence, words):
        sentence_words = self.lemmatize_sentence(sentence)
        bag = [0] * len(words)
        for s in sentence_words:
            for i, w in enumerate(words):
                if w == s:
                    bag[i] = 1

        return np.array(bag)

    def predict_class(self, sentence, model):
        p = self.bow(sentence, WORDS)
        res = model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({"intent": CLASSES[r[0]], "probability": str(r[1])})
        return return_list

    def getResponse(self, ints, intents_json):
        classification_tag = ints[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag'] == classification_tag:
                result = random.choice(i['responses'])
                break

        return (classification_tag, result)

    def chatbot_response(self, text):
        ints = self.predict_class(text, CLASSIFICATION_MODEL)
        (classification_tag, res) = self.getResponse(ints, INTENTS)
        return classification_tag, res
