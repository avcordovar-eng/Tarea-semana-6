"""
Punto de entrada principal del sistema restaurante_app.

Este archivo se encarga de:
1. Importar las subclases Platillo y Bebida, y el servicio Restaurante.
2. Instanciar y configurar el objeto principal del restaurante.
3. Crear objetos de prueba (dos Platillos y dos Bebidas).
4. Demostrar la encapsulación del precio, validando que no sea cero ni negativo.
5. Agregar los objetos creados al servicio.
6. Invocar los métodos del servicio para mostrar los productos de manera polimórfica en consola.
"""

from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def ejecutar_demostracion() -> None:
    """
    Función que orquesta la creación de objetos, pruebas de encapsulación
    y la visualización polimórfica del menú del restaurante.
    """
    # 1. Instanciación del servicio principal
    mi_restaurante = Restaurante("El Rincón de Alex")

    # 2. Creación de objetos de tipo Platillo (Comidas)
    platillo_1 = Platillo(
        nombre="Lomo Saltado con Papas",
        precio=12.50,
        calorias=720,
        disponible=True
    )
    
    platillo_2 = Platillo(
        nombre="Ceviche Mixto Especial",
        precio=15.00,
        calorias=480,
        disponible=True
    )

    # 3. Creación de objetos de tipo Bebida (Líquidos)
    bebida_1 = Bebida(
        nombre="Jugo de Maracuyá (Fruta)",
        precio=2.50,
        volumen_ml=400,
        disponible=True
    )
    
    bebida_2 = Bebida(
        nombre="Chicha Morada Clásica",
        precio=3.00,
        volumen_ml=500,
        disponible=True
    )

    # 4. Demostración de Encapsulación: Acceso y modificación del precio con validación
    print("\n" + "=" * 80)
    print("        DEMOSTRACIÓN DE ENCAPSULACIÓN Y VALIDACIONES DE PRECIO")
    print("=" * 80)
    
    # Lectura del precio usando el getter obtener_precio()
    print(f"Producto: '{platillo_1.nombre}'")
    print(f" -> Precio original (obtenido con getter): ${platillo_1.obtener_precio():.2f}")
    
    # Modificación exitosa usando el setter cambiar_precio()
    nuevo_precio_valido = 13.99
    platillo_1.cambiar_precio(nuevo_precio_valido)
    print(f" -> Precio actualizado con éxito (setter):  ${platillo_1.obtener_precio():.2f}")
    
    # Intento de asignación con valor negativo (debe fallar y lanzar ValueError)
    try:
        print(" -> Intentando cambiar precio a un valor negativo (-2.50)...")
        platillo_1.cambiar_precio(-2.50)
    except ValueError as error:
        print(f"    [ERROR CAPTURADO DE FORMA CORRECTA]: {error}")
        
    # Intento de asignación con valor igual a cero (debe fallar y lanzar ValueError)
    try:
        print(" -> Intentando cambiar precio a cero (0.00)...")
        platillo_1.cambiar_precio(0.00)
    except ValueError as error:
        print(f"    [ERROR CAPTURADO DE FORMA CORRECTA]: {error}")
    
    print("=" * 80)

    # 5. Agregar los objetos creados a la lista administrada por Restaurante
    mi_restaurante.registrar_producto(platillo_1)
    mi_restaurante.registrar_producto(platillo_2)
    mi_restaurante.registrar_producto(bebida_1)
    mi_restaurante.registrar_producto(bebida_2)

    # 6. Mostrar el menú polimórfico en consola
    mi_restaurante.mostrar_menu()

    print("\n" + "#" * 90)
    print("         DEMOSTRACIÓN DE EJECUCIÓN CON EXITO (POO Python - Alex Cordova)")
    print("#" * 90 + "\n")

if __name__ == "__main__":
    ejecutar_demostracion()
