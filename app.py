from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]

        return f"""
        <h2>Login Details Received</h2>
        <p>Email: {email}</p>
        <p>Role: {role}</p>
        """

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)