from modelos.producto import Producto

class Platillo(Producto):
    """
    Representa un platillo o comida específica en el menú del restaurante.
    Hereda de la clase base Producto.
    """

    def __init__(self, nombre: str, precio: float, calorias: int, disponible: bool = True) -> None:
        """
        Inicializa un nuevo platillo llamando al constructor de la clase padre.

        Args:
            nombre (str): El nombre del platillo.
            precio (float): El precio del platillo.
            calorias (int): Las calorías del platillo (en kcal).
            disponible (bool): Indica la disponibilidad del platillo.
        """
        # Uso de super() para inicializar atributos de la clase padre Producto
        super().__init__(nombre, precio, disponible)
        
        # Atributo específico de la clase Platillo
        self.calorias: int = calorias

    def mostrar_informacion(self) -> None:
        """
        Sobrescribe el método mostrar_informacion de la clase padre.
        Muestra la información del platillo incluyendo su aporte calórico.
        """
        estado: str = "Disponible" if self.disponible else "Agotado"
        # Acceso al precio encapsulado a través del método público obtener_precio()
        print(f"[Platillo] {self.nombre:<25} | Precio: ${self.obtener_precio():.2f} | Calorías: {self.calorias} kcal | Estado: {estado}")
