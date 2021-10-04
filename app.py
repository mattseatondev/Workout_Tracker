
from flask import Flask, render_template, request, session
import datetime
app = Flask(__name__)
app.secret_key = 'speeblebeebleneeblegoodllleke'
from calendar import Calendar

@app.route('/')
def home():
    now = datetime.date.today()
    month = now.strftime('%B')
    day = (spl := str(now).split('-'))[2]
    year = spl[0]
    day_of_week = now.strftime("%A")
    cal = Calendar((month, day, year, day_of_week))
    cal.match_day_quant()
    print(cal.number_of_days())
    return render_template('home.html')