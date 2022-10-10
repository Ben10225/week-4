from flask import Flask, render_template, redirect, request, session, url_for

app = Flask(__name__, static_folder="public", static_url_path="/")

app.secret_key="anytxt"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/member")
def member():
  if session["account"] == False:
    return redirect("/")
  return render_template("member.html")

@app.route("/signin", methods=["post"])
def sign():
  account = request.form["account"]
  password = request.form["password"]
  if account == "test" and password == "test":
    session["account"] = account
    return redirect("/member")
  else:
    if account == "" or password == "":
      return redirect("/error?message=請輸入帳號、密碼")
    return redirect("/error?message=帳號、密碼輸入錯誤")

@app.route("/error")
def fail():
  err = request.args.get("message", "輸入錯誤")
  return render_template("error.html", message=err)

@app.route("/signout")
def signout():
  session['account'] = False
  return redirect("/")

@app.route("/square", methods=["post"])
def square():
  numinput = request.form["count"]
  if numinput == "0": 
    return redirect("/")
  if numinput == "" or numinput.isdigit() == False:
    return redirect("/")
  return redirect(url_for("sqDynamic", id=numinput))

@app.route("/square/<id>")
def sqDynamic(id):
  if id.isdigit():
    num = int(id)
    result = num**2
    return render_template("square.html", result=result)

app.run(port=3000)