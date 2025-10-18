# Importar sistema 
import os

# Carpeta DAO
import DAO.CRUDGestionDepartamento 
import DAO.CRUDGestionEmpleado 
import DAO.CRUDGestionProyecto 
import DAO.CRUDGestionUsuario

# Carpeta DTO
from DTO.Departamento import Departamento
from DTO.Empleado import Empleado
from DTO.Persona import Persona
from DTO.Proyecto import Proyecto
from DTO.RegistroTiempo import RegistroTiempo
from DTO.Usuario import Usuario

def menuPrincipal():
    os.system("cls")
    print("================================")
    print("   M E N U  P R I N C I P A L   ")
    print("================================")
    print("          1. INGRESAR           ")
    print("          2. MOSTRAR            ")
    print("          3. MODIFICAR          ")
    print("          4. ELIMINAR           ")
    print("          5. SALIR              ")
    print("================================")

def menuIngresar():
    os.system("cls")
    print("======================================")
    print("       M E N U  I N G R E S A R       ")
    print("======================================")
    print("      1. INGRESAR DEPARTAMENTO        ")
    print("      2. INGRESAR EMPLEADO            ")
    print("      3. INGRESAR PROYECTO            ")
    print("      4. INGRESAR USUARIO             ")
    print("      5. VOLVER AL MENU               ")
    print("======================================")

def menuMostrar():
    os.system("cls")
    print("======================================")
    print("        M E N U  M O S T R A R        ")
    print("======================================")
    print("      1. MOSTRAR DEPARTAMENTO         ")
    print("      2. MOSTRAR EMPLEADO             ")
    print("      3. MOSTRAR PROYECTO             ")
    print("      4. MOSTRAR USUARIO              ")
    print("      5. VOLVER AL MENU               ")
    print("======================================")

def menuMostrarEspecifico():
    os.system("cls")
    print("======================================")
    print("        M E N U  M O S T R A R        ")
    print("======================================")
    print("      1. MOSTRAR TODO                 ")
    print("      2. MOSTRAR ESPECIFICO           ")
    print("      3. MOSTRAR PARCIAL              ")
    print("      4. VOLVER AL MENU               ")
    print("======================================")

def menuModificar():
    os.system("cls")
    print("======================================")
    print("       M E N U  M O D I F I C A R     ")
    print("======================================")
    print("      1. MODIFICAR DEPARTAMENTO       ")
    print("      2. MODIFICAR EMPLEADO           ")
    print("      3. MODIFICAR PROYECTO           ")
    print("      4. MODIFICAR USUARIO            ")
    print("      5. VOLVER AL MENU               ")
    print("======================================")

def menuEliminar():
    os.system("cls")
    print("======================================")
    print("        M E N U  E L I M I N A R      ")
    print("======================================")
    print("      1. ELIMINAR DEPARTAMENTO        ")
    print("      2. ELIMINAR EMPLEADO            ")
    print("      3. ELIMINAR PROYECTO            ")
    print("      4. ELIMINAR USUARIO             ")
    print("      5. VOLVER AL MENU               ")
    print("======================================")

#------------------------------------------------------------------------------------------------

# Funciones Usuario
def ingresarDatosUsuario():
    os.system("cls")
    print("============================================")
    print("       I N G R E S A R  U S U A R I O       ")
    print("============================================")
    id = input("Ingrese ID: ")
    nombre = input("Ingrese Nombre: ")
    apellido = input("Ingrese Apellido: ")
    correo = input("Ingrese Correo: ")
    telefono = input("Ingrese Telefono: ")
    clave = input("Ingrese Clave: ")
    acceso = input("Ingrese Acceso: ")
    u = Usuario(id, nombre, apellido, correo, telefono, clave, acceso)
    DAO.CRUDGestionUsuario.registrarUsuario(u)

def mostrarDatosUsuario():
    os.system("cls")
    print("==============================================================")
    print("        M O S T R A R  T O D O S  L O S  U S U A R I O        ")
    print("==============================================================")
    usuarios = DAO.CRUDGestionUsuario.mostrarUsuario()
    for u in usuarios:
        print(f"ID: {u[0]} | Nombre: {u[1]} | Apellido: {u[2]} | Correo: {u[3]} | Telefono: {u[4]} | Clave: {u[5]} | Acceso: {u[6]}")
    input("\n\n Presione Enter para continuar...")

def mostrarDatosUsuarioEspecifico():
    os.system("cls")
    print("=========================================================")
    print("    M O S T R A R  U S U A R I O  E S P E C I F I C O    ")
    print("=========================================================")
    id = input("Ingrese ID del usuario a buscar: ")
    u = DAO.CRUDGestionUsuario.buscarUsuario(id)
    if u:
        print(f"ID: {u[0]} | Nombre: {u[1]} | Apellido: {u[2]} | Correo: {u[3]} | Telefono: {u[4]} | Clave: {u[5]} | Acceso: {u[6]}")
    else:
        print("Usuario no encontrado.")
    input("\n\n Presione Enter para continuar...")

def mostrarDatosUsuarioParcial():
    os.system("cls")
    print("=====================================================")
    print("     M O S T R A R  U S U A R I O  P A R C I A L     ")
    print("=====================================================")
    cant = int(input("Ingrese la cantidad de usuarios a mostrar: "))
    datos = DAO.CRUDGestionUsuario.cosultaparcialUsuario(cant)
    for u in datos:
        print(f"ID: {u[0]} | Nombre: {u[1]} | Apellido: {u[2]} | Correo: {u[3]} | Telefono: {u[4]} | Clave: {u[5]} | Acceso: {u[6]}")
    input("\n\n Presione Enter para continuar...")

def modificarDatosUsuario():
    os.system("cls")
    listanuevos = []
    print("============================================")
    print("       M O D I F I C A R  U S U A R I O     ")
    print("============================================")
    mostrarDatosUsuario()
    mod = input("Ingrese el ID del usuario a modificar: ")
    datos = DAO.CRUDGestionUsuario.buscarUsuario(mod)
    print(f"ID: {datos[0]}")
    listanuevos.append(datos[0])
    
    opm = input(f"Desea modificar el Nombre {datos[1]}? (s/n): ")
    if opm.lower() == 's':
        nuevo_nombre = input("Ingrese el nuevo Nombre: ")
        listanuevos.append(nuevo_nombre)
    else:
        listanuevos.append(datos[1])
    opm = input(f"Desea modificar el Apellido {datos[2]}? (s/n): ")
    if opm.lower() == 's':
        nuevo_apellido = input("Ingrese el nuevo Apellido: ")
        listanuevos.append(nuevo_apellido)
    else:
        listanuevos.append(datos[2])
    opm = input(f"Desea modificar el Correo {datos[3]}? (s/n): ")
    if opm.lower() == 's':
        nuevo_correo = input("Ingrese el nuevo Correo: ")
        listanuevos.append(nuevo_correo)
    else:
        listanuevos.append(datos[3])
    opm = input(f"Desea modificar el Telefono {datos[4]}? (s/n): ")
    if opm.lower() == 's':
        nuevo_telefono = input("Ingrese el nuevo Telefono: ")
        listanuevos.append(nuevo_telefono)
    else:
        listanuevos.append(datos[4])
    opm = input(f"Desea modificar la Clave {datos[5]}? (s/n): ")
    if opm.lower() == 's':
        nueva_clave = input("Ingrese la nueva Clave: ")
        listanuevos.append(nueva_clave)
    else:
        listanuevos.append(datos[5])
    opm = input(f"Desea modificar el Acceso {datos[6]}? (s/n): ")
    if opm.lower() == 's':
        nuevo_acceso = input("Ingrese el nuevo Acceso: ")
        listanuevos.append(nuevo_acceso)
    else:
        listanuevos.append(datos[6])
    DAO.CRUDGestionUsuario.modificarUsuario(Usuario(listanuevos[0], listanuevos[1], listanuevos[2], listanuevos[3], listanuevos[4], listanuevos[5], listanuevos[6]))

def eliminarDatosUsuario():
    os.system("cls")
    print("============================================")
    print("        E L I M I N A R  U S U A R I O      ")
    print("============================================")
    id = input("Ingrese ID del usuario a eliminar: ")
    DAO.CRUDGestionUsuario.eliminarUsuario(id)

#------------------------------------------------------------------------------------------------

# Funciones Departamento
def ingresarDatosDepartamento():
    os.system("cls")
    print("==================================================")
    print("     I N G R E S A R  D E P A R T A M E N T O     ")
    print("==================================================")
    id = input("Ingrese ID: ")
    nombre = input("Ingrese Nombre: ")
    gerente = input("Ingrese Gerente: ")
    d = Departamento(id, nombre, gerente)
    DAO.CRUDGestionDepartamento.registrarDepartamento(d)

def mostrarDatosDepartamento():
    os.system("cls")
    print("================================================================")
    print("   M O S T R A R  T O D O S  L O S  D E P A R T A M E N T O S   ")
    print("================================================================")
    departamentos = DAO.CRUDGestionDepartamento.mostrarDepartamento()
    for d in departamentos:
        print(f"ID: {d[0]} | Nombre: {d[1]} | Gerente: {d[2]}")
    input("\n\n Presione Enter para continuar...")

def mostrarDatosDepartamentoEspecifico():
    os.system("cls")
    print("=============================================================")
    print(" M O S T R A R  D E P A R T A M E N T O  E S P E C I F I C O ")
    print("=============================================================")
    id = input("Ingrese ID del departamento a buscar: ")
    d = DAO.CRUDGestionDepartamento.buscarDepartamento(id)
    if d:
        print(f"ID: {d[0]} | Nombre: {d[1]} | Gerente: {d[2]}")
    else:
        print("Departamento no encontrado.")
    input("\n\n Presione Enter para continuar...")

def mostrarDatosDepartamentoParcial():
    os.system("cls")
    print("=======================================================")
    print(" M O S T R A R  D E P A R T A M E N T O  P A R C I A L ")
    print("=======================================================")
    cant = int(input("Ingrese la cantidad de departamentos a mostrar: "))
    datos = DAO.CRUDGestionDepartamento.cosultaparcialDepartamento(cant)
    for d in datos:
        print(f"ID: {d[0]} | Nombre: {d[1]} | Gerente: {d[2]}")
    input("\n\n Presione Enter para continuar...")

def modificarDatosDepartamento():
    os.system("cls")
    listanuevos = []
    print("====================================================")
    print("     M O D I F I C A R  D E P A R T A M E N T O     ")
    print("====================================================")
    mostrarDatosDepartamento()
    mod = input("Ingrese el ID del departamento a modificar: ")
    datos = DAO.CRUDGestionDepartamento.buscarDepartamento(mod)
    print(f"ID: {datos[0]}")
    listanuevos.append(datos[0])
    opm = input(f"Desea modificar el Nombre {datos[1]}? (s/n): ")
    if opm.lower() == 's':
        nuevo_nombre = input("Ingrese el nuevo Nombre: ")
        listanuevos.append(nuevo_nombre)
    else:
        listanuevos.append(datos[1])
    opm = input(f"Desea modificar el Gerente {datos[2]}? (s/n): ")
    if opm.lower() == 's':
        nuevo_gerente = input("Ingrese el nuevo Gerente: ")
        listanuevos.append(nuevo_gerente)
    else:
        listanuevos.append(datos[2])
    DAO.CRUDGestionDepartamento.modificarDepartamento(Departamento(listanuevos[0], listanuevos[1], listanuevos[2]))

def eliminarDatosDepartamento():
    os.system("cls")
    print("==================================================")
    print("     E L I M I N A R  D E P A R T A M E N T O     ")
    print("==================================================")
    id = input("Ingrese ID del departamento a eliminar: ")
    DAO.CRUDGestionDepartamento.eliminarDepartamento(id)

#------------------------------------------------------------------------------------------------

# Funciones Empleado
def ingresarDatosEmpleado():
    os.system("cls")
    print("==============================================")
    print("       I N G R E S A R  E M P L E A D O       ")
    print("==============================================")
    id = input("Ingrese ID: ")
    nombre = input("Ingrese Nombre: ")
    apellido = input("Ingrese Apellido: ")
    correo = input("Ingrese Correo: ")
    telefono = input("Ingrese Fono: ")
    FechaContrato = input("Ingrese Fecha de Contrato (YYYY-MM-DD): ")
    salario = input("Ingrese Salario: ")
    e = Empleado(id, nombre, apellido, correo, telefono, FechaContrato, salario)
    DAO.CRUDGestionEmpleado.registrarEmpleado(e)

def mostrarDatosEmpleado():
    os.system("cls")
    print("==============================================================")
    print("      M O S T R A R  T O D O S  L O S  E M P L E A D O S      ")
    print("==============================================================")
    empleados = DAO.CRUDGestionEmpleado.mostrarEmpleado()
    for e in empleados:
        print(f"ID: {e[0]} | Nombre: {e[1]} | Apellido: {e[2]} | Correo: {e[3]} | Telefono: {e[4]} | FechaContrato: {e[5]} | Salario: {e[6]}")
    input("\n\n Presione Enter para continuar...")

def mostrarDatosEmpleadoEspecifico():
    os.system("cls")
    print("=========================================================")
    print("  M O S T R A R  E M P L E A D O  E S P E C I F I C O    ")
    print("=========================================================")
    id = input("Ingrese ID del empleado a buscar: ")
    e = DAO.CRUDGestionEmpleado.buscarEmpleado(id)
    if e:
        print(f"ID: {e[0]} | Nombre: {e[1]} | Apellido: {e[2]} | Correo: {e[3]} | Telefono: {e[4]} | FechaContrato: {e[5]} | Salario: {e[6]}")
    else:
        print("Empleado no encontrado.")
    input("\n\n Presione Enter para continuar...")

def mostrarDatosEmpleadoParcial():
    os.system("cls")
    print("=====================================================")
    print("   M O S T R A R  E M P L E A D O  P A R C I A L     ")
    print("=====================================================")
    cant = int(input("Ingrese la cantidad de empleados a mostrar: "))
    datos = DAO.CRUDGestionEmpleado.cosultaparcialEmpleado(cant)
    for e in datos:
        print(f"ID: {e[0]} | Nombre: {e[1]} | Apellido: {e[2]} | Correo: {e[3]} | Telefono: {e[4]} | FechaContrato: {e[5]} | Salario: {e[6]}")
    input("\n\n Presione Enter para continuar...")

def modificarDatosEmpleado():
    os.system("cls")
    listanuevos = []
    print("================================================")
    print("       M O D I F I C A R  E M P L E A D O       ")
    print("================================================")
    mostrarDatosEmpleado()
    mod = input("Ingrese el ID del empleado a modificar: ")
    datos = DAO.CRUDGestionEmpleado.buscarEmpleado(mod)
    print(f"ID: {datos[0]}")
    listanuevos.append(datos[0])
    opm = input(f"Desea modificar el Nombre {datos[1]}? (s/n): ")
    if opm.lower() == 's':
        nuevo_nombre = input("Ingrese el nuevo Nombre: ")
        listanuevos.append(nuevo_nombre)
    else:
        listanuevos.append(datos[1])
    opm = input(f"Desea modificar el Apellido {datos[2]}? (s/n): ")
    if opm.lower() == 's':
        nuevo_apellido = input("Ingrese el nuevo Apellido: ")
        listanuevos.append(nuevo_apellido)
    else:
        listanuevos.append(datos[2])
    opm = input(f"Desea modificar el Correo {datos[3]}? (s/n): ")
    if opm.lower() == 's':
        nuevo_correo = input("Ingrese el nuevo Correo: ")
        listanuevos.append(nuevo_correo)
    else:
        listanuevos.append(datos[3])
    opm = input(f"Desea modificar el Telefono {datos[4]}? (s/n): ")
    if opm.lower() == 's':
        nuevo_telefono = input("Ingrese el nuevo Telefono: ")
        listanuevos.append(nuevo_telefono)
    else:
        listanuevos.append(datos[4])
    opm = input(f"Desea modificar la Fecha de Contrato {datos[5]}? (s/n): ")
    if opm.lower() == 's':
        nueva_FechaContrato = input("Ingrese la nueva Fecha de Contrato (YYYY-MM-DD): ")
        listanuevos.append(nueva_FechaContrato)
    else:
        listanuevos.append(datos[5])
    opm = input(f"Desea modificar el Salario {datos[6]}? (s/n): ")
    if opm.lower() == 's':
        nuevo_salario = input("Ingrese el nuevo Salario: ")
        listanuevos.append(nuevo_salario)
    else:
        listanuevos.append(datos[6])
    DAO.CRUDGestionEmpleado.modificarEmpleado(Empleado(listanuevos[0], listanuevos[1], listanuevos[2], listanuevos[3], listanuevos[4], listanuevos[5], listanuevos[6]))

def eliminarDatosEmpleado():
    os.system("cls")
    print("============================================")
    print("       E L I M I N A R  E M P L E A D O     ")
    print("============================================")
    id = input("Ingrese ID del empleado a eliminar: ")
    DAO.CRUDGestionEmpleado.eliminarEmpleado(id)

#------------------------------------------------------------------------------------------------

# Funciones Proyecto
def ingresarDatosProyecto():
    os.system("cls")
    print("==============================================")
    print("       I N G R E S A R  P R O Y E C T O       ")
    print("==============================================")
    id = input("Ingrese ID: ")
    nombre = input("Ingrese Nombre: ")
    descripcion = input("Ingrese Descripcion: ")
    FechaInicio = input("Ingrese Fecha de Inicio (YYYY-MM-DD): ")
    p = Proyecto(id, nombre, descripcion, FechaInicio)
    DAO.CRUDGestionProyecto.registrarProyecto(p)

def mostrarDatosProyecto():
    os.system("cls")
    print("==============================================================")
    print("      M O S T R A R  T O D O S  L O S  P R O Y E C T O S      ")
    print("==============================================================")
    proyectos = DAO.CRUDGestionProyecto.mostrarProyecto()
    for p in proyectos:
        print(f"ID: {p[0]} | Nombre: {p[1]} | Descripcion: {p[2]} | FechaInicio: {p[3]}")
    input("\n\n Presione Enter para continuar...")

def mostrarDatosProyectoEspecifico():
    os.system("cls")
    print("=========================================================")
    print("  M O S T R A R  P R O Y E C T O  E S P E C I F I C O    ")
    print("=========================================================")
    id = input("Ingrese ID del proyecto a buscar: ")
    p = DAO.CRUDGestionProyecto.buscarProyecto(id)
    if p:
        print(f"ID: {p[0]} | Nombre: {p[1]} | Descripcion: {p[2]} | FechaInicio: {p[3]}")
    else:
        print("Proyecto no encontrado.")
    input("\n\n Presione Enter para continuar...")

def mostrarDatosProyectoParcial():
    os.system("cls")
    print("=====================================================")
    print("   M O S T R A R  P R O Y E C T O  P A R C I A L     ")
    print("=====================================================")
    cant = int(input("Ingrese la cantidad de proyectos a mostrar: "))
    datos = DAO.CRUDGestionProyecto.cosultaparcialProyecto(cant)
    for p in datos:
        print(f"ID: {p[0]} | Nombre: {p[1]} | Descripcion: {p[2]} | FechaInicio: {p[3]}")
    input("\n\n Presione Enter para continuar...")

def modificarDatosProyecto():
    os.system("cls")
    listanuevos = []
    print("================================================")
    print("       M O D I F I C A R  P R O Y E C T O       ")
    print("================================================")
    mostrarDatosProyecto()
    mod = input("Ingrese el ID del proyecto a modificar: ")
    datos = DAO.CRUDGestionProyecto.buscarProyecto(mod)
    print(f"ID: {datos[0]}")
    listanuevos.append(datos[0])
    opm = input(f"Desea modificar el Nombre {datos[1]}? (s/n): ")
    if opm.lower() == 's':
        nuevo_nombre = input("Ingrese el nuevo Nombre: ")
        listanuevos.append(nuevo_nombre)
    else:
        listanuevos.append(datos[1])
    opm = input(f"Desea modificar la Descripcion {datos[2]}? (s/n): ")
    if opm.lower() == 's':
        nueva_descripcion = input("Ingrese la nueva Descripcion: ")
        listanuevos.append(nueva_descripcion)
    else:
        listanuevos.append(datos[2])
    opm = input(f"Desea modificar la Fecha de Inicio {datos[3]}? (s/n): ")
    if opm.lower() == 's':
        nueva_FechaInicio = input("Ingrese la nueva Fecha de Inicio (YYYY-MM-DD): ")
        listanuevos.append(nueva_FechaInicio)
    else:
        listanuevos.append(datos[3])
    DAO.CRUDGestionProyecto.modificarProyecto(Proyecto(listanuevos[0], listanuevos[1], listanuevos[2], listanuevos[3]))

def eliminarDatosProyecto():
    os.system("cls")
    print("============================================")
    print("       E L I M I N A R  P R O Y E C T O     ")
    print("============================================")
    id = input("Ingrese ID del proyecto a eliminar: ")
    DAO.CRUDGestionProyecto.eliminarProyecto(id)

#------------------------------------------------------------------------------------------------

# Función Principal
def main():
    while True:
        menuPrincipal()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            # Lógica para ingresar datos
            menuIngresar()
            opcion_ingresar = int(input("Seleccione una opción: "))
            if opcion_ingresar == 1:
                # Lógica para ingresar departamento
                ingresarDatosDepartamento()
            if opcion_ingresar == 2:
                # Lógica para ingresar empleado
                ingresarDatosEmpleado()
            if opcion_ingresar == 3:
                # Lógica para ingresar proyecto
                ingresarDatosProyecto()
            if opcion_ingresar == 4:
                # Lógica para ingresar usuario
                ingresarDatosUsuario()
            if opcion_ingresar == 5:
                pass

        elif opcion == 2:
            # Lógica para mostrar datos
            menuMostrar()
            opcion_mostrar = int(input("Seleccione una opción: "))
            if opcion_mostrar == 1:
                # Lógica para mostrar departamento
                menuMostrarEspecifico()
                opcion_mostrar_departamento = int(input("Seleccione una opción: "))
                if opcion_mostrar_departamento == 1:
                    mostrarDatosDepartamento()
                elif opcion_mostrar_departamento == 2:
                    mostrarDatosDepartamentoEspecifico()
                elif opcion_mostrar_departamento == 3:
                    mostrarDatosDepartamentoParcial()
                elif opcion_mostrar_departamento == 4:
                    pass
            if opcion_mostrar == 2:
                # Lógica para mostrar empleado
                menuMostrarEspecifico()
                opcion_mostrar_empleado = int(input("Seleccione una opción: "))
                if opcion_mostrar_empleado == 1:
                    mostrarDatosEmpleado()
                elif opcion_mostrar_empleado == 2:
                    mostrarDatosEmpleadoEspecifico()
                elif opcion_mostrar_empleado == 3:
                    mostrarDatosEmpleadoParcial()
                elif opcion_mostrar_empleado == 4:
                    pass
            if opcion_mostrar == 3:
                # Lógica para mostrar proyecto
                menuMostrarEspecifico()
                opcion_mostrar_proyecto = int(input("Seleccione una opción: "))
                if opcion_mostrar_proyecto == 1:
                    mostrarDatosProyecto()
                elif opcion_mostrar_proyecto == 2:
                    mostrarDatosProyectoEspecifico()
                elif opcion_mostrar_proyecto == 3:
                    mostrarDatosProyectoParcial()
                elif opcion_mostrar_proyecto == 4:
                    pass
            if opcion_mostrar == 4:
                menuMostrarEspecifico()
                opcion_mostrar_usuario = int(input("Seleccione una opción: "))
                if opcion_mostrar_usuario == 1:
                    mostrarDatosUsuario()
                elif opcion_mostrar_usuario == 2:
                    mostrarDatosUsuarioEspecifico()
                elif opcion_mostrar_usuario == 3:
                    mostrarDatosUsuarioParcial()
                elif opcion_mostrar_usuario == 4:
                    pass

        elif opcion == 3:
            # Lógica para modificar datos
            menuModificar()
            opcion_modificar = int(input("Seleccione una opción: "))
            if opcion_modificar == 1:
                # Lógica para modificar departamento
                modificarDatosDepartamento()
            if opcion_modificar == 2:
                # Lógica para modificar empleado
                modificarDatosEmpleado()
            if opcion_modificar == 3:
                # Lógica para modificar proyecto
                modificarDatosProyecto()
            if opcion_modificar == 4:
                modificarDatosUsuario()

        elif opcion == 4:
            menuEliminar()
            opcion_eliminar = int(input("Seleccione una opción: "))
            if opcion_eliminar == 1:
                # Lógica para eliminar departamento
                eliminarDatosDepartamento()
            if opcion_eliminar == 2:
                # Lógica para eliminar empleado
                eliminarDatosEmpleado()
            if opcion_eliminar == 3:
                # Lógica para eliminar proyecto
                eliminarDatosProyecto()
            if opcion_eliminar == 4:
                eliminarDatosUsuario()
            
        elif opcion == 5:
            opcion2 = input("¿Está seguro que desea salir? (s/n): ")
            if opcion2.lower() == 's':
                print("Saliendo del programa...")
                exit()
        else:
            print("Opción inválida. Intente nuevamente.")

main()