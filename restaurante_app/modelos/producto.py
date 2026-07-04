class Producto:
    """
    Clase padre que representa un producto general en el menú del restaurante.
    """

    def __init__(self, nombre: str, precio: float, disponible: bool = True) -> None:
        """
        Inicializa un nuevo producto con su nombre, precio y disponibilidad.

        Args:
            nombre (str): El nombre del producto.
            precio (float): El precio de venta del producto (debe ser mayor a cero).
            disponible (bool): Indica si el producto está disponible actualmente en el menú.
        """
        self.nombre: str = nombre
        self.disponible: bool = disponible
        
        # Validación del precio en el constructor
        if precio <= 0:
            raise ValueError("El precio inicial debe ser un valor estrictamente mayor a cero.")
        
        # Atributo encapsulado (privado con doble guion bajo)
        self.__precio: float = precio

    def obtener_precio(self) -> float:
        """
        Método de acceso (getter) para retornar el precio encapsulado del producto.

        Returns:
            float: El precio del producto.
        """
        return self.__precio

    def cambiar_precio(self, nuevo_precio: float) -> None:
        """
        Método de modificación (setter) para cambiar el precio con validación.

        Args:
            nuevo_precio (float): El nuevo precio a asignar (debe ser mayor a cero).
        """
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser un valor estrictamente mayor a cero (no puede ser negativo ni cero).")
        self.__precio = nuevo_precio

    def mostrar_informacion(self) -> None:
        """
        Muestra en consola la información básica del producto.
        Diseñado para ser sobrescrito por las subclases demostrando polimorfismo.
        """
        estado: str = "Disponible" if self.disponible else "Agotado"
        print(f"Producto: {self.nombre:<25} | Precio: ${self.__precio:.2f} | Estado: {estado}")
