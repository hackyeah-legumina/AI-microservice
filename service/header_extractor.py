def extract_session_id(request):
    if 'BOT_SESSION_ID' not in request.headers.keys():
        return ""

    return request.headers['BOT_SESSION_ID']


def extract_lang(request):
    if 'LANG' not in request.headers.keys():
        return "PL"

    return request.headers['LANG']
