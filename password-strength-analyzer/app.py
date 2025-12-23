from flask import Flask, render_template, request, send_file
from analyzer.strength import analyze_password
from analyzer.wordlist import generate_wordlist
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    preview = None
    active_tab = "analyzer"   # default tab

    if request.method == "POST":
        action = request.form.get("action")

        if action == "analyze":
            password = request.form.get("password")
            result = analyze_password(password)
            active_tab = "analyzer"

        elif action == "preview":
            data = {
                "name": request.form.get("name"),
                "nickname": request.form.get("nickname"),
                "pet": request.form.get("pet"),
                "year": request.form.get("year"),
                "favorite": request.form.get("favorite"),
            }
            preview = generate_wordlist(data)[:20]
            active_tab = "generator"

        elif action == "download":
            data = {
                "name": request.form.get("name"),
                "nickname": request.form.get("nickname"),
                "pet": request.form.get("pet"),
                "year": request.form.get("year"),
                "favorite": request.form.get("favorite"),
            }
            words = generate_wordlist(data)
            content = "\n".join(words)

            return send_file(
                io.BytesIO(content.encode()),
                mimetype="text/plain",
                as_attachment=True,
                download_name="custom_wordlist.txt"
            )

    return render_template(
        "index.html",
        result=result,
        preview=preview,
        active_tab=active_tab
    )


if __name__ == "__main__":
    app.run(debug=True)
