from flask import Flask, request,  render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Menú de página - Indice"

@app.route("/inicio", methods = ["GET", "POST"])
def inicio():
    if request.method == "POST":
        nombre = request.form.get("txtNombre")
        email = request.form["txtEmail"]
        mensaje = request.form["txtMensaje"]
        if nombre != "admin" and email != "admin@nz.com":
            sText = "MENSAJE:" + nombre + "," + email
            with open ("datos1.txt","a") as f:
                f.write(sText)
                f.write("\n")
            return render_template("form1.html")
        else:
            return "Datos " + email + nombre + mensaje
    else:
        return render_template("form1.html")
if __name__ == '__main__':
    app.run(debug=True)
