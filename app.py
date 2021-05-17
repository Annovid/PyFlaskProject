"""
Main file
"""
from flask import Flask, request, redirect, render_template
import parsing

app = Flask(__name__)


@app.route('/find/<read>', methods=["POST", "GET"])
def find(read) -> None:
    """
    This function parses the KinoPoisk content and renders the page
    """
    films = parsing.parsing(read)
    if len(films) == 0:
        return render_template('not_found.html')
    return render_template('films.html', count=len(films), arr=films)


@app.route('/', methods=["POST", "GET"])
def index() -> None:
    """
    The initializer function
    """
    if request.method == "POST":
        read = request.form.get('read')
        return redirect("/find/{}".format(read))
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
