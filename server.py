from flask import Flask, request, json

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json
    res = {"result": data['first'] + data['second']}
    ans = json.dumps(res, indent=4)
    return ans
    
@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    res = {"result": data['first'] - data['second']}
    ans = json.dumps(res, indent=4)
    return ans

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
