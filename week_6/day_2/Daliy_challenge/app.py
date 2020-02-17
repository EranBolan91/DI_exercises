from flask import Flask
from flask import render_template
import feedparser

app = Flask(__name__)
rss = 'https://news.google.com/rss?x=1571747254.2933&hl=en-US&gl=US&ceid=US:en'

@app.route('/')
def home():
    items_list = getHeadLines(rss)
    print(items_list[0])
    return render_template('home.html',items_list=items_list)



def getHeadLines(rss_url):
    items = []
    feed = feedparser.parse(rss_url)
    for newItem in feed['items']:
        items.append(newItem)
    return items


if __name__ == "__main__":
    app.run(debug=True)