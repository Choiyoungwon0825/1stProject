from flask import Blueprint, render_template
# db import
from apps.app import db
# TABLE(workout) import
from apps.crud.models import WorkOut
from flask import Blueprint, render_template, redirect, url_for
from apps.crud.forms import WorkOutForm
# Blueprint로 crud 앱 생성
crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)

# index 엔드포인트를 작성하고 index.html 반환
@crud.route("/")
def index():
    return render_template("crud/index.html")

@crud.route("/sql")
def sql():
    db.session.query(WorkOut).all()
    return "안녕하세요~ 올리버 샘입니다~ 와~ 콘솔보소?"

@crud.route("/createWorkOut", methods=["GET","POST"])
def createWorkOut():
    # WorkOutForm을 인스턴스화 한다
    form = WorkOutForm()
    if form.validate_on_submit():
        # 운동 기록
        workout = WorkOut(
            exName = form.exName.data,
            weight = form.weight.data,
            repeat = form.repeat.data,
            setRp = form.setRp.data,
            text = form.text.data,
        )
        # 운동을 추가하고 커밋한다.
        db.session.add(workout)
        db.session.commit()
        # 운동 기록 화면으로 리다이렉트한다.
        return redirect(url_for("crud.workoutMemo"))
    return render_template("crud/createWorkOut.html", form=form)

@crud.route("/workoutMemo")
def workoutMemo():
    workout = WorkOut.query.all()
    # total = WorkOut.repeat * WorkOut.setRp * WorkOut.weight
    
    return render_template("crud/workoutMemo.html", workout=workout)

@crud.route("workoutMemo/<workout_id>", methods=["GET","POST"], endpoint="endpoint")
def editWorkOut(workout_id):
    form = WorkOutForm()

    # WorkOut 모델을 이용하여 사용자를 취득한다.
    workout = WorkOut.filter_by(id=workout_id).first()

    # form으로 부터 제출된 경우는 사용자를 갱신하여 운동 기록 화면으로 리다이렉트 한다.
    if form.validate_on_submit():
        workout.exName = form.exName.data
        workout.weight = form.weight.data
        workout.repeat = form.repeat.data
        workout.setRp = form.setRp.data
        workout.text = form.text.data
        db.session.add(workout)
        db.session.commit()
        return redirect(url_for("crud.workoutMemo"))
    
    # GET의 경우는 HTML 반환
    return render_template("crud/edit.html", workout=workout, form=form)