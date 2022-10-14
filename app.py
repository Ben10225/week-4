
from flask import Flask, render_template, redirect, session, request, make_response, Response
import re

app = Flask(__name__, static_folder="public", static_url_path="/")
# app.debug = True

app.secret_key="anytxt"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/member")
def member():
  # if session["account"] == False:
  #   # return redirect("/")

  # cookie
  account = request.cookies.get("account")
  if not account :
    return redirect("/")

  return render_template("member.html")

@app.route("/signin", methods=["post"])
def sign():
  account = request.form["account"]
  password = request.form["password"]
  if account == "test" and password == "test":
    # session["account"] = account
    # return redirect("/member")

    # cookie
    resp = make_response(redirect("/member"))
    resp.set_cookie('account', 'flask', 7200)
    return resp

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
  # session['account'] = False
  # return redirect("/")

  # cookie
  resp = make_response(redirect("/"))
  resp.set_cookie('account', '', 0)
  return resp


@app.route("/square/<id>")
def sqDynamic(id):
  if not bool(re.match(r"^[1-9][0-9]*$", id)):
    print(id)
    return redirect("/")
  if id.isdigit():
    num = int(id)
    result = num**2
    print(result)
    return render_template("square.html", result=result)


app.run(port=3000)