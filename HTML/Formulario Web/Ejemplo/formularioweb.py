from flask import Flask, request,  render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Main Page - Index"

@app.route("/form1", methods = ["GET", "POST"])
def form1():
    if request.method == "POST":
        nombre = request.form.get("txtNombre")
        email = request.form["txtEmail"]
        print(nombre)
        print(email)
        return "Datos " + email + nombre
    else: #GET
        return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=False)
