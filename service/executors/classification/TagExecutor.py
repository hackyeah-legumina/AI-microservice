from context.Context import Context
from service.executors.Executor import Executor
from service.executors.ResponseGeneratorExecutor import ResponseGeneratorExecutor
from service.executors.classification.FindStudiesExecutor import FindStudiesExecutor


class TagExecutor(Executor):

    def __init__(self):
        self.tag_dict_executor = {
            "FindStudies": FindStudiesExecutor(),
            # "FAQ": FaqExecutor()
        }

        self.post_exec = ResponseGeneratorExecutor()

    def execute(self, context: Context):
        if context.classification_tag not in self.tag_dict_executor.keys():
            return {
                "text": context.response
            }
        else:
            self.tag_dict_executor[context.classification_tag].execute(context)
            self.post_exec.execute(context)

