from context.Context import Context
from service.executors.Executor import Executor


class FindStudiesExecutor(Executor):

    def execute(self, context: Context):
        if ['CITY'] == context.labels:
            pass
        elif ['UNIVERSITY'] == context.labels:
            pass
        elif ['CITY', 'SUBJECT'] == context.labels:
            pass