from flask import Flask,render_template,request
import json
import urllib.request

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        #for default name
        city = 'chennai'

    API_KEY = 'API KEY'  # initialize your key here

    # source contain json data from api
    source = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}').read()

    # converting json data to dictionary
    list_of_data = json.loads(source)
    print(list_of_data)
    # data for variable list_of_data
    data = {
        "name":str(list_of_data['name']),
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'k',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
    }
    return render_template('index.html',data=data)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
