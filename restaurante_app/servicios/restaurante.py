from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """
    Clase de servicio encargada de gestionar los productos del menú y el registro de clientes.
    """

    def __init__(self, nombre: str) -> None:
        """
        Inicializa un nuevo restaurante con su nombre y listas vacías para productos y clientes.
        
        Args:
            nombre (str): El nombre comercial del restaurante.
        """
        self.nombre: str = nombre
        # Lista compuesta para almacenar los objetos de tipo Producto
        self.lista_productos: list[Producto] = []
        # Lista compuesta para almacenar los objetos de tipo Cliente
        self.lista_clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto) -> None:
        """
        Registra un nuevo producto en la lista del restaurante.
        
        Args:
            producto (Producto): El producto a registrar.
        """
        self.lista_productos.append(producto)

    def registrar_cliente(self, cliente: Cliente) -> None:
        """
        Registra un nuevo cliente en el sistema del restaurante.
        
        Args:
            cliente (Cliente): El cliente a registrar.
        """
        self.lista_clientes.append(cliente)

    def mostrar_menu(self) -> None:
        """
        Muestra en consola el menú actual del restaurante de forma formateada.
        """
        print(f"\n==================================================")
        print(f"            MENÚ DE: {self.nombre.upper()}         ")
        print(f"==================================================")
        if not self.lista_productos:
            print("   No hay productos registrados en el menú actualmente.")
        else:
            for producto in self.lista_productos:
                print(f" • {producto}")
        print(f"==================================================")

    def mostrar_clientes(self) -> None:
        """
        Muestra en consola la lista de clientes registrados en el sistema.
        """
        print(f"\n==================================================")
        print(f"          CLIENTES REGISTRADOS EN EL SISTEMA       ")
        print(f"==================================================")
        if not self.lista_clientes:
            print("   No hay clientes registrados en el sistema actualmente.")
        else:
            for cliente in self.lista_clientes:
                print(f" • {cliente}")
        print(f"==================================================")
