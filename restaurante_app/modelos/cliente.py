class Cliente:
    """
    Representa a un cliente registrado en el sistema del restaurante.
    """

    def __init__(self, nombre_completo: str, correo_electronico: str, telefono: str, es_frecuente: bool = False) -> None:
        """
        Inicializa un nuevo cliente con sus datos de contacto y estado de fidelidad.
        
        Args:
            nombre_completo (str): El nombre y apellido del cliente.
            correo_electronico (str): La dirección de correo electrónico del cliente.
            telefono (str): El número de teléfono de contacto.
            es_frecuente (bool): Indica si el cliente es considerado un cliente habitual o VIP.
        """
        self.nombre_completo: str = nombre_completo
        self.correo_electronico: str = correo_electronico
        self.telefono: str = telefono
        self.es_frecuente: bool = es_frecuente

    def cambiar_estado_frecuente(self, es_frecuente: bool) -> None:
        """
        Actualiza el estado de cliente frecuente en el sistema.
        
        Args:
            es_frecuente (bool): El nuevo estado de fidelidad.
        """
        self.es_frecuente = es_frecuente

    def __str__(self) -> str:
        """
        Retorna una representación en texto del cliente.
        
        Returns:
            str: Los datos del cliente formateados como una cadena.
        """
        tipo_cliente: str = "Frecuente" if self.es_frecuente else "Regular"
        return f"{self.nombre_completo} ({tipo_cliente}) - Correo: {self.correo_electronico} | Teléfono: {self.telefono}"
