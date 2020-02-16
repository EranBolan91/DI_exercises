import datetime
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/<path:args>')
def birthdate(args):
    date = args.split("/")
    dateBirth = datetime.datetime(int(date[2]),int(date[1]),int(date[0]), 1, 1, 1)
    diff = datetime.datetime.now() - dateBirth
    minutes = int(diff.total_seconds()/60)
    timePass = str(minutes) +' minutes have passed'
    html = render_template('exercices_xp_ninja.html', timePass=timePass)
    return html

if __name__ == '__main__':
    app.run()