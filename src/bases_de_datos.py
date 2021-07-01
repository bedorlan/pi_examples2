import mysql.connector
cnn = mysql.connector.connect(host = "localhost", 
                              user = "pilar", 
                              passwd = "pilar", 
                              database = "database1")


def consultar_personas(): 
    cur = cnn.cursor() 
    cur.execute("select * from personas") 
    datos = cur.fetchall()
     
    
    for fila in datos: 
        print(fila)
        
        
        
        
        
def insertar_nueva_persona(nombre, cedula, telefono):
    cur = cnn.cursor() 
    sql = """insert into personas (nombre,cedula,telefono)
        values (%s, %s, %s)"""
    datos = (nombre, cedula, telefono)
    cur.execute(sql, datos) 
    cnn.commit()
    
      
    
     
def crear_menu():
    while True:
        
        menu = int(input("Usted tiene el siguiente menu \n1 para agrepar persona \n2 para mostrar personas \n0 para salir \nEscriba una opcion: "))
        
        if menu == 1:
            nombre = input("Ingrese el nombre de la persona:")
            cedula = input("Ingrese la cedula: ")
            telefono = input("Ingrese el telefono: ")
            insertar_nueva_persona(nombre, cedula, telefono)
            print("Se ha agregado los cambios exitosamente" )
            
        if menu == 2:
            consultar_personas()
            
        if menu == 0:
            break

crear_menu()
