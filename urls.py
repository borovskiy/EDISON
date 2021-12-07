from views import app
from views import StartGame, AnswerHistory, AnswerOptions, ClearSession

app.add_url_rule('/', view_func=StartGame.as_view('index'))
app.add_url_rule('/answer', view_func=AnswerOptions.as_view('answer'))
app.add_url_rule('/history', view_func=AnswerHistory.as_view('history'))
app.add_url_rule('/clear_session', view_func=ClearSession.as_view('clear_session'))
