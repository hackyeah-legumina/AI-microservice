from context.Context import Context
from service.executors.Executor import Executor
from util.extractor.header_extractor import extract_session_id, extract_lang
from util.managers.SessionManager import SessionManager
from pojo.Session import Session


class ModelService:
    def __int__(self):
        self.sessions = {}
        self.session_manager = SessionManager()
        self.action_executors: list[Executor] = []

    def handle_conversation_request(self, request):
        session_id = extract_session_id(request)
        language = extract_lang(request)
        session = self.get_session(session_id)

        context = Context(session, language)

        for executor in self.action_executors:
            executor.execute(context)

    def get_session(self, session_id) -> Session:
        if session_id not in self.sessions:
            session = self.session_manager.create_session()
            self.sessions[session.id] = session
        else:
            session = self.sessions[session_id]

        return session
