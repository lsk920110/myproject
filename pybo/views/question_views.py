from flask import Blueprint, render_template
from pybo.forms import QuestionForm

from pybo.models import Question

bp = Blueprint('question',__name__,url_prefix='/')

@bp.route('/list/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html',question_list=question_list)
            #render_template(이동할페이지,전송할 데이터의 이름과,데이터)
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html',question=question)

@bp.route('/create')
def create():
    form = QuestionForm()
    return render_template('question/question_form.html',form=form)