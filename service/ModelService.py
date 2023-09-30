from extractor.header_extractor import extract_session_id, extract_lang
from managers.SessionManager import SessionManager
from pojo.Session import Session


class ModelService:
    def __int__(self):
        self.sessions: list[Session] = []
        self.session_manager = SessionManager()

    def handle_conversation_request(self, request):
        session_id = extract_session_id(request)
        language = extract_lang(request)

        if session_id not in self.sessions:
            self.session_manager.create_session()

        # do sth for different language


