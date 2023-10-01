from context.Context import Context
from context.StaticContext import NLP_MODEL
from service.executors.Executor import Executor


class NerModelExecutor(Executor):

    def execute(self, context: Context):
        doc = NLP_MODEL(context.request["text"])
        context.labels = [ent.label_ for ent in doc.ents]
        context.doc = doc
