from flask import Blueprint, render_template, request, url_for
from pybo.forms import QuestionForm , AnswerForm

from pybo.models import Question

from datetime import datetime
from werkzeug.utils import redirect
from .. import db

bp = Blueprint('question',__name__,url_prefix='/')

@bp.route('/list/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html',question_list=question_list)
            #render_template(이동할페이지,전송할 데이터의 이름과,데이터)
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html',question=question, form=form)

@bp.route('/create', methods = ('GET','POST'))
def create():
    form = QuestionForm()

    #r구분을 method와 변수의 유효성 검사로 한다...
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))



    return render_template('question/question_form.html',form=form)