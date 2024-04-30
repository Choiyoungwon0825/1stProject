# import flask class
from flask import (Flask,
                    render_template,
                    url_for,
                    request,
                    redirect,
                    flash)
import datetime as dt
import logging
from flask_debugtoolbar import DebugToolbarExtension


# flask class instance
app = Flask(__name__)
# 세션 정보 보호를 위한 SECRET_KEY 추가
app.config["SECRET_KEY"] = "healthprojectkey"
# 로그 레벨을 설정한다.
app.logger.setLevel(logging.DEBUG)
# 리다이렉트를 중단하지 않도록 한다
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
# DebugToolbarExtension에 애플리케이션을 설정한다
toolbar = DebugToolbarExtension(app)

req = request
date = dt.datetime.now()
print('===========FLASK 1st Project===========')
print(date)
print('=======================================')

# URL & run 
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello/<name>",
           methods=["GET","POST"],
           endpoint="hello-endpoint")
def hello(name):
    return render_template("index.html", name=name)

@app.route("/health")
def health():
    return render_template("health.html")

@app.route("/healthComplete", methods=["GET","POST"])
def healthComplete():
    if req.method == "POST": 
        # form 속성을 사용하여 form값 취득
        exName = req.form["exName"]
        setRp = req.form["setRp"]
        weight = req.form["weight"]
        repeat = req.form["repeat"]

        # 입력 체크
        is_vaild = True
        if not exName:
            flash("운동종류 선택은 필수입니다!")
            is_vaild=False

        if not setRp:
            flash("세트 수 선택은 필수입니다!")
            is_vaild=False

        if not weight:
            flash("중량 입력은 필수입니다!")
            is_vaild=False

        if not repeat:
            flash("반복 수 입력은 필수입니다!")
            is_vaild=False
        
        if not is_vaild:
            return redirect(url_for("health"))


        print(exName, setRp, weight, repeat)
        print(type(setRp),type(weight),type(repeat))

        flash("기록 완료")
        return redirect(url_for("healthComplete", exName=exName, setRp=setRp, weight=weight, repeat=repeat))
    exName = req.args.get("exName")
    setRp = req.args.get("setRp")
    weight = req.args.get("weight")
    repeat = req.args.get("repeat")
    total = int(setRp) * int(weight) * int(repeat)

    print(exName,setRp,weight,repeat)
    print(total)
   
    return render_template("healthComplete.html",exName=exName, setRp=setRp, weight=weight, repeat=repeat, total=total, date=date)

@app.route("/history")
def history():
    return render_template("history.html")
