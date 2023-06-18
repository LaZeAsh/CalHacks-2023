from flask import Flask, request, jsonify, session
from flask_session import Session

app = Flask(__name__)
Session(app)

# Generate a schedule 
@app.route('/events/', methods=['POST'])
def generate():
    parameter = request.get_json()['parameter']
    print(parameter)

    
@app.route('/plan/', methods=['POST'])
def plan():
    time = request.get_json()['time'] 
    date = request.get_json()['date']
    location = request.get_json()['location']
    # Insert a statement here if the event is created return true otherwise false
    if True:
        return True 
    

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
