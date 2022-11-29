from flask_cors import CORS
from flask import Flask, request



app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/data', methods=["POST"])
def postExplainToCache():
    jsonData = request.json
    sentence = jsonData["sentences"]
    print("👉"+sentence)
    response ="[[[[[" + sentence + "]]]]]" 
    return{"response": response}



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="86")