"""
Punto de entrada principal del sistema de gestión de restaurante.

Este archivo se encarga de:
1. Importar los modelos y el servicio del restaurante.
2. Instanciar y configurar el objeto principal de tipo Restaurante.
3. Crear objetos de prueba para los modelos Producto y Cliente.
4. Agregar los objetos creados a las listas de gestión del restaurante.
5. Invocar los métodos para mostrar la información registrada en la consola.
"""

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def ejecutar_demostracion() -> None:
    """
    Función que orquesta la creación y visualización de los datos del restaurante.
    """
    # 1. Instanciación del servicio principal del restaurante
    mi_restaurante = Restaurante("El Rincón de Alex")

    # 2. Creación de al menos dos objetos del modelo Producto
    # Producto 1: Un plato fuerte disponible
    plato_principal = Producto(
        nombre="Lomo Saltado con Papas",
        precio=12.50,
        categoria="Plato Fuerte",
        disponible=True
    )
    
    # Producto 2: Una bebida disponible
    bebida_refrescante = Producto(
        nombre="Jugo Natural de Maracuyá",
        precio=2.75,
        categoria="Bebida",
        disponible=True
    )

    # Producto 3: Un postre que no está disponible temporalmente
    postre_delicioso = Producto(
        nombre="Tarta de Tres Leches con Canela",
        precio=4.50,
        categoria="Postre",
        disponible=False
    )

    # 3. Creación de al menos dos objetos del modelo Cliente
    # Cliente 1: Cliente registrado y frecuente (Estudiante que desarrolla la tarea)
    cliente_estudiante = Cliente(
        nombre_completo="Alex Vinicio Cordova Romero",
        correo_electronico="alex.cordova@uea.edu.ec",
        telefono="0987654321",
        es_frecuente=True
    )

    # Cliente 2: Cliente regular registrado
    cliente_regular = Cliente(
        nombre_completo="María Celeste Espinoza",
        correo_electronico="maria.celeste@outlook.com",
        telefono="0991234567",
        es_frecuente=False
    )

    # 4. Registro de los productos creados en el servicio del restaurante
    mi_restaurante.registrar_producto(plato_principal)
    mi_restaurante.registrar_producto(bebida_refrescante)
    mi_restaurante.registrar_producto(postre_delicioso)

    # 5. Registro de los clientes creados en el servicio del restaurante
    mi_restaurante.registrar_cliente(cliente_estudiante)
    mi_restaurante.registrar_cliente(cliente_regular)

    # 6. Presentación ordenada de los datos en la consola
    print("\n" + "#" * 60)
    print("       SISTEMA MODULAR DE GESTIÓN DE RESTAURANTE - UEA")
    print("#" * 60)
    
    # Mostrar el menú de comida y bebida registrado
    mi_restaurante.mostrar_menu()
    
    # Mostrar la base de clientes registrados
    mi_restaurante.mostrar_clientes()
    
    print("\n" + "#" * 60)
    print("           DEMOSTRACIÓN DE EJECUCIÓN CON EXITO")
    print("#" * 60 + "\n")

if __name__ == "__main__":
    ejecutar_demostracion()
