from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/order", methods=["POST"])
def order():
    name = request.form["name"]
    coffee = request.form["coffee"]
    quantity = request.form["quantity"]

    return render_template(
        "order_success.html",
        name=name,
        coffee=coffee,
        quantity=quantity
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)