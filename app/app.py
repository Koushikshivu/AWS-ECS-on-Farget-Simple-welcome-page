from flask import Flask, request, render_template, jsonify
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    if request.method == "POST":
        name = request.form.get("name")
    return render_template("index.html", name=name)
# Health check endpoint
@app.route("/health", methods=["GET"])
def health():
    return "healthy", 200
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

