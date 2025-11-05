# Importar sistema 
import os, datetime, time

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
    os.system("clear")
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
                os.system("clear")
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
            try:
                fecha = datetime.datetime.strptime(fecha_inicio, "%Y-%m-%d")
                if fecha > datetime.datetime.now():
                    print("Fecha de contrato invalida")
                    fecha_inicio = input("Ingrese la fecha de contrato (aaaa-mm-dd): ").strip()
                else:
                    break
            except ValueError:
                print("Fecha de contrato invalida")
                fecha_inicio = input("Ingrese la fecha de contrato (aaaa-mm-dd): ").strip()

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
            elif not GestionDepartamento.verificar(departamento_id):
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

        nuevo_nombre = input(f"Nombre [{emp[2]}] (con Enter mantiene valores): ").strip().capitalize() or emp[2]
        nuevo_direccion = input(f"Dirección [{emp[3]}] (con Enter mantiene valores): ").strip().capitalize() or emp[3]
        nuevo_telefono = input(f"Teléfono [{emp[4]}] (con Enter mantiene valores): ").strip() or emp[4]
        nuevo_correo = input(f"Correo [{emp[5]}] (con Enter mantiene valores): ").strip() or emp[5]
        nuevo_fecha_inicio = input(f"Fecha inicio [{emp[6]}] (con Enter mantiene valores): ").strip() or emp[6]
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

#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------

def main():
    while True:
        menuPrincipal()
        opm = input("Ingrese una opcion: ").strip()
        while True:
            if not opm in ("1", "2", "3", "4", "5", "6", "7"):
                print("Opcion invalida")
                opm = input("Ingrese una opcion: ").strip()
            else:
                break
        if opm == "1":
            menuEmpleado()
        elif opm == "2":
            menuDepartamento()
        elif opm == "3":
            menuProyecto()
        elif opm == "4":
            menuRegistroTiempo()
        elif opm == "5":
            menuRegistroHoras()
        elif opm == "6":
            menuReporte()
        elif opm == "7":
            opm = input("Desea salir? (S/N): ").strip().upper()
            if opm == "S":
                print("Saliendo...")
                time.sleep(0.8)
                os.system("clear")
                break
            else:
                continue

main()