# Importar sistema 
import os

# Carpeta DAO
import DAO.CRUDGestionDepartamento as GestionDepartamento
import DAO.CRUDGestionEmpleado as GestionEmpleado
import DAO.CRUDGestionProyecto as GestionProyecto
import DAO.CRUDGestionTiempo as GestionTiempo
import DAO.CRUDAsignacion_emp as Asignacion

# Carpeta DTO
from DTO.Departamento import Departamento
from DTO.Empleado import Empleado
from DTO.Proyecto import Proyecto
from DTO.RegistroTiempo import RegistroTiempo

# Funciones Menu
def menuPrincipal():
    os.system("cls")
    print("==========================================")
    print("        M E N U  P R I N C I P A L        ")
    print("==========================================")
    print("  1. Gestionar Empleado                   ")
    print("  2. Gestionar Departamento               ")
    print("  3. Gestionar Proyecto                   ")
    print("  4. Registro de Tiempo                   ")
    print("  5. Asignacion de Empleados a Proyectos  ")
    print("  6. Generar Informe                      ")
    print("  7. Salir                                ")
    print("==========================================")

def menuEmpleado():
    try:
        os.system("cls")
        print("==========================================")
        print("         M E N U  E M P L E A D O         ")
        print("==========================================")
        print("  1. Ingresar Datos Empleado              ")
        print("  2. Mostrar Datos Empleado               ")
        print("  3. Buscar Datos Empleado                ")
        print("  4. Modificar Datos Empleado             ")
        print("  5. Eliminar Datos Empleado              ")
        print("  6. Salir                                ")
        print("==========================================")
        
        op = input("Ingrese una opcion: ").strip()
        while True:
            if op not in ['1','2','3','4','5','6']:
                os.system("cls")
                print("==========================================")
                print("         M E N U  E M P L E A D O         ")
                print("==========================================")
                print("  1. Ingresar Datos Empleado              ")
                print("  2. Mostrar Datos Empleado               ")
                print("  3. Buscar Datos Empleado                ")
                print("  4. Modificar Datos Empleado             ")
                print("  5. Eliminar Datos Empleado              ")
                print("  6. Salir                                ")
                print("==========================================")
                op = input("Ingrese una opcion: ").strip()
            else:
                break
        if op == '1':
            ingresarDatosEmpleado()
        elif op == '2':
            mostrarDatosEmpleado()
        elif op == '3':
            mostrarDatosEmpleadoEspecifico()
        elif op == '4':
            modificarDatosEmpleado()
        elif op == '5':
            eliminarDatosEmpleado()
        elif op == '6':
            return
    except Exception as e:
        print(e)

def menuDepartamento():
    try:
        os.system("cls")
        print("==========================================")
        print("       M E N U  D E P A R T A M E N T O   ")
        print("==========================================")
        print("  1. Ingresar Datos Departamento          ")
        print("  2. Mostrar Datos Departamento           ")
        print("  3. Buscar Datos Departamento            ")
        print("  4. Modificar Datos Departamento         ")
        print("  5. Eliminar Datos Departamento          ")
        print("  6. Salir                                ")
        print("==========================================")

        op = input("Ingrese una opcion: ").strip()
        while True:
            if op not in ['1','2','3','4','5','6']:
                os.system("cls")
                print("==========================================")
                print("       M E N U  D E P A R T A M E N T O   ")
                print("==========================================")
                print("  1. Ingresar Datos Departamento          ")
                print("  2. Mostrar Datos Departamento           ")
                print("  3. Buscar Datos Departamento            ")
                print("  4. Modificar Datos Departamento         ")
                print("  5. Eliminar Datos Departamento          ")
                print("  6. Salir                                ")
                print("==========================================")
                op = input("Ingrese una opcion: ").strip()
            else:
                break
        if op == '1':
            ingresarDatosDepartamento()
        elif op == '2':
            mostrarDatosDepartamento()
        elif op == '3':
            mostrarDatosDepartamentoEspecifico()
        elif op == '4':
            modificarDatosDepartamento()
        elif op == '5':
            eliminarDatosDepartamento()
        elif op == '6':
            return
    except Exception as e:
        print(e)

def menuProyecto():
    try:
        os.system("cls")
        print("==========================================")
        print("         M E N U  P R O Y E C T O         ")
        print("==========================================")
        print("  1. Ingresar Datos Proyecto              ")
        print("  2. Mostrar Datos Proyecto               ")
        print("  3. Buscar Datos Proyecto                ")
        print("  4. Modificar Datos Proyecto             ")
        print("  5. Eliminar Datos Proyecto              ")
        print("  6. Salir                                ")
        print("==========================================")

        op = input("Ingrese una opcion: ").strip()
        while True:
            if op not in ['1','2','3','4','5','6']:
                os.system("cls")
                print("==========================================")
                print("         M E N U  P R O Y E C T O         ")
                print("==========================================")
                print("  1. Ingresar Datos Proyecto              ")
                print("  2. Mostrar Datos Proyecto               ")
                print("  3. Buscar Datos Proyecto                ")
                print("  4. Modificar Datos Proyecto             ")
                print("  5. Eliminar Datos Proyecto              ")
                print("  6. Salir                                ")
                print("==========================================")
                op = input("Ingrese una opcion: ").strip()
            else:
                break
        if op == '1':
            ingresarDatosProyecto()
        elif op == '2':
            mostrarDatosProyecto()
        elif op == '3':
            mostrarDatosProyectoEspecifico()
        elif op == '4':
            modificarDatosProyecto()
        elif op == '5':
            eliminarDatosProyecto()
        elif op == '6':
            return
    except Exception as e:
        print(e)

def menuRegistroTiempo():
    try:
        os.system("cls")
        print("==========================================")
        print("         M E N U  R E G I S T R O         ")
        print("==========================================")
        print("  1. Ingresar Datos Registro              ")
        print("  2. Mostrar Datos por empleado           ")
        print("  3. Salir                                ")
        print("==========================================")

        op = input("Ingrese una opcion: ").strip()
        while True:
            if op not in ['1','2','3']:
                os.system("cls")
                print("==========================================")
                print("         M E N U  R E G I S T R O         ")
                print("==========================================")
                print("  1. Ingresar Datos Registro              ")
                print("  2. Mostrar Datos por empleado           ")
                print("  3. Salir                                ")
                print("==========================================")
                op = input("Ingrese una opcion: ").strip()
            else:
                break
        if op == '1':
            ingresarDatosTiempo()
        elif op == '2':
            mostrarDatosTiempo()
        elif op == '3':
            return
    except Exception as e:
        print(e)

def menuAsignacion():
    try:
        os.system("cls")
        print("==========================================")
        print("         M E N U  A S I G N A C I O N     ")
        print("==========================================")
        print("  1. Asignar                              ")
        print("  2. Deasignar                            ")    
        print("  3. Mostrar por empleado                 ")
        print("  4. Salir                                ")
        print("==========================================")

        op = input("Ingrese una opcion: ").strip()
        while True:
            if op not in ['1','2','3','4']:
                os.system("cls")
                print("==========================================")
                print("         M E N U  A S I G N A C I O N     ")
                print("==========================================")
                print("  1. Asignar                              ")
                print("  2. Deasignar                            ")    
                print("  3. Mostrar por empleado                 ")
                print("  4. Salir                                ")
                print("==========================================")
                op = input("Ingrese una opcion: ").strip()
            else:
                break
        if op == '1':
            asignar()
        elif op == '2':
            desasignar()
        elif op == '3':
            mostrarPorEmpleado()
        elif op == '4':
            return
    except Exception as e:
        print(e)

#------------------------------------------------------------------------------------------------
# Funciones para el menu de Empleados

def ingresarDatosEmpleado():
    try:
        print("=== Ingresar Datos Empleado ===")
        id = input("Ingrese el ID: ").strip()
        while True:
            if not GestionEmpleado.verificarEmpleado(id):
                print("ID invalido")
                id = input("Ingrese el ID: ").strip()
            else:
                break

        nombre = input("Ingrese el nombre: ").strip().upper()
        while True:
            if not nombre.isalpha():
                print("Nombre invalido")
                nombre = input("Ingrese el nombre: ").strip().upper()
            else:
                break

        direccion = input("Ingrese la direccion: ").strip().upper()
        while True:
            if not direccion.isalpha():
                print("Direccion invalida")
                direccion = input("Ingrese la direccion: ").strip().upper()
            else:
                break

        telefono = input("Ingrese el telefono: ").strip()
        while True:
            if not telefono.isdigit():
                print("Telefono invalido")
                telefono = input("Ingrese el telefono: ").strip()
            else:
                break
        correo = input("Ingrese el correo: ").strip().lower()
        while True:
            if "@" not in correo or "." not in correo:
                print("Correo invalido")
                correo = input("Ingrese el correo: ").strip().lower()
            else:
                break

        empleado = Empleado(id, nombre, direccion, telefono, correo)
        GestionEmpleado.registrarEmpleado(empleado)
        print("Empleado registrado con exito")
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

def mostrarDatosEmpleado():
    try:
        print("=== Mostrar Datos Empleado ===")
        GestionEmpleado.mostrarEmpleado()
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------

mostrarDatosEmpleado()