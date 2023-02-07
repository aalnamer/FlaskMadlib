"""Madlibs Stories."""
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = 'for'
debug = DebugToolbarExtension(app)

@app.route("/")
def home_page():
    return render_template("home.html")
    
@app.route("/madlibs")
def madlibs():
    prompts = story.prompts
    return render_template("madlibs.html", prompts = prompts)
    
@app.route("/story")
def show_story():
        text = story.generate(request.args)
        return render_template("story.html", text = text)



class Story:
    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
