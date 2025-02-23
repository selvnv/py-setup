"""Main module."""

from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def root_page():
    """Render root page.

    Returns:
        _type_: _description_
    """
    return render_template("layout.html")


def main():
    """Run app."""
    app.run(debug=True)


if __name__ == "__main__":
    """Run main."""
    main()
