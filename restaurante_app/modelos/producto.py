class Producto:
    """
    Representa un plato, bebida o producto disponible en el menú del restaurante.
    """

    def __init__(self, nombre: str, precio: float, categoria: str, disponible: bool = True) -> None:
        """
        Inicializa un nuevo producto con su nombre, precio, categoría y disponibilidad.
        
        Args:
            nombre (str): El nombre del producto.
            precio (float): El precio de venta del producto.
            categoria (str): La categoría a la que pertenece (ej. Plato Fuerte, Bebida).
            disponible (bool): Indica si el producto está disponible actualmente en el menú.
        """
        self.nombre: str = nombre
        self.precio: float = precio
        self.categoria: str = categoria
        self.disponible: bool = disponible

    def actualizar_disponibilidad(self, disponible: bool) -> None:
        """
        Actualiza el estado de disponibilidad de un producto.
        
        Args:
            disponible (bool): El nuevo estado de disponibilidad.
        """
        self.disponible = disponible

    def __str__(self) -> str:
        """
        Retorna una representación del producto como una cadena de texto.
        
        Returns:
            str: Una cadena formateada con los datos del producto.
        """
        estado: str = "Disponible" if self.disponible else "Agotado"
        return f"[{self.categoria}] {self.nombre} - ${self.precio:.2f} ({estado})"
