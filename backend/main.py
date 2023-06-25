import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
API_KEY = 'e55683ef8398f3108c7a97b154763a34'

@app.route('/api/weather', methods=['POST'])
def get_weather():
    city = request.json.get('city')

    if not city:
        return jsonify({'error': 'City parameter is required.'}), 400

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather = {
                'description': data['weather'][0]['description'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity']
            }
            return jsonify(weather)
        else:
            return jsonify({'error': data['message']}), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
