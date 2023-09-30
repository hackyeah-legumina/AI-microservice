from abc import ABC, abstractmethod

from context.Context import Context


class Executor(ABC):

    @abstractmethod
    def execute(self, context: Context):
        pass
