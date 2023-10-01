from googletrans import Translator

from context.Context import Context
from service.executors.Executor import Executor


class LanguageExecutor(Executor):

    def __init__(self):
        self.translator = Translator()

    def execute(self, context: Context):
        if context.language != 'PL':
            translation = translator.translate(context.request, src='pl', dst='de')
            context.request = translation
