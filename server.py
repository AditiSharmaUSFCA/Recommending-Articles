# Launch with
#
# gunicorn -D --threads 4 -b 0.0.0.0:5000 --access-logfile server.log --timeout 60 server:app glove.6B.300d.txt bbc

from flask import Flask, render_template
from doc2vec import *
import sys



app = Flask(__name__)

@app.route("/")
def articles():

    return render_template('articles.html', articles=articles[1:])

    """Show a list of article titles"""


@app.route("/article/<topic>/<filename>")
def article(topic, filename):
    fname = topic + "/" + filename
    for article in articles:
        if fname == article[0]:
            text = article[2]
            title = article[1]
            related = recommended(article, articles[1:], 5)
            return render_template('article.html', title=title, text=text, relatedArticles=related)

    """
    Show an article with relative path filename. Assumes the BBC structure of
    topic/filename.txt so our URLs follow that.
    """


# initialization
i = sys.argv.index('server:app')
glove_filename = sys.argv[i+1]
articles_dirname = sys.argv[i+2]


gloves = load_glove(glove_filename)
articles = load_articles(articles_dirname, gloves)

