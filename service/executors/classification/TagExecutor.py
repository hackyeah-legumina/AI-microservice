from context.Context import Context
from service.executors.Executor import Executor
from service.executors.classification.FindStudiesExecutor import FindStudiesExecutor


class TagExecutor(Executor):

    def __init__(self):
        self.tag_dict_executor = {
            "FindStudies": FindStudiesExecutor(),
            # "FAQ": FaqExecutor()
        }

    def execute(self, context: Context):
        if context.classification_tag not in self.tag_dict_executor.keys():
            return "INVALID CLASSIFICATION TAG"
        else:
            self.tag_dict_executor[context.classification_tag].execute(context)
