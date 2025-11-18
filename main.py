# Importar sistema 
import os
from datetime import datetime
import re
from getpass import getpass
import json, requests

# Carpeta DAO
import DAO.CRUDGestionDepartamento as GestionDepartamento
import DAO.CRUDGestionEmpleado as GestionEmpleado
import DAO.CRUDGestionProyecto as GestionProyecto
import DAO.CRUDGestionTiempo as GestionTiempo
import DAO.CRUDAsignacion_emp as Asignacion_emp
import DAO.CRUDUsuario as GestionUsuario
import DAO.CRUDIndicador as GestionIndicador

# Carpeta DTO
from DTO.Departamento import Departamento
from DTO.Empleado import Empleado
from DTO.Proyecto import Proyecto
from DTO.RegistroTiempo import RegistroTiempo
from DTO.Usuario import Usuario
from DTO.IndicadorEconomico import IndicadorEconomico

# Funciones Menu
def menuPrincipal(tipo_usuario):
    os.system("clear")
    print("==========================================")
    print("        M E N U  P R I N C I P A L        ")
    print("==========================================")
    if tipo_usuario == "Administrador":
        print("  1. Gestionar Empleado                   ")
        print("  2. Gestionar Departamento               ")
        print("  3. Gestionar Proyecto                   ")
        print("  4. Registro de Tiempo                   ")
        print("  5. Asignacion de Empleados a Proyectos  ")
        print("  6. Indicador Economico                  ")
        print("  7. Generar Informe                      ")
        print("  8. Salir                                ")
        print("==========================================")
    else:
        print("  1. Idicador Economico                   ")
        print("  2. Registro tiempo                      ")
        print("  3. Salir                                ")
        print("==========================================")

def menuEmpleado():
    try:
        os.system("clear")
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
                os.system("clear")
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
            mostrarDatoEmpleadoEspecifico()
        elif op == '4':
            modificarEmpleado()
        elif op == '5':
            eliminarEmpleado()
        elif op == '6':
            return
    except Exception as e:
        print(e)

def menuDepartamento():
    try:
        os.system("clear")
        print("==========================================")
        print("     M E N U  D E P A R T A M E N T O     ")
        print("==========================================")
        print("  1. Ingresar Datos Departamento          ")
        print("  2. Mostrar Datos Departamento           ")
        print("  3. Modificar Datos Departamento         ")
        print("  4. Eliminar Datos Departamento          ")
        print("  5. Salir                                ")
        print("==========================================")

        op = input("Ingrese una opcion: ").strip()
        while True:
            if op not in ['1','2','3','4','5','6']:
                os.system("clear")
                print("==========================================")
                print("     M E N U  D E P A R T A M E N T O     ")
                print("==========================================")
                print("  1. Ingresar Datos Departamento          ")
                print("  2. Mostrar Datos Departamento           ")
                print("  3. Modificar Datos Departamento         ")
                print("  4. Eliminar Datos Departamento          ")
                print("  5. Salir                                ")
                print("==========================================")
                op = input("Ingrese una opcion: ").strip()
            else:
                break
        if op == '1':
            ingresarDatosDepartamento()
        elif op == '2':
            mostrarDatosDepartamento()
        elif op == '3':
            modificarDatosDepartamento()
        elif op == '4':
            eliminarDatosDepartamento()
        elif op == '5':
            return
    except Exception as e:
        print(e)

def menuProyecto():
    try:
        os.system("clear")
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
            if op not in ['1','2','3','4','5','6','7']:
                os.system("clear")
                print("==========================================")
                print("         M E N U  P R O Y E C T O         ")
                print("==========================================")
                print("  1. Ingresar Datos Proyecto              ")
                print("  2. Mostrar Datos Proyecto               ")
                print("  3. Modificar Datos Proyecto             ")
                print("  4. Eliminar Datos Proyecto              ")
                print("  5. Salir                                ")
                print("==========================================")
                op = input("Ingrese una opcion: ").strip()
            else:
                break
        if op == '1':
            ingresarDatosProyecto()
        elif op == '2':
            mostrarDatosProyecto()
        elif op == '3':
            modificarDatosProyecto()
        elif op == '4':
            eliminarDatosProyecto()
        elif op == '5':
            return
    except Exception as e:
        print(e)

def menuRegistroTiempo():
    try:
        os.system("clear")
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
                os.system("clear")
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
        os.system("clear")
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
                os.system("clear")
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

def menuUsuario():
    os.system("clear")
    print("==========================================")
    print("         M E N U  U S U A R I O           ")
    print("==========================================")
    print("  1. Ingresar Usuario                     ")
    print("  2. Iniciar sesion                       ")
    print("  3. Salir                                ")
    print("==========================================")

def menuIndicador(tipo_usuario):
    os.system("clear")
    print("==========================================")
    print("       M E N U  I N D I C A D O R         ")
    print("==========================================")
    if tipo_usuario == "Administrador":
        print("  1. Indicador Economico                  ")
        print("  2. Mostrar Indicadores                  ")
        print("  3. Eliminar Indicador                   ")
        print("  4. Salir                                ")
        print("==========================================")
        opm = input("Ingrese una opcion: ").strip()
        while True:
            if opm not in ['1','2','3','4']:
                os.system("clear")
                print("==========================================")
                print("       M E N U  I N D I C A D O R         ")
                print("==========================================")
                print("  1. Indicador Economico                  ")
                print("  2. Mostrar Indicadores                  ")
                print("  3. Eliminar Indicador                   ")
                print("  4. Salir                                ")
                print("==========================================")
                opm = input("Ingrese una opcion: ").strip()
            else:
                break
        if opm == '1':
            consultaIndicadores()
        elif opm == '2':
            mostrarIndicadores()
        elif opm == '3':
            eliminarIndicador()
        elif opm == '4':
            return
    else:
        print("  1. Indicador Economico                  ")
        print("  2. Mostrar Indicadores                  ")
        print("  3. Salir                                ")
        print("==========================================")
        opm = input("Ingrese una opcion: ").strip()
        while True:
            if opm not in ['1','2','3']:
                os.system("clear")
                print("==========================================")
                print("       M E N U  I N D I C A D O R         ")
                print("==========================================")
                print("  1. Indicador Economico                  ")
                print("  2. Mostrar Indicadores                  ")
                print("  3. Salir                                ")
                print("==========================================")
                opm = input("Ingrese una opcion: ").strip()
            else:
                break
        if opm == '1':
            consultaIndicadores()
        elif opm == '2':
            mostrarIndicadores()
        elif opm == '3':
            return
#------------------------------------------------------------------------------------------------
# Funciones para el menu de Empleados

def ingresarDatosEmpleado():
    try:
        print("=== Ingresar Datos Empleado ===")
        run = input("Ingrese el run: ").strip()
        while True:
            if not run.isdigit():
                print("Run invalido")
                run = input("Ingrese el run: ").strip()
            else:
                break
        
        nombre = input("Ingrese el nombre: ").strip().capitalize()
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

        fecha_inicio = input("Ingrese la fecha de contrato (aaaa-mm-dd): ").strip()
        while True:
            fecha = input("Ingrese la fecha de contrato (aaaa-mm-dd): ").strip()
            if not fecha:
                fecha = datetime.now().strftime("%Y-%m-%d")
            elif not re.match(r'^\d{4}-\d{2}-\d{2}$', fecha):
                print("Fecha de inicio invalida")
                fecha = input("Ingrese la fecha de contrato (aaaa-mm-dd): ").strip()
            else:
                break
                
        salario = input("Ingrese el salario: ").strip()
        while True:
            if not salario.isdigit():
                print("Salario invalido")
                salario = input("Ingrese el salario: ").strip()
            else:
                break

        print("\n=== Departamento Disponibles ===")
        datos = GestionDepartamento.mostrarTodo()
        if not datos:
            print("No hay departamentos disponibles")
            input("Presione enter para continuar")
            return
        for d in datos:
            print(f"Id: {d[0]} | Nombre: {d[1]}")
        departamento_id = input("\nIngrese el id del departamento: ").strip()
        while True:
            if not departamento_id.isdigit():
                print("Id de departamento invalido")
                departamento_id = input("Ingrese el id del departamento: ").strip()
            elif not GestionDepartamento.verificarDepartamento(departamento_id):
                print("Departamento no encontrado")
                departamento_id = input("Ingrese el id del departamento: ").strip()
            else:
                break

        empleado = Empleado(run, nombre, direccion, telefono, correo, fecha_inicio, salario, departamento_id)
        GestionEmpleado.agregar(empleado)
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

def mostrarDatosEmpleado():
    try:
        print("=== Mostrar Datos Empleado ===")
        datos = GestionEmpleado.mostrarTodos()
        if not datos:
            print("No hay empleados para mostrar")
            input("\nPresione enter para continuar")
            return
        for d in datos:
            print(f"User_id: {d[0]} | Run: {d[1]} | Nombre: {d[2]} | Direccion: {d[3]} | Telefono: {d[4]} | Correo: {d[5]} | Fecha inicio: {d[6]} | Salario: {d[7]} | Dept: {d[8]}\n----------------------------")
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

def mostrarDatoEmpleadoEspecifico():
    try:
        print("=== Mostrar Datos Empleado Especifico ===")
        EmpleadoData = GestionEmpleado.mostrarTodos()
        if not EmpleadoData:
            print("No hay empleados para mostrar")
            input("\nPresione enter para continuar")
            return
        for d in EmpleadoData:
            print(f"User_id: {d[0]} | Nombre : {d[2]}")
        ide = int(input("Ingrese el id del empleado: ").strip())
        d = GestionEmpleado.buscarEmpleado(ide)
        while True:
            if not d:
                print("Empleado no existe")
                ide = int(input("Ingrese el id del empleado: ").strip())
                d = GestionEmpleado.buscarEmpleado(ide)
            else:
                break
        print(f"User_id: {d[0]} | Run: {d[1]} | Nombre: {d[2]} | Direccion: {d[3]} | Telefono: {d[4]} | Correo: {d[5]} | Fecha inicio: {d[6]} | Salario: {d[7]} | Dept: {d[8]}")
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

def mostrarDatoEmpleadoParcial():
    try:
        print("=== Mostrar Datos Empleado Parcial ===")
        datos = GestionEmpleado.mostrarTodos()
        if not datos:
            print("No hay empleados para mostrar")
            input("\nPresione enter para continuar")
            return
        num = input("Ingrese la cantidad a mostrar: ").strip()
        while True:
            if not num.isdigit():
                print("Cantidad invalida")
                num = input("Ingrese la cantidad a mostrar").strip()
            else:
                break
        datos = GestionEmpleado.cosultaParcial(int(num))
        for d in datos:
            print(f"User_id: {d[0]} | Run: {d[1]} | Nombre: {d[2]} | Direccion: {d[3]} | Telefono: {d[4]} | Correo: {d[5]} | Fecha inicio: {d[6]} | Salario: {d[7]} | Dept: {d[8]}")
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

def modificarEmpleado():
    try:
        os.system("clear")
        print("=== Modificar Datos Empleado ===")
        datosEmpleado = GestionEmpleado.mostrarTodos()
        if not datosEmpleado:
            print("No hay empleados para modificar")
            input("Presione enter para continuar")
            return
        
        for d in datosEmpleado:
            print(f"User_id: {d[0]} | Nombre: {d[2]}")
        try:
            ide = int(input("\nIngrese el id del empleado: ").strip())
        except ValueError:
            print("Id de empleado invalido")
            input("Presione enter para continuar")
            return
        
        emp = GestionEmpleado.buscarEmpleado(ide)
        if not emp:
            print("Empleado no encontrado")
            input("Presione enter para continuar")
            return
        
        lst = [emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6], emp[7], emp[8]]

        nuevo_nombre = input(f"Nombre [{emp[2]}] (con Enter mantiene valores): ").strip().capitalize()
        while True:
            #verificamos si el nombre esta vacio
            if not nuevo_nombre:
                nuevo_nombre = emp[2]
            #verificamos que el nombre solo contenga letras
            elif not nuevo_nombre.isalpha():
                print("Nombre invalido")
                nuevo_nombre = input(f"Nombre [{emp[2]}] (con Enter mantiene valores): ").strip().upper()
            else:
                break
        nuevo_direccion = input(f"Dirección [{emp[3]}] (con Enter mantiene valores): ").strip().capitalize()
        while True:
            #verificamos si la direccion esta vacia
            if not nuevo_direccion:
                nuevo_direccion = emp[3]
            #verificamos que la direccion solo contenga letras
            elif not nuevo_direccion.isalpha():
                print("Direccion invalida")
                nuevo_direccion = input(f"Dirección [{emp[3]}] (con Enter mantiene valores): ").strip().upper()
            else:
                break
        nuevo_telefono = input(f"Teléfono [{emp[4]}] (con Enter mantiene valores): ").strip()
        while True:
            #verificamos si el telefono esta vacio
            if not nuevo_telefono:
                nuevo_telefono = emp[4]
            #verificamos que el telefono solo contenga numeros
            elif not str(nuevo_telefono).isdigit():
                print("Telefono invalido")
                nuevo_telefono = input(f"Teléfono [{emp[4]}] (con Enter mantiene valores): ").strip()
            else:
                break
        nuevo_correo = input(f"Correo [{emp[5]}] (con Enter mantiene valores): ").strip()
        while True:
            #verificamos si el correo esta vacio
            if not nuevo_correo:
                nuevo_correo = emp[5]
            #verificamos que el correo sea valido
            elif not '@' in nuevo_correo or '.' not in nuevo_correo:
                print("Correo invalido")
                nuevo_correo = input(f"Correo [{emp[5]}] (con Enter mantiene valores): ").strip()
            else:
                break
        nuevo_fecha_inicio = input(f"Fecha inicio [{emp[6]}] (con Enter mantiene valores): ").strip() 
        while True:
            if not nuevo_fecha_inicio:
                nuevo_fecha_inicio = str(emp[6])
            try:
                datetime.strptime(nuevo_fecha_inicio, '%Y-%m-%d')
                break
            except (ValueError, AssertionError):
                print("Fecha invalida")
                nuevo_fecha_inicio = input(f"Fecha inicio [{emp[6]}] (con Enter mantiene valores): ").strip()
        nuevo_salario = input(f"Salario [{emp[7]}] (con Enter mantiene valores): ").strip() or str(emp[7])
        datosDepartamento = GestionDepartamento.mostrarTodo()
        if not datosDepartamento:
            print("No hay departamentos disponibles. No se cambiar el departamento.")
            print(f"Se mantiene el departamento actual: {emp[8]}")
            dept_valido = emp[8]
            input("Presione enter para continuar")
        else:
            print("Departamentos disponibles:")
            for d in datosDepartamento:
                print(f"ID: {d[0]} | Nombre: {d[1]}")

            while True:
                dept_input = input("Departamento ID (para asignar): ").strip()
                if not dept_input.isdigit():
                    print("Id de departamento invalido")
                dept_int = int(dept_input)
                if any(dept_int == d[0] for d in datosDepartamento):
                    dept_valido = dept_int
                    break
                print("Departamento no encontrado")

        lst[2] = nuevo_nombre
        lst[3] = nuevo_direccion
        lst[4] = nuevo_telefono
        lst[5] = nuevo_correo
        lst[6] = nuevo_fecha_inicio

        try:
            if nuevo_salario is not None and nuevo_salario != "":
                lst[7] = float(nuevo_salario)
            else:
                lst[7] = None
        except ValueError:
            print("Salario invalido")
            lst[7] = emp[7]
            input("Presione enter para continuar")
        
        if dept_valido is not None:
            lst[8] = int(dept_valido) 
        else:
            lst[8] = None

        GestionEmpleado.editar(lst)
        print(f"Empleado {emp[2]} modificado con exito")
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

def eliminarEmpleado():
    try:
        print("=== Eliminar Datos Empleado ===")
        datos = GestionEmpleado.mostrarTodos()
        if not datos:
            print("No hay empleados para eliminar")
            input("Presione enter para continuar")
            return
        for d in datos:
            print(f"User_id: {d[0]} | Nombre: {d[2]}\n----------------------------")
        id = input("\nIngrese el id del empleado: ").strip()
        while True:
            if not id.isdigit():
                print("Run de empleado invalido")
                id = input("Ingrese el id del empleado: ").strip()
            else:
                break
        if not GestionEmpleado.verificar(id):
            print("Empleado no encontrado")
            input("\nPresione enter para continuar")
            return
        GestionEmpleado.eliminar(id)
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

#------------------------------------------------------------------------------------------------
# funciones departamento

def ingresarDatosDepartamento():
    try:
        print("=== Insertar Datos Departamento ===")
        nombre = input("Ingrese el nombre del departamento: ").strip().capitalize()
        while True:
            if not nombre.isalpha():
                print("Nombre invalido")
                nombre = input("Ingrese el nombre del departamento: ").strip().upper()
            else:
                break
        datos = GestionEmpleado.mostrarTodos()
        if not datos:
            print("No hay empleados para mostrar")
            input("Presione enter para continuar")
            return
        for d in datos:
            print(f"User_id: {d[0]} | Nombre: {d[2]}\n----------------------------")
        gerente_id = input("Ingrese el id del gerente del departamento: ").strip()
        while True:
            if not gerente_id.isdigit():
                print("Id de gerente invalido")
                gerente_id = input("Ingrese el id del gerente del departamento: ").strip()
            elif not GestionDepartamento.verificarGerente(gerente_id):
                print("Gerente no encontrado")
                gerente_id = input("Ingrese el id del gerente del departamento: ").strip()
            else:
                break
        descripcion = input("Ingrese la descripcion del departamento: ").strip()
        GestionDepartamento.agregar(Departamento(nombre, gerente_id, descripcion))
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

def mostrarDatosDepartamento():
    try:
        print("=== Mostrar Datos Departamentos ===")
        datos = GestionDepartamento.mostrarTodo()
        if not datos:
            print("No hay departamentos para mostrar")
            input("Presione enter para continuar")
            return
        for d in datos:
            print(f"ID: {d[0]} | Nombre: {d[1]} | Gerente: {d[2]} | Descripcion: {d[3]}\n----------------------------")
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

def modificarDatosDepartamento():
    try:
        print("=== Modificar Datos Departamento ===")
        datos = GestionDepartamento.mostrarTodo()
        if not datos:
            print("No hay departamentos para modificar")
            input("Presione enter para continuar")
            return
        for d in datos:
            print(f"ID: {d[0]} | Nombre: {d[1]}\n----------------------------")
        id = input("\nIngrese el id del departamento: ").strip()
        while True:
            if not id.isdigit():
                print("Id de departamento invalido")
                id = input("Ingrese el id del departamento: ").strip()
            else:
                break
        if not GestionDepartamento.verificarDepartamento(id):
            print("Departamento no encontrado")
            input("\nPresione enter para continuar")
            return
        
        d = GestionDepartamento.buscarDepartamento(id)

        lst = [d[0], d[1], d[2], d[3]]

        nuevo_nombre = input("Ingrese el nuevo nombre del departamento: ").strip().capitalize()
        while True:
            #verificamos si el nombre esta vacio
            if not nuevo_nombre:
                nuevo_nombre = d[1]
            #verificamos que el nombre sea solo letras
            elif not nuevo_nombre.isalpha():
                print("Nombre invalido")
                nuevo_nombre = input("Ingrese el nuevo nombre del departamento: ").strip().upper()
            else:
                break
        datos = GestionEmpleado.mostrarTodos()
        if not datos:
            print("No hay empleados para mostrar")
            input("Presione enter para continuar")
            return
        for de in datos:
            print(f"User_id: {de[0]} | Nombre: {de[2]}\n----------------------------")
        nuevo_gerente = input("Ingrese el nuevo id del gerente del departamento: ").strip()
        while True:
            if not nuevo_gerente:
                nuevo_gerente = d[2]
            elif not nuevo_gerente.isdigit():
                print("Id de gerente invalido")
                nuevo_gerente = input("Ingrese el nuevo id del gerente del departamento: ").strip()
            elif not GestionDepartamento.verificarGerente(nuevo_gerente):
                print("Gerente no encontrado")
                nuevo_gerente = input("Ingrese el nuevo id del gerente del departamento: ").strip()
            else:
                break
        nueva_descripcion = input("Ingrese la nueva descripcion del departamento: ").strip() or d[3]

        lst[1] = nuevo_nombre
        lst[2] = nuevo_gerente
        lst[3] = nueva_descripcion

        GestionDepartamento.editar(lst)
        print(f"Departamento {d[1]} modificado con exito")
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

def eliminarDatosDepartamento():
    try:
        print("=== Eliminar Datos Departamento ===")
        datos = GestionDepartamento.mostrarTodo()
        if not datos:
            print("No hay departamentos para eliminar")
            input("Presione enter para continuar")
            return
        for d in datos:
            print(f"ID: {d[0]} | Nombre: {d[1]}\n----------------------------")
        id = input("\nIngrese el id del departamento: ").strip()
        while True:
            if not id.isdigit():
                print("Id de departamento invalido")
                id = input("Ingrese el id del departamento: ").strip()
            else:
                break
        if not GestionDepartamento.verificarDepartamento(id):
            print("Departamento no encontrado")
            input("\nPresione enter para continuar")
            return
        GestionDepartamento.eliminar(id)
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

#------------------------------------------------------------------------------------------------
# funciones proyecto

def ingresarDatosProyecto():
    try:
        print("=== Ingresar Datos Proyecto ===")
        nombre = input("Ingrese el nombre del proyecto: ").strip().capitalize()
        while True:
            if not nombre.isalpha():
                print("Nombre invalido")
                nombre = input("Ingrese el nombre del proyecto: ").strip().upper()
            else:
                break
        descripcion = input("Ingrese la descripcion del proyecto: ").strip().capitalize()
        fecha_inicio = input("Ingrese la fecha de inicio del proyecto (YYYY-MM-DD): ").strip()
        while True:
            if fecha_inicio == "":
                print("Fecha de inicio invalida")
                fecha_inicio = input("Ingrese la fecha de inicio del proyecto (YYYY-MM-DD): ").strip()
            elif not fecha_inicio:
                fecha_inicio = datetime.now().strftime("%Y-%m-%d")
            elif not re.match(r'^\d{4}-\d{2}-\d{2}$', fecha_inicio):
                print("Fecha de inicio invalida")
                fecha_inicio = input("Ingrese la fecha de inicio del proyecto (YYYY-MM-DD): ").strip()
            else:
                break
        p = Proyecto(nombre, descripcion, fecha_inicio)
        GestionProyecto.registrar(p)
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)
        
def mostrarDatosProyecto():
    try:
        print("=== Mostrar Datos Proyecto ===")
        datos = GestionProyecto.mostrarTodo()
        if not datos:
            print("No hay proyectos para mostrar")
            input("Presione enter para continuar")
            return
        for d in datos:
            print(f"ID: {d[0]} | Nombre: {d[1]} | Descripcion: {d[2]} | Fecha inicio: {d[3]}\n----------------------------")
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

def modificarDatosProyecto():
    try:
        print("=== Editar Datos Proyecto ===")
        datos = GestionProyecto.mostrarTodo()
        if not datos:
            print("No hay proyectos para editar")
            input("Presione enter para continuar")
            return
        for d in datos:
            print(f"ID: {d[0]} | Nombre: {d[1]} | Descripcion: {d[2]} | Fecha inicio: {d[3]}\n----------------------------")
        id = input("\nIngrese el id del proyecto: ").strip()
        while True:
            if not id.isdigit():
                print("Id de proyecto invalido")
                id = input("Ingrese el id del proyecto: ").strip()
            else:
                break
        if not GestionProyecto.verificar(id):
            print("Proyecto no encontrado")
            input("\nPresione enter para continuar")
            return
        p = GestionProyecto.buscarProyecto(id)
        lst = [p[0], p[1], p[2], p[3]]
        nuevo_nombre = input("Ingrese el nuevo nombre del proyecto: ").strip().capitalize()
        while True:
            if not nuevo_nombre:
                nuevo_nombre = p[1]
            elif not nuevo_nombre.isalpha():
                print("Nombre invalido")
                nuevo_nombre = input("Ingrese el nuevo nombre del proyecto (Enter para mantener el mismo): ").strip().upper()
            else:
                break
        nueva_descripcion = input("Ingrese la nueva descripcion del proyecto (Enter para mantener la misma): ").strip() or p[2]
        nueva_fecha_inicio = input("Ingrese la nueva fecha de inicio del proyecto (YYYY-MM-DD) (Enter para mantener la misma): ").strip()
        while True:
            if not nueva_fecha_inicio:
                nueva_fecha_inicio = p[3]
            elif not nueva_fecha_inicio:
                nueva_fecha_inicio = datetime.now().strftime("%Y-%m-%d")
            elif not re.match(r'^\d{4}-\d{2}-\d{2}$', nueva_fecha_inicio):
                print("Fecha de inicio invalida")
                nueva_fecha_inicio = input("Ingrese la nueva fecha de inicio del proyecto (YYYY-MM-DD) (Enter para mantener la misma): ").strip()
            else:
                break

        lst[1] = nuevo_nombre
        lst[2] = nueva_descripcion
        lst[3] = nueva_fecha_inicio

        GestionProyecto.editar(lst)
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

def eliminarDatosProyecto():
    try:
        print("=== Eliminar Datos Proyecto ===")
        datos = GestionProyecto.mostrarTodo()
        if not datos:
            print("No hay proyectos para eliminar")
            input("Presione enter para continuar")
            return
        for d in datos:
            print(f"ID: {d[0]} | Nombre: {d[1]} | Descripcion: {d[2]} | Fecha inicio: {d[3]}\n----------------------------")
        id = input("\nIngrese el id del proyecto: ").strip()
        while True:
            if not id.isdigit():
                print("Id de proyecto invalido")
                id = input("Ingrese el id del proyecto: ").strip()
            else:
                break
        if not GestionProyecto.verificar(id):
            print("Proyecto no encontrado")
            input("\nPresione enter para continuar")
        GestionProyecto.eliminar(id)
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

#------------------------------------------------------------------------------------------------
#funciones registro de tiempo

def ingresarDatosTiempo():
    try:
        print("=== Ingresar Datos Tiempo ===")
        empleados = GestionEmpleado.mostrarTodos()
        if not empleados:
            print("No hay empleados para mostrar")
            input("Presione enter para continuar")
            return
        
        print("=== Empleados Disponibles ===")
        for d in empleados:
            print(f"ID: {d[0]} | Nombre: {d[2]}\n----------------------------")
        
        while True:
            eId = input("\nIngrese el id del empleado: ").strip()
            if not eId.isdigit():
                print("Id de empleado invalido")
                eId = input("Ingrese el id del empleado: ").strip()
            else:
                break

        eId = int(eId)

        if not GestionEmpleado.verificar(eId):
            print("Empleado no encontrado")
            input("\nPresione enter para continuar")
            return

        os.system("clear")
        print("=== Proyectos Disponibles ===")
        proyecto = GestionProyecto.mostrarTodo()
        if not proyecto:
            print("No hay proyectos para mostrar")
            input("Presione enter para continuar")
            return
        for d in proyecto:
            print(f"ID: {d[0]} | Nombre: {d[1]} | Descripcion: {d[2]} | Fecha inicio: {d[3]}\n----------------------------")
        
        while True:
            pId = input("\nIngrese el id del proyecto: ").strip()
            if not pId.isdigit():
                print("Id de proyecto invalido")
                pId = input("Ingrese el id del proyecto: ").strip()
            else:
                break

        pId = int(pId)

        if not GestionProyecto.verificar(pId):
            print("Proyecto no encontrado")
            input("\nPresione enter para continuar")
            return

        while True:
            fecha = input("\nIngrese la fecha del registro (YYYY-MM-DD): ").strip()
            if not fecha:
                fecha = datetime.now().strftime("%Y-%m-%d")
            elif not re.match(r'^\d{4}-\d{2}-\d{2}$', fecha):
                print("Fecha invalida")
                fecha = input("Ingrese la fecha del registro (YYYY-MM-DD): ").strip()
            else:
                break

        while True:
            horas = input("\nIngrese las horas trabajadas: ").strip()
            if not horas.isdigit():
                print("Horas invalidas")
                horas = input("Ingrese las horas trabajadas: ").strip()
            else:
                break

        descripcion = input("\nIngrese la descripcion del registro: ").strip()

        tiempo = RegistroTiempo(eId, pId, fecha, horas, descripcion)
        GestionTiempo.agregar(tiempo)
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

def mostrarDatosTiempo():
    try:
        print("=== Mostrar Datos Tiempo ===")
        datos = GestionTiempo.mostrarTodo()
        if not datos:
            print("No hay tiempos para mostrar")
            input("Presione enter para continuar")
            return
        for d in datos:
            print(f"ID: {d[0]} | Empleado: {d[1]} | Proyecto: {d[2]} | Fecha: {d[3]} | Horas: {d[4]} | Descripcion: {d[5]}\n----------------------------")
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

#------------------------------------------------------------------------------------------------
#funcinoes asignacion

def asignar():
    try:
        print("=== Asignar Empleado a Proyecto ===")
        empleados = GestionEmpleado.mostrarTodos()
        if not empleados:
            print("No hay proyectos para mostrar")
            input("Presione enter para continuar")
            return
        
        print("=== Empleados Disponibles ===")
        for d in empleados:
            print(f"ID: {d[0]} | Nombre: {d[2]}\n----------------------------")
        
        while True:
            eId = input("\nIngrese el id del empleado: ").strip()
            if not eId.isdigit():
                print("Id de empleado invalido")
                eId = input("Ingrese el id del empleado: ").strip()
            else:
                break

        eId = int(eId)

        if not GestionEmpleado.verificar(eId):
            print("Empleado no encontrado")
            input("\nPresione enter para continuar")
            return

        proyectos = GestionProyecto.mostrarTodo()
        if not proyectos:
            print("No hay proyectos para mostrar")
            input("Presione enter para continuar")
            return

        print("=== Proyectos Disponibles ===")
        for d in proyectos:
            print(f"ID: {d[0]} | Nombre: {d[1]} | Descripcion: {d[2]} | Fecha inicio: {d[3]}\n----------------------------")

        while True:
            pId = input("\nIngrese el id del proyecto: ").strip()
            if not pId.isdigit():
                print("Id de proyecto invalido")
                pId = input("Ingrese el id del proyecto: ").strip()
            else:
                break

        pId = int(pId)

        if not GestionProyecto.verificar(pId):
            print("Proyecto no encontrado")    
            input("\nPresione enter para continuar")
            return

        rol = input("\nIngrese el rol del empleado (Opcional): ").strip()

        Asignacion_emp.asignar(eId, pId, rol or None)
        input("Presione enter para continuar")
        return

    except Exception as e:
        print(e)

def desasignar():
    try:
        print("=== Desasignar Empleado de Proyecto ===")
        empleado = GestionEmpleado.mostrarTodos()
        for e in empleado:
            print(f"ID: {e[0]} | Nombre: {e[2]}\n----------------------------")
        
        while True:
            eId = input("\nIngrese el id del empleado: ").strip()
            if not eId.isdigit():
                print("Id de empleado invalido")
                eId = input("Ingrese el id del empleado: ").strip()
            else:
                break

        eId = int(eId)

        if not GestionEmpleado.verificar(eId):
            print("Empleado no encontrado")
            input("\nPresione enter para continuar")
            return

        asignaciones = Asignacion_emp.obtenerPorEmpleado(eId)
        if not asignaciones:
            print("Empleado no asignado a ningun proyecto")
            input("\nPresione enter para continuar")
            return
        
        proyectos = GestionProyecto.mostrarTodo()
        proyecto_dict = {}

        proyectos = GestionProyecto.mostrarTodo()
        proyecto_dict = {}

        for p in proyectos:
            proyecto_dict[p[0]] = p[1]

        print("=== Asignaciones del empleado===")
        for r in asignaciones:
            asign_id = r[0]
            proyecto_id = r[2]
            rol = r[4]
            proyecto_nombre = proyecto_dict.get(proyecto_id, f"ID {proyecto_id}")
            print(f"ID: {asign_id} | Proyecto: {proyecto_nombre} | Rol: {rol}\n----------------------------")

        opm = input("\n¿Desea desasignar al empleado de un proyecto? (S/N): ").strip().upper()
        if opm != "S":
            print("Accion cancelada")
            input("Presione enter para continuar")
            return
        
        asid_input = input("\nIngrese el id de la asignacion: ").strip()
        while True:
            if not asid_input.isdigit():
                print("Id de asignacion invalido")
                asid_input = input("Ingrese el id de la asignacion: ").strip()
            else:
                break

        asid = int(asid_input)

        if not Asignacion_emp.verificar(asid):
            print("Asignacion no encontrada")
            input("\nPresione enter para continuar")
            return
            
        Asignacion_emp.desasignar(asid)
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

def mostrarPorEmpleado():
    try:
        print("=== Mostrar Asignaciones por Empleado ===")
        empleados = GestionEmpleado.mostrarTodos()
        if not empleados:
            print("No hay empleados para mostrar")
            input("Presione enter para continuar")
            return
        
        for d in empleados:
            print(f"ID: {d[0]} | Nombre: {d[2]}\n----------------------------")
        id = input("\nIngrese el id del empleado: ").strip()

        while True:
            if not id.isdigit():
                print("ID de empleado invalido")
                id = input("Ingrese el id del empleado: ").strip()
            else:
                break

        id = int(id)

        if not GestionEmpleado.verificar(id):
            print("Empleado no encontrado")
            input("\nPresione enter para continuar")
            return

        asignaciones = Asignacion_emp.obtenerPorEmpleado(id)
        if not asignaciones:
            print("El empleado no tiene asignaciones")
            input("\nPresione enter para continuar")
            return
        
        proyectos = GestionProyecto.mostrarTodo()
        proyecto_dict = {}

        for p in proyectos:
            proyecto_dict[p[0]] = p[1]

        print("=== Asignaciones del empleado===")
        for r in asignaciones:
            asign_id = r[0]
            proyecto_id = r[2]
            rol = r[4]
            proyecto_nombre = proyecto_dict.get(proyecto_id, f"ID {proyecto_id}")
            print(f"ID: {asign_id} | Proyecto: {proyecto_nombre} | Rol: {rol}\n----------------------------")
        input("Presione enter para continuar")
        return

    except Exception as e:
        print(e)
#------------------------------------------------------------------------------------------------
#funcion Informe
def generarInforme():
    try:
        os.system("clear")
        print("==============================================")
        print("         I N F O R M E  G E N E R A L         ")
        print("==============================================")

        print("=== Empleados ===\n")
        empleados = GestionEmpleado.mostrarTodos()
        if not empleados:
            print("No hay empleados para mostrar")

        empleados_dict = {}

        for e in empleados:
            empleados_dict[e[0]] = e[2]

        for e in empleados:
            correo = e[5] if len(e) > 5 else ""
            dept = e[8] if len(e) > 8 else ""
            print(f"  ID: {e[0]} | Nombre: {e[2]} | RUN: {e[1]} | Correo: {correo} | Dept: {dept}")
        print("-" * 100)

        print("=== Departamentos ===\n")

        departamentos = GestionDepartamento.mostrarTodo()
        if not departamentos:
            print("No hay departamentos para mostrar")

        for d in departamentos:
            gerente_id = d[2] if len(d) > 2 else ""
            gerente_nombre = empleados_dict.get(gerente_id, f"ID {gerente_id}")
            empleados_en_dept = []

            for e in empleados:
                if len(e) > 8 and e[8] == d[0]:
                    empleados_en_dept.append(e[2])

            empleado_str = ""
            primero = True
            for nombre in empleados_en_dept:
                if primero:
                    empleado_str = nombre
                    primero = False
                else:
                    empleado_str += ", " + nombre
            
            if empleado_str == "":
                empleado_str = "No hay empleados en este departamento"

            print(f"  ID: {d[0]} | Nombre: {d[1]} | Gerente: {gerente_nombre} | Empleados: {empleado_str}")
        print("-" * 100)

        print("=== Proyectos ===\n")

        proyectos = GestionProyecto.mostrarTodo()
        if not proyectos:
            print("No hay proyectos para mostrar")

        for p in proyectos:
            dept_id = p[2] if len(p) > 2 else ""
            emp_ids = []
            for e in empleados:
                asigns = Asignacion_emp.obtenerPorEmpleado(p[0])
                for a in asigns:
                    if a[2] == p[0]:
                        emp_ids.append(e[0])

            emp_str = ""
            primero = True
            for id in emp_ids:
                if primero:
                    emp_str = id
                    primero = False
                else:
                    emp_str += ", " + id

            if emp_str == "":
                emp_str = "No hay empleados en este proyecto"

            print(f"  ID: {p[0]} | Nombre: {p[1]} | Dept: {dept_id} | Empleados: {emp_str}")
        print("-" * 100)

        print("=== Registros de Tiempo ===\n")

        tiempos = GestionTiempo.mostrarTodo()
        if not tiempos:
            print("No hay tiempos para mostrar")

        for t in tiempos:
            fecha = t[3] if len(t) > 3 else ""
            horas = t[4] if len(t) > 4 else ""
            empleado_nombre = empleados_dict.get(t[1], f"ID {t[1]}")
            print(f"  ID: {t[0]} | Empleado: {empleado_nombre} | Proyecto: {t[2]} | Fecha: {fecha} | Horas: {horas} | Descripcion: {t[5]}")
        print("-" * 100)

        print("=== Indicadores ===\n")
        indicadores = GestionIndicador.obtenerTodos()
        if not indicadores:
            print("No hay indicadores para mostrar")

        for i in indicadores:
            print(f"  ID: {i[0]} | Tipo: {i[1]} | Fecha: {i[2]} | Valor: {i[3]} | Fecha Solicitada: {i[4]} | id_usuario: {i[5]} | Fuente: {i[6]}")
        print("-" * 100)

        input("\nPresione enter para continuar")
    except Exception as e:
        print(e)

#------------------------------------------------------------------------------------------------
# funciones usuarios
def ingresoUsuario():
    try:
        os.system("clear")
        print("========================================")
        print("      I N G R E S O  U S U A R I O      ")
        print("========================================")
        username = input("Username: ").strip()
        while True:
            while True:
                clave1 = getpass("Contraseña: ").strip()
                if len(clave1) < 8 or len(clave1) > 16:
                    print("La contraseña debe tener entre 8 y 16 caracteres.")
                elif not re.search("[A-Z]", clave1):
                    print("La contraseña debe contener al menos una letra mayúscula.")
                elif not re.search("[a-z]", clave1):
                    print("La contraseña debe contener al menos una letra minúscula.")
                elif not re.search("[0-9]", clave1):
                    print("La contraseña debe contener al menos un número.")
                elif not re.search("[!@#$%^&*()_+]", clave1):
                    print("La contraseña debe contener al menos un carácter especial.")
                else:
                    break
            while True:
                clave2 = getpass("Confirmar contraseña: ").strip()
                if clave2 != clave1:
                    print("Las contraseñas no coinciden. Por favor, ingrese la contraseña nuevamente.")
                else:
                    break
            if clave1 == clave2:
                break

        while True:
            nombre = input("Nombre: ").strip().capitalize()
            if not nombre.isalpha():
                print("El nombre debe contener solo letras.")
            else:
                break
        while True:
            apellidos = input("Apellidos: ").strip().capitalize()
            if not apellidos.isalpha():
                print("Los apellidos deben contener solo letras.")
            else:
                break
        while True:
            correo = input("Correo: ").strip()
            if not "@" in correo or not "." in correo:
                print("El correo debe ser contener un @ y un punto.")
            else:
                break

        print("========== Tipos de usuario ===========")
        print("  1. Administrador")
        print("  2. Usuario")
        while True:
            tipo = input("Ingrese el tipo de usuario: ").strip()
            if not tipo.isdigit():
                print("Tipo de usuario invalido")
            elif int(tipo) < 1 or int(tipo) > 2:
                print("Tipo de usuario invalido")
            elif tipo == 1:
                tipo = "Administrador"
            elif tipo == 2:
                tipo = "Usuario"
            else:
                break
        Usuario.registrar_usuario(username, clave1, nombre, apellidos, correo, tipo)
        print("========================================")
    except Exception as e:
        print(e)

def login():
    try:
        os.system("clear")
        print("====================================")
        print("      L O G I N  U S U A R I O      ")
        print("====================================")
        global nombreUsuario
        username = input("Username: ").strip()
        clave = getpass("Contraseña: ").strip()
        exito = Usuario.login(username, clave)
        nombreUsuario = username
        acceso = False
        if exito:
            print("Login exitoso")
            acceso = True
        else:
            print("Login fallido")
            acceso = False
        print("====================================")
        return acceso
    except Exception as e:
        print(e)
#------------------------------------------------------------------------------------------------
# funcion indicadores
def consultaIndicadores():
    os.system('clear')
    print("=== Consulta Externa de Indicadores Económicos ===")
    
    TIPO_INDICADOR = input("Ingrese el tipo de indicador (UF, IVP, IPC, UTM, Dolar, Euro): ").strip().upper()
    while True:
        FECHA_CONSULTA = input("Ingrese la fecha a consultar (DD-MM-AAAA): ").strip()
        try:
            FECHA_CONSULTA = datetime.strptime(FECHA_CONSULTA, "%d-%m-%Y").strftime("%d-%m-%Y")
            break
        except ValueError:
            print("Formato de fecha incorrecto. Debe ser DD-MM-AAAA.")

    indicador_map = {
        "UF": "uf", "IVP": "ivp", "IPC": "ipc", 
        "UTM": "utm", "DOLAR": "dolar", "EURO": "euro"
    }
    
    endpoint = indicador_map.get(TIPO_INDICADOR)

    if not endpoint:
        print("Tipo de indicador no reconocido o no soportado por la API de ejemplo.")
        input("ENTER para continuar...")
        return

    API_URL = f"https://mindicador.cl/api/{endpoint}/{FECHA_CONSULTA}"

    print(f"\nConsultando {TIPO_INDICADOR} para el {FECHA_CONSULTA}...")
    
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status() 
        
        datos_json = response.json()
        
        serie = datos_json.get("serie", [])
        
        id_usuario_obtenido = GestionUsuario.verificarTipo(nombreUsuario)[0][0]

        if serie:
            valor = serie[0].get("valor")
            fecha_valor = serie[0].get("fecha", "")[:10] 
            
            print(f"\n Valor Obtenido: {TIPO_INDICADOR} = ${valor:,.2f}")
            print(f"   Fecha del Valor: {fecha_valor}")

            almacenar = input("\n¿Desea almacenar este valor en la base de datos? (S/N): ").strip().upper()

            if almacenar == 'S':
                existente = GestionIndicador.obtenerPorFecha(fecha_valor, TIPO_INDICADOR)
                
                if existente:
                    print(f"El indicador {TIPO_INDICADOR} para {fecha_valor} ya existe (ID: {existente[0]}). No se almacena.")
                else:
                    FECHA_CONSULTA = datetime.now().strftime('%Y-%m-%d')
                    indicador = IndicadorEconomico(
                    tipo_indicador = TIPO_INDICADOR,
                    fecha_valor = fecha_valor,
                    valor = valor,
                    fecha_consulta = FECHA_CONSULTA,
                    id_usuario = id_usuario_obtenido,
                    fuente = API_URL 
                    )
                    GestionIndicador.agregar(indicador)
            
        else:
            print(f"No se encontró el valor para {TIPO_INDICADOR} en la fecha {FECHA_CONSULTA}.")

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión o API: {e}")
    except json.JSONDecodeError:
        print("Error al decodificar la respuesta JSON de la API.")
    except Exception as e:
        print(f"ERROR desconocido durante la consulta: {e}")

    input("ENTER para continuar...")

def mostrarIndicadores():
    try:
        os.system('clear')
        print("=== Listado de Indicadores Económicos ===")
        id_usuario = GestionUsuario.obtenerID(nombreUsuario)
        tipo = GestionUsuario.verificarTipo(nombreUsuario)[0][6]
        indicadores = GestionIndicador.obtenerTodos()
        if tipo == "Administrador":
            if not indicadores:
                print("No hay indicadores para mostrar")
                input("Presione enter para continuar")
                return
            else:
                for i in indicadores:
                    print(f"ID: {i[0]}")
                    print(f"Tipo de Indicador: {i[1]}")
                    print(f"Fecha del Valor: {i[2]}")
                    print(f"Valor: {i[3]:,.2f}")
                    print(f"ID Usuario: {i[5]}")
                    print("------------------------------------")
                input("ENTER para continuar...")
        else:
            if not indicadores:
                print("No hay indicadores para mostrar")
                input("ENTER para continuar...")
                return
            indicadores = GestionIndicador.obtenerPorId(id_usuario)
            for i in indicadores:
                print(f"ID: {i[0]}")
                print(f"Tipo de Indicador: {i[1]}")
                print(f"Fecha del Valor: {i[2]}")
                print(f"Valor: {i[3]:,.2f}")
                print(f"ID Usuario: {i[5]}")
                print("------------------------------------")
            input("ENTER para continuar...")
    except Exception as e:
        print(e)

def eliminarIndicador():
    try:
        os.system('clear')
        print("=== Eliminar Indicadores Económicos ===")
        indicadores = GestionIndicador.obtenerTodos()
        print(indicadores)
        if not indicadores:
            print("No hay indicadores para eliminar")
            input("ENTER para continuar...")
            return
        else:
            for i in indicadores:
                print(f"ID: {i[0]} | Tipo de Indicador: {i[1]} | Fecha del Valor: {i[2]} | Valor: {i[3]:,.2f}")
                print("------------------------------------")
            try:
                id_indicador = int(input("Ingrese el ID del indicador a eliminar: "))
            except ValueError:
                print("Opcion invalida")
                input("ENTER para continuar...")
                return
            if id_indicador in [i[0] for i in indicadores]:
                GestionIndicador.eliminar(id_indicador)
                print("Indicador eliminado con exito")
            else:
                print("Indicador no encontrado")
        input("ENTER para continuar...")
    except Exception as e:
        print(e)

#------------------------------------------------------------------------------------------------
# main

if __name__ == "__main__":
    try:
        while True:
            os.system("clear")
            menuUsuario()
            op = input("Ingrese una opcion: ").strip()
            if op == '1':
                ingresoUsuario()
            elif op == '2':
                acceso = login()
                if acceso:
                    dato = GestionUsuario.verificarTipo(nombreUsuario)
                    tipo = dato[0][6]
                    if tipo == "Administrador":
                        while True:
                            menuPrincipal(tipo)
                            try:
                                while True:
                                    op = input("Ingrese una opcion: ").strip()
                                    break
                            except ValueError:
                                print("Opcion invalida")
                            if op == '1':
                                menuEmpleado()
                            elif op == '2':
                                menuDepartamento()
                            elif op == '3':
                                menuProyecto()
                            elif op == '4':
                                menuRegistroTiempo()
                            elif op == '5':
                                menuAsignacion()
                            elif op == '6':
                                menuIndicador(tipo)
                            elif op == '7':
                                generarInforme()
                            elif op == '8':
                                print("Saliendo...")
                                break
                    else:
                        while True:
                            menuPrincipal(tipo)
                            op = input("Ingrese una opcion: ").strip()
                            if op == '1':
                                menuIndicador(tipo)
                            elif op == '2':
                                menuRegistroTiempo()
                            elif op == '3':
                                print("Saliendo...")
                                break
            elif op == '3':
                print("Saliendo...")
                break
    except Exception as e:
        print(e)
