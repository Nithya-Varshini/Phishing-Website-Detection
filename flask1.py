from flask import Flask, request, jsonify
import requests
import json
import urllib.parse

app = Flask(__name__)

key = 'OfkP2146kTwMTTGU5h28OvhacBj6HSVV'

def malicious_url_scanner_api(url: str, vars: dict = {}) -> dict:
    url = 'https://www.ipqualityscore.com/api/json/url/%s/%s' % (key, urllib.parse.quote_plus(url))
    response = requests.get(url, params=vars)
    return json.loads(response.text)

@app.route('/detect-phishing', methods=['POST'])
def detect_phishing():
    data = request.get_json()
    url = data.get('url')
    if url:
        result = malicious_url_scanner_api(url)
        
            # You can use 'unsafe' here as needed
        print(result['phishing'])
        return jsonify(result['phishing'])
    else:
        return jsonify({'error': 'URL not provided'})

if __name__ == '__main__':
    app.run(debug=True)
