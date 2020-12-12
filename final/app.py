"""
A scalable web app for listing charities, social services 
and volunteers in Portland.
"""
import flask, os
from flask.views import MethodView
from index import Index
from service import Service
from volunteer import Volunteer
from create_service import Create_service
from create_volunteer import Create_volunteer

app = flask.Flask(__name__)

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/service/',
                 view_func=Service.as_view('service'),
                 methods=["GET"])

app.add_url_rule('/service/create/',
                 view_func=Create_service.as_view('create_service'),
                 methods=['GET', 'POST'])

app.add_url_rule('/volunteer/',
                 view_func=Volunteer.as_view('volunteer'),
                 methods=["GET"])

app.add_url_rule('/volunteer/create/',
                 view_func=Create_volunteer.as_view('create_volunteer'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get('PORT',5000)))
