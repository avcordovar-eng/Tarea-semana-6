from modelos.producto import Producto

class Restaurante:
    """
    Clase de servicio encargada de gestionar los productos del menú del restaurante.
    """

    def __init__(self, nombre: str) -> None:
        """
        Inicializa un nuevo restaurante con su nombre y una lista vacía de productos.

        Args:
            nombre (str): El nombre comercial del restaurante.
        """
        self.nombre: str = nombre
        # Lista compuesta para almacenar los objetos de tipo Producto (Platillo o Bebida)
        self.lista_productos: list[Producto] = []

    def registrar_producto(self, producto: Producto) -> None:
        """
        Registra un nuevo producto (platillo o bebida) en la lista del restaurante.

        Args:
            producto (Producto): El producto a registrar.
        """
        self.lista_productos.append(producto)

    def mostrar_menu(self) -> None:
        """
        Muestra en consola el menú completo del restaurante de forma formateada.
        Demuestra polimorfismo al recorrer la lista de productos y llamar al
        método mostrar_informacion() de cada objeto, el cual se ejecuta según
        la clase real a la que pertenezca (Platillo o Bebida).
        """
        print(f"\n==========================================================================================")
        print(f"                              MENÚ OFICIAL: {self.nombre.upper()}                          ")
        print(f"==========================================================================================")
        if not self.lista_productos:
            print("   No hay productos registrados en el menú actualmente.")
        else:
            for producto in self.lista_productos:
                print(" • ", end="")
                # Demostración de Polimorfismo: llamada dinámica según el tipo real
                producto.mostrar_informacion()
        print(f"==========================================================================================")
