from context.Context import Context
from service.executors.ClassificationModelExecutor import ClassificationModelExecutor
from service.executors.Executor import Executor
from service.executors.LanguageExecutor import LanguageExecutor
from service.executors.NerModelExecutor import NerModelExecutor
from service.executors.ResponseGeneratorExecutor import ResponseGeneratorExecutor
from service.executors.classification.TagExecutor import TagExecutor
from service.header_extractor import extract_session_id, extract_lang
from pojo.SessionManager import SessionManager
from pojo.Session import Session

sessions = {}
session_manager = SessionManager()
action_executors: list[Executor] = [
    LanguageExecutor(),
    ClassificationModelExecutor(),
    NerModelExecutor(),
    TagExecutor()
]


def get_session(session_id) -> Session:
    if session_id not in sessions.keys():
        session = session_manager.create_session()
        sessions[session.id] = session
    else:
        session = sessions[session_id]

    return session


def handle_conversation_request(request):
    session_id = extract_session_id(request)
    language = extract_lang(request)
    session = get_session(session_id)

    context = Context(session, language, request=request.get_json(force=True))

    for executor in action_executors:
        executor.execute(context)

    return context.response
