# Viktigt: Denna kodrad ska alltid placeras längst ner i filen.
# Detta för att säkerställa en korrekt uppstart av servern.
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """This function returns a greeting message.

    Returns:
        str: The greeting message.
    """
    return "Hello, World!"

@app.route("/new")
def new():
    """This function returns a greeting message.

    Returns:
        str: The greeting message.
    """
    return "Hello, World!"

@app



app.run(debug=True, host="0.0.0.0")
