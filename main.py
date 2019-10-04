from flask import Flask, jsonify, request
from flask_cors import CORS
from user import USER
from events import EVENTS
app = Flask(__name__)
CORS(app)
U = USER()
E = EVENTS()
@app.route("/register", methods=["POST"])						
def register():
	payload = request.json
	if U.search(payload['uid'])==True:
		return jsonify({'success':False})
	else:
		U.insert(payload)
		return jsonify({'success':True})

@app.route("/login",methods=["POST"])
def login():
	payload = request.json
	print(payload)
	if U.search(payload['id'])==True and U.pwd(payload['id'])==payload['passwd'] :
		return jsonify({'success':True})
	else:
		return jsonify({'success':False})

@app.route("/addevent",methods=["POST"])
def add_event():
	payload = request.json
	E.insert(payload)
	return jsonify({'success':True})

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")




