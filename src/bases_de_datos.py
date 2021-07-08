import mysql.connector
cnn = mysql.connector.connect(host="localhost",
                              user="pilar",
                              passwd="pilar",
                              database="database1")


def query_person():
    cur = cnn.cursor()
    cur.execute("select * from personas")
    data = cur.fetchall()

    for row in data:
        print(row)


def insert_new_person(nombre, cedula, telefono):
    cur = cnn.cursor()
    sql = """insert into personas (nombre,cedula,telefono)   
    values (%s, %s, %s)"""
    data = (nombre, cedula, telefono)
    cur.execute(sql, data)
    cnn.commit()


def insert_donations(cedula, valor, fecha):
    cur = cnn.cursor()
    sql = """insert into donaciones (cedula,valor,fecha)
        values (%s, %s, %s)"""
    data = (cedula, valor, fecha)
    cur.execute(sql, data)
    cnn.commit()


def query_donations():
    cur = cnn.cursor()
    cur.execute(
        """select personas.nombre, personas.cedula, sum(donaciones.valor) total_donaciones 
        from personas, donaciones 
        where personas.cedula = donaciones.cedula 
        group by personas.cedula, personas.nombre"""
    )
    data = cur.fetchall()
    for row in data:
        print(row)


def create_menu():
    while True:

        menu = int(input("""Usted tiene el siguiente menu 
                         1 para agregar persona 
                         2 para mostrar personas 
                         3 para agregar registro de donacion
                         4 para consultar registro de donaciones
                         0 para salir 
                         Escriba una opcion: """))

        if menu == 1:
            nombre = input("Ingrese el nombre de la persona:")
            cedula = input("Ingrese la cedula: ")
            telefono = input("Ingrese el telefono: ")
            try:
                insert_new_person(nombre, cedula, telefono)
                print("Se ha agregado los cambios exitosamente")

            except:
                print("Oops!  El valor esta duplicado.  intente de nuevo...")
                break

        if menu == 2:
            query_person()

        if menu == 3:
            cedula = input("Ingrese la cedula: ")
            valor = int(input("Ingrese el valor de la donacion: "))
            fecha = input("Ingrese la fecha de la donacion A/M/D: ")
            try:
                insert_donations(cedula, valor, fecha)
                print("Se ha agregado los cambios exitosamente")

            except:
                print("Oops!  La cedula no esta registrada.  intente de nuevo...")
                break

        if menu == 4:
            query_donations()

        if menu == 0:
            break


create_menu()
