import mysql.connector

def conectar_base_datos():
    """
    1
    """
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='user_ramiro_espana',
            password='AbcdeUdeC',
            database='bd_ramiro_espana_ejercicio11'
        )
        cursor = conexion.cursor()
        return conexion, cursor
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None, None

def agregar_registro(tabla, datos):
    """Agrega un nuevo registro a la tabla especificada."""
    conexion, cursor = conectar_base_datos()
    if conexion:
        placeholders = ', '.join(['%s'] * len(datos))
        columnas = ', '.join(datos.keys())
        consulta = f"INSERT INTO {tabla} ({columnas}) VALUES ({placeholders})"
        try:
            cursor.execute(consulta, tuple(datos.values()))
            conexion.commit()
            print("Registro agregado correctamente.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conexion.close()

def mostrar_registros(tabla):
    """Muestra todos los registros de la tabla especificada."""
    conexion, cursor = conectar_base_datos()
    if conexion:
        consulta = f"SELECT * FROM {tabla}"
        try:
            cursor.execute(consulta)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conexion.close()

def actualizar_registro(tabla, id_registro, actualizaciones):
    """Actualiza un registro existente en la tabla especificada."""
    conexion, cursor = conectar_base_datos()
    if conexion:
        set_clause = ', '.join([f"{columna} = %s" for columna in actualizaciones.keys()])
        consulta = f"UPDATE {tabla} SET {set_clause} WHERE id = %s"
        try:
            cursor.execute(consulta, tuple(actualizaciones.values()) + (id_registro,))
            conexion.commit()
            print("Registro actualizado correctamente.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conexion.close()

def eliminar_registro(tabla, id_registro):
    """Elimina un registro de la tabla especificada."""
    conexion, cursor = conectar_base_datos()
    if conexion:
        consulta = f"DELETE FROM {tabla} WHERE id = %s"
        try:
            cursor.execute(consulta, (id_registro,))
            conexion.commit()
            print("Registro eliminado correctamente.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conexion.close()

def consulta_avanzada(consulta, parametros=None):
    """Ejecuta una consulta personalizada con parámetros opcionales."""
    conexion, cursor = conectar_base_datos()
    if conexion:
        try:
            cursor.execute(consulta, parametros)
            resultados = cursor.fetchall()
            for resultado in resultados:
                print(resultado)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conexion.close()

def main():
    """Programa principal para interactuar con la base de datos."""
    while True:
        print("\nOperaciones con la Base de Datos:")
        print("1. Agregar Registro")
        print("2. Mostrar Registros")
        print("3. Actualizar Registro")
        print("4. Eliminar Registro")
        print("5. Consulta Personalizada")
        print("6. Salir")
        opcion = input("Ingresa tu opción: ")

        if opcion == '1':
            tabla = input("Ingresa el nombre de la tabla: ")
            datos = {}
            while True:
                columna = input("Ingresa el nombre de la columna (o escribe 'hecho' para terminar): ")
                if columna.lower() == 'hecho':
                    break
                valor = input(f"Ingresa el valor para {columna}: ")
                datos[columna] = valor
            agregar_registro(tabla, datos)
        elif opcion == '2':
            tabla = input("Ingresa el nombre de la tabla: ")
            mostrar_registros(tabla)
        elif opcion == '3':
            tabla = input("Ingresa el nombre de la tabla: ")
            id_registro = int(input("Ingresa el ID del registro a actualizar: "))
            actualizaciones = {}
            while True:
                columna = input("Ingresa el nombre de la columna a actualizar (o escribe 'hecho' para terminar): ")
                if columna.lower() == 'hecho':
                    break
                valor = input(f"Ingresa el nuevo valor para {columna}: ")
                actualizaciones[columna] = valor
            actualizar_registro(tabla, id_registro, actualizaciones)
        elif opcion == '4':
            tabla = input("Ingresa el nombre de la tabla: ")
            id_registro = int(input("Ingresa el ID del registro a eliminar: "))
            eliminar_registro(tabla, id_registro)
        elif opcion == '5':
            consulta = input("Ingresa tu consulta personalizada: ")
            parametros = input("Ingresa los parámetros de la consulta (separados por comas) o presiona Enter: ")
            if parametros:
                parametros = tuple(parametros.split(','))
            else:
                parametros = None
            consulta_avanzada(consulta, parametros)
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
