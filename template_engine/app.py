from flask import Flask, render_template, flash

app = Flask(__name__, 
template_folder="views",
static_folder="public")
app.config["SECRET_KEY"] = "secret"

@app.route("/templates")
def templates():
    users = {
        "name": "Edvaldo Silva",
        "idade": 99,
        "email": "edvaldosilva4904@gmail.com"
    }

    flash("Usuario criado com sucesso!")

    return render_template("index.html", users=users)

@app.route("/users")
def users():
    flash("Users routes")

    return render_template("users.html")

if __name__ == "__main__":
    app.run(debug=True)