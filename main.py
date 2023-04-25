from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/home')
def hello_world():
    return 'Hello, World!'

@app.route('/sum/<string:n>')
def sum(n):
    
    num={
        "result":n,
        "achieved":"True"
    }
    return jsonify(num)

if __name__=="__main__":
    app.run(debug=True)