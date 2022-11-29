from flask_cors import CORS
from flask import Flask, request, make_response, jsonify
from flask_cors import cross_origin



app = Flask(__name__)
#CORS(app, resources=r'/*')
CORS(app, resources={r"/.*": {"origins": ["http://127.0.0.1","https://yuenci.github.io/"]}}, supports_credentials=True) 
#CORS(app, supports_credentials=True)

@app.route('/data', methods=["POST"])
def postExplainToCache():
    jsonData = request.json
    sentence = jsonData["sentences"]
    print("👉"+sentence)
    response ="[[[[[" + sentence + "]]]]]" 
    return{"response": response}


# @app.after_request
# def after(resp):
#     resp = make_response(resp)
#     resp.headers['Access-Control-Allow-Origin'] = '*'
#     resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
#     resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
#     return resp


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="86")