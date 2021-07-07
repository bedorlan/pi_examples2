from flask import Flask, Response
import json
import mysql.connector


cnn = mysql.connector.connect(host = "localhost", 
                              user = "pilar", 
                              passwd = "pilar", 
                              database = "database1")



def consultar_personas(): 
    cur = cnn.cursor() 
    cur.execute("select * from personas") 
    datos = cur.fetchall()
     
    archivo = []
    for fila in datos:
        lista = []
        for i in fila:
            lista.append(i)
        archivo.append(lista)
    return(archivo)
        
       

def convertir_a_diccionario(archivo): 
    
    lista = []
    for i in archivo:
        diccionario = {}  
        diccionario["nombre"] = i[0]
        diccionario["cedula"] = i[1]
        diccionario["telefono"] = i[2]
        lista.append(diccionario)
        
    return lista
        
     

app = Flask(__name__)

@app.route("/")
def Index():
    return "{}"

@app.route("/persons")
def persons():
    archivo = convertir_a_diccionario(consultar_personas())
    return Response(json.dumps(archivo), mimetype='application/json')
    


@app.route("/api2")
def Api2():
    dict1 = {"prop1": "pilar", "prop2": "orlando"}
    return Response(json.dumps(dict1), mimetype='application/json')

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=3000, debug= True)
    