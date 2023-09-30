def extract_session_id(request):
    session_id = request.headers['BOT_SESSION_ID']

    if session_id is None:
        return ""

    return session_id

def extract_lang(request):
    language = request.headers['LANG']

    if language is None:
        return "EN"

    return language
