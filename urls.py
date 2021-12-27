from views import app
import views

app.add_url_rule('/', view_func=views.StartGame.as_view('index'))
app.add_url_rule('/answer', view_func=views.AnswerOptions.as_view('answer'))
app.add_url_rule('/history', view_func=views.AnswerHistory.as_view('history'))
app.add_url_rule('/clear_session', view_func=views.ClearSession.as_view('clear_session'))
