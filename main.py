from flask import Flask, jsonify, request
from flask_cors import CORS
from user import USER
from events import EVENTS
from payment import PAYMENT
from rec_eve import RECIEPT_EVENT
from eve_use import EVENT_USER
app = Flask(__name__)
CORS(app)
U = USER()
E = EVENTS()
P = PAYMENT()
R_E = RECIEPT_EVENT()
E_U = EVENT_USER()
Uid = None
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
		Uid=payload['id']
		print(Uid)
		return jsonify({'success':True})
	else:
		return jsonify({'success':False})
        
@app.route("/userhome",methods=["GET"])
def userhome():
	print(Uid)
	e = E_U.getevents(Uid)	
	all_events = E.getevents(e)
	return jsonify({'events':allevents, 'success':True,'uid':Uid})
    
@app.route("/delete-event",methods=["POST"])
def delete_event():
    payload = request.json 
    id = payload["id"]
    E.delete(id)
    rid = R_E.delete(id)
    E_U.delete(id)
    P.delete(rid)
    return jsonify({'success':True})
    
@app.route("/addevent",methods=["POST"])
def add_event():
    payload = request.json
    eid = E.size()+1
    if E.check_date(payload['e_date']) == True:
        return jsonify({'success':False})
    E.insert(payload,eid)
    E_U.insert(eid,payload['uid'])
    rid = P.size()+1
    P.insert(rid,1000)
    R_E.insert(rid,eid)
    return jsonify({'success': True})
    
if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")
