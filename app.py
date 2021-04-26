from flask import Flask, send_file
import datetime
app = Flask(__name__)

@app.errorhandler(404)
def home(e):
    return 'Utiliza /p/a21xxxxxx com o teu numero de aluno para marcar presença'

@app.route('/p/<id>', methods=["GET"])
def marcarpresenca(id):
    x = datetime.datetime.now()
    filename = str("p/" + datetime.datetime.now().strftime("%d-%m-%Y") + ".txt")

    f = open(filename, "a")
    f.write(str(id + ";" + datetime.datetime.now().strftime("%H:%M")) + "\n")
    f.close()

    return "Presença marcada para " + id

@app.route('/f/<date>')
def getpresenca(date):
        return send_file("p/" + date + ".txt", as_attachment=True)

if __name__ == "__main__":
        app.run()