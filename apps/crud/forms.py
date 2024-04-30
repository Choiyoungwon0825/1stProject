from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired

class WorkOutForm(FlaskForm):
    check = RadioField(
        "운동종류",
        choices=[[0, "무산소운동"], [1, "유산소운동"]],
        validators=[
            DataRequired(message="운동종류")
        ]
    )
    
    exName = SelectField(
        "운동명",
        default="데드리프트",
        choices=["데드리프트","런지","레그 레이즈","레그 프레스","벤치 프레스","사이드 래터럴 레이즈","스쿼트","풀 업","푸시업",],
        validators=[
            DataRequired(message="운동명"),
        ]
    )
    weight = IntegerField(
        "중량",
        default=1,
    )
    repeat = IntegerField(
        "반복수",
        default=1,
        validators=[
            DataRequired(message="반복수"),
        ]
    )
    setRp = IntegerField(
        "세트수",
        default=1,
        validators=[
            DataRequired(message="세트수")
        ]
    )
    text = StringField(
        "특이사항",
    )
    # else :
        #  "유산소운동이당"
    
    submit = SubmitField("기록하기")
