from flask import Flask, request

app = Flask(__name__)

global competences 
competences = [ 'intelligence', 'gentil', 'genereux, enfin a moitie' ]

@app.route("/")
def hello():
    return { "message": "Hello Sebastien, ceci est une demo faite pour stacklabs" }

@app.route("/moi")
def me():
    return {
            "nom": "nguyen",
            "prenom": "jean-michel",
            "age": 40,
            "competences" : competences
            }

@app.route("/competences", methods=['GET', 'POST'])
def my_competences():
   if request.method == "GET":
           return { "competences" : competences }
   if request.method == "POST":
       new_competence = request.get_json(force=True).get('competence')
       if new_competence is None:
           return { "message": "attribute could not be handle" }, 400
       else:
           competences.append(new_competence)
           return { "competences" : competences }

@app.route("/competences/<competence>", methods=['DELETE'])
def remove_competence(competence):
   if request.method == "DELETE":
       if competence is None:
           return { "message": "attribute could not be handle" }, 400
       else:
           try: 
               competences.remove(competence)
           except ValueError as e:
               return { "message": "could not remove the competence" }
           return { "competences" : competences }
