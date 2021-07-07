from flask import Flask, Response
import json
import mysql.connector

cnn = mysql.connector.connect(host="localhost",
                              user="pilar",
                              passwd="pilar",
                              database="database1")


def query_people():
    cur = cnn.cursor()
    cur.execute("select * from personas")
    data = cur.fetchall()

    file = []
    for row in data:
        list = []
        for i in row:
            list.append(i)
        file.append(list)
    return(file)


def convert_to_dictionary(file):

    list = []
    for i in file:
        dictionary = {}
        dictionary["nombre"] = i[0]
        dictionary["cedula"] = i[1]
        dictionary["telefono"] = i[2]
        list.append(dictionary)

    return list


app = Flask(__name__)


@app.route("/")
def Index():
    return "{}"


@app.route("/persons")
def persons():
    file = convert_to_dictionary(query_people())
    return Response(json.dumps(file), mimetype='application/json')


@app.route("/api2")
def Api2():
    dict1 = {"prop1": "pilar", "prop2": "orlando"}
    return Response(json.dumps(dict1), mimetype='application/json')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
