
from flask import Flask, render_template, redirect, url_for, session, request, make_response, Response
from cryptography.fernet import Fernet
import re

app = Flask(__name__, static_folder="public", static_url_path="/")
app.debug = True

app.secret_key="anytxt"

key = Fernet.generate_key()
f = Fernet(key)
pwdName = f.encrypt(b"cryptographyPWD")
pwdVal = f.encrypt(b"flask")

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/member")
def member():
  # if session["account"] == False:
  #   # return redirect("/")

  # cookie
  # account = request.cookies.get("account")
  # if not account :
  #   return redirect("/")
  # return render_template("member.html")


  # cryptography
  account = request.cookies.get(bytes(pwdName).decode("utf-8")[:-2])
  if not account:
    return redirect("/")

  remakeVal = bytes(f.decrypt(str.encode(account[2:]))).decode("utf-8")
  # print(str.encode(remakeVal) == pwdVal)
  if remakeVal == "flask" :
    return render_template("member.html")


@app.route("/signin", methods=["post"])
def sign():
  account = request.form["account"]
  password = request.form["password"]
  if account == "test" and password == "test":
    # session["account"] = account
    # return redirect("/member")

    # cookie
    # resp = make_response(redirect("/member"))
    # resp.set_cookie('account', 'flask', 7200)
    # return resp

    # cryptography
    resp = make_response(redirect("/member"))
    resp.set_cookie(pwdName, pwdVal, 7200)
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
  # resp = make_response(redirect("/"))
  # resp.set_cookie('account', '', 0)
  # return resp

  # cryptography
  resp = make_response(redirect("/"))
  resp.set_cookie(pwdName, '', 0)
  return resp


@app.route("/square/<id>")
def sqDynamic(id):
  if not bool(re.match(r"^[1-9][0-9]*$", id)):
    print(id)
    return redirect("/")
  if id.isdigit():
    num = int(id)
    result = num**2
    return render_template("square.html", result=result)

app.run(port=3000)


# def generate_key():
#     return Fernet.generate_key()


# def encrypt(key, pwd):
#     cipher_suite = Fernet(key)
#     bpwd = bytes(pwd, 'utf-8')
#     ciphered_text = cipher_suite.encrypt(bpwd)
#     return ciphered_text


# def decrypt(key, enc_pwd):
#     cipher_suite = Fernet(key)
#     uncipher_text = (cipher_suite.decrypt(enc_pwd))
#     return bytes(uncipher_text).decode("utf-8")

# key = generate_key()
# print(bytes(key).decode("utf-8"))
# encryptstr = encrypt(key, "abc123")
# print(bytes(encryptstr).decode("utf-8"))
# print(decrypt(key, encryptstr))