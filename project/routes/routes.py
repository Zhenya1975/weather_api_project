from flask import Blueprint, render_template, redirect, url_for, abort, request, jsonify, flash
# from models.models import SportDB, LeagueDB, TeamsDB, Match_statusDB, MatchesDB
from sqlalchemy import desc, asc
import pandas as pd
from datetime import datetime
import requests
import json
# import ssl

# ssl._create_default_https_context = ssl._create_unverified_context


from extensions import extensions

# from sqlalchemy import desc, asc, func
# from sqlalchemy import and_, or_
# from flask_socketio import SocketIO, emit
# from datetime import datetime

db = extensions.db
# db.create_all()
# db.session.commit()
home = Blueprint('home', __name__, template_folder='templates')

socketio = extensions.socketio


@home.route('/weather')
def weather():
    URL = 'https://api.open-meteo.com/v1/forecast?latitude=51.16&longitude=71.43&hourly=temperature_2m'
    request = requests.get(URL)

    weather_data_dict = request.json()
    # print(weather_data_dict.keys())
    hourly_axis_data = weather_data_dict['hourly']
    time_axis_data = hourly_axis_data['time']
    date_list_string = [date_string.split("T")[0] for date_string in time_axis_data]
    # dates_list = [datetime.strptime(date, "%Y-%m-%dT%H:%M").date() for date in time_axis_data]
    # print(date_list_string[0])
    # print(type(time_axis_data[0]))
    temperature_axis_data = hourly_axis_data['temperature_2m']
    # print(temperature_axis_data)
    # df_data = pd.DataFrame(weather_json['hourly'])
    # print(df_data)
    # df = pd.read_json(URL)
    # df.to_csv('weather.csv')
    # print(df)
    # labels = ['a', 'b', 'c']
    labels = date_list_string
    # data = [1, 2, 3]
    data = temperature_axis_data


    return render_template("weather.html", labels = labels, data=data)

@home.route('/graphwindow')
def graphwindow():

    return render_template('graph_window.html')


@home.route('/')
def home_view():
    # request = requests.get('http://api.open-notify.org')
    # people = requests.get('http://api.open-notify.org/astros.json')
    # people_json = people.json()
    # To print the number of people in space
    # print("Number of people in space:", people_json['number'])
    # To print the names of people in space using a for loop
    # for p in people_json['people']:
    #    print(p['name'])

    # parameter = {"rel_rhy": "jingle"}
    # request = requests.get('https://api.datamuse.com/words', parameter)
    # rhyme_json = request.json()
    # for i in rhyme_json[0:3]:
        # print(i['word'])

    return render_template('home.html')
    # return render_template(request.text)

@home.route('/graph_load_ajaxfile', methods=["POST", "GET"])
def graph_load_ajaxfile():
    if request.method == 'POST':

        return jsonify({'htmlresponse': render_template('graph_window.html')})
        # return redirect('/dash/')

