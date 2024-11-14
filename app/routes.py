from flask import Blueprint, render_template, request

bp = Blueprint("main", __name__)

@bp.route("/", methods=["GET", "POST"])
def form():
    user_data = {}
    if request.method == "POST":
        user_data = {
            "name": request.form.get("name"),
            "city": request.form.get("city"),
            "hobby": request.form.get("hobby"),
            "age": request.form.get("age"),
        }
    return render_template("form.html", user_data=user_data)