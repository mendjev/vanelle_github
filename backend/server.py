from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")

def hello_world():  
    return "<p>Hello, World!</p>"

def hello_world1():  
    return "<p>Hello, Ceci est un compteur avec la liste des routes disponibles!</p>"

compteur=0
@app.route("/cpt")
def afficher_compteur():
    return jsonify({
        "compteur":compteur,
        "message":f"La valeur actuelle du compteur est {compteur}"

    })

@app.route("/incr")
def incrementer():

    global compteur
    compteur += 1

    return jsonify({
        "compteur":compteur,
        "action":"incrémentation",
        "message":f"Compteur incrémenté ! Nouvelle valeur :{compteur}"
    })

@app.route("/decr")
def decrementer():

    global compteur
    compteur -= 1

    return jsonify({
        "compteur":compteur,
        "action":"décrémentation",
        "message":f"Compteur décrémenté ! Nouvelle valeur :{compteur}"
    })

if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1',port=5000)