# import app variable
from app import app


@app.route("/admin/dashboard")
def admin_dashboard():
    return "admin dashboard sb？"


# route 貌似能够格式化每个url
@app.route("/admin/profile")
def admin_profile():
    return "<h1 style='color: red'>啊～啊～啊～要去了～～～!!!!</h1>"
