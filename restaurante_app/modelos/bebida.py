from modelos.producto import Producto

class Bebida(Producto):
    """
    Representa una bebida disponible en el menú del restaurante.
    Hereda de la clase base Producto.
    """

    def __init__(self, nombre: str, precio: float, volumen_ml: int, disponible: bool = True) -> None:
        """
        Inicializa una nueva bebida llamando al constructor de la clase padre.

        Args:
            nombre (str): El nombre de la bebida.
            precio (float): El precio de la bebida.
            volumen_ml (int): El volumen en mililitros de la bebida (ml).
            disponible (bool): Indica la disponibilidad de la bebida.
        """
        # Uso de super() para inicializar atributos de la clase padre Producto
        super().__init__(nombre, precio, disponible)
        
        # Atributo específico de la clase Bebida
        self.volumen_ml: int = volumen_ml

    def mostrar_informacion(self) -> None:
        """
        Sobrescribe el método mostrar_informacion de la clase padre.
        Muestra la información de la bebida incluyendo su volumen.
        """
        estado: str = "Disponible" if self.disponible else "Agotado"
        # Acceso al precio encapsulado a través del método público obtener_precio()
        print(f"[Bebida]   {self.nombre:<25} | Precio: ${self.obtener_precio():.2f} | Volumen: {self.volumen_ml} ml | Estado: {estado}")
