from context.Context import Context
from service.executors.ClassificationModelExecutor import ClassificationModelExecutor
from service.executors.Executor import Executor
from service.executors.NerModelExecutor import NerModelExecutor
from service.executors.PrepareDataExecutor import PrepareDataExecutor
from service.executors.ResponseGeneratorExecutor import ResponseGeneratorExecutor
from util.extractor.header_extractor import extract_session_id, extract_lang
from util.managers.SessionManager import SessionManager
from pojo.Session import Session

sessions = {}
session_manager = SessionManager()
action_executors: list[Executor] = [
    ClassificationModelExecutor()
]


class ModelService:

    def handle_conversation_request(self, request):
        session_id = extract_session_id(request)
        language = extract_lang(request)
        session = self.get_session(session_id)

        context = Context(session, language, request=request.get_json(force=True))

        for executor in action_executors:
            executor.execute(context)

        return context.response

    def get_session(self, session_id) -> Session:
        if session_id not in sessions.keys():
            session = session_manager.create_session()
            sessions[session.id] = session
        else:
            session = sessions[session_id]

        return session
