# Importar sistema 
import os, datetime

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
    opm = input("Ingrese una opcion: ").strip()
    while True:
        if opm not in ['1','2','3','4','5','6','7']:
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
            opm = input("Ingrese una opcion: ").strip()
        else:
            break
    if opm == '1':
        menuEmpleado()
    elif opm == '2':
        menuDepartamento()
    elif opm == '3':
        menuProyecto()
    elif opm == '4':
        menuTiempo()
    elif opm == '5':
        menuAsignacion()
    elif opm == '6':
        menuInforme()
    elif opm == '7':
        return

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
        run = input("Ingrese el run: ").strip()
        while True:
            if not run.isdigit():
                print("Run invalido")
                run = input("Ingrese el run: ").strip()
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

        fecha_inicio = input("Ingrese la fecha de contrato (dd-mm-aaaa): ").strip()
        while True:
            try:
                fecha = datetime.datetime.strptime(fecha_inicio, "%d-%m-%Y")
                if fecha > datetime.datetime.now():
                    print("Fecha de contrato invalida")
                    fecha_inicio = input("Ingrese la fecha de contrato (dd-mm-aaaa): ").strip()
                else:
                    break
            except ValueError:
                print("Fecha de contrato invalida")
                fecha_inicio = input("Ingrese la fecha de contrato (dd-mm-aaaa): ").strip()

        salario = input("Ingrese el salario: ").strip()
        while True:
            if not salario.isdigit():
                print("Salario invalido")
                salario = input("Ingrese el salario: ").strip()
            else:
                break

        departamento_id = input("Ingrese el id del departamento: ").strip()
        while True:
            if not departamento_id.isdigit():
                print("Id de departamento invalido")
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
        for d in datos:
            print(f"User_id: {d[0]} | Run: {d[1]} | Nombre: {d[2]} | Direccion: {d[3]} | Telefono: {d[4]} | Correo: {d[5]} | Fecha inicio: {d[6]} | Salario: {d[7]} | Dept: {d[8]}")
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

def mostrarDatoEmpleadoEspecifico():
    try:
        print("=== Mostrar Datos Empleado Especifico ===")
        EmpleadoData = GestionEmpleado.mostrarTodos()
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
        os.system("cls")
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

        nuevo_nombre = input(f"Nombre [{emp[2]}] (con Enter mantiene valores): ") or emp[2]
        nuevo_direccion = input(f"Dirección [{emp[3]}] (con Enter mantiene valores): ") or emp[3]
        nuevo_telefono = input(f"Teléfono [{emp[4]}] (con Enter mantiene valores): ") or emp[4]
        nuevo_correo = input(f"Correo [{emp[5]}] (con Enter mantiene valores): ") or emp[5]
        nuevo_fecha_inicio = input(f"Fecha inicio [{emp[6]}] (con Enter mantiene valores): ") or emp[6]
        nuevo_salario = input(f"Salario [{emp[7]}] (con Enter mantiene valores): ") or str(emp[7])

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
        GestionEmpleado.mostrarTodos()
        id = input("Ingrese el id del empleado: ").strip()
        while True:
            if not id.isdigit():
                print("Run de empleado invalido")
                id = input("Ingrese el id del empleado: ").strip()
            else:
                break
        GestionEmpleado.eliminar(id)
        input("Presione enter para continuar")
        return
    except Exception as e:
        print(e)

#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------

os.system("cls")
modificarEmpleado()