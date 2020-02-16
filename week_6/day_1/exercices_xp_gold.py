import datetime
import random
from flask import Flask
from flask import request
from flask import render_template
#Exercise 1
app = Flask(__name__)

@app.route('/')
def date_count_down():
    end = datetime.datetime(2021,1,1,1,1,1)
    diff = end - datetime.datetime.now()
    count_hours, rem = divmod(diff.seconds, 3600)
    count_minutes, count_seconds = divmod(rem, 60)
    time = str(diff.days) + " days " + str(count_hours) +" hours " + str(count_minutes) + " mins " + str(count_seconds) + ' seconds '
    html = render_template('exercices_xp_gold.html',time=time)
    return html

#Exercise 2
@app.route('/number',methods=['GET'])
# /number?number=10
def number():
    number = request.args.get('number')
    rnd = random.randrange(1,101)
    html = ""
    if number == rnd:
        html = 'Congrats! you have found the number '
    else:
        html = 'Too bad, maybe next time'

    return html

#Exercise 3
@app.route('/date')
def check_dates():
    todayDate = datetime.datetime.now()
    end = datetime.datetime(2020, 3, 7, 1, 1, 1)
    diff = end - datetime.datetime.now()
    count_hours, rem = divmod(diff.seconds, 3600)
    count_minutes, count_seconds = divmod(rem, 60)
    purimDate = str(diff.days) + " days " + str(count_hours) + " hours " + str(count_minutes) + " mins " + str(
        count_seconds) + ' seconds '
    html = render_template('exercices_xp_gold.html', todayDate=todayDate,purimDate=purimDate)
    return html

if __name__ == "__main__":
    app.run(debug=True)


