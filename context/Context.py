from pojo.Session import Session


class Context:

    def __init__(self, current_session: Session, language: str):
        self.current_session = current_session
        self.language = language
