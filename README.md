# Sistema de Gestión de Restaurante (POO en Python - Versión Mejorada)

**Estudiante:** Alex Vinicio Cordova Romero  
**Materia:** Programación Orientada a Objetos  
**Institución:** Universidad Estatal Amazónica (UEA)  

---

## 1. Descripción del Sistema
Este proyecto consiste en una aplicación modular de consola desarrollada en Python que simula de forma simplificada el funcionamiento interno de un restaurante, centrándose especialmente en el menú de productos. El objetivo principal es demostrar la correcta aplicación de conceptos fundamentales y avanzados de la Programación Orientada a Objetos (POO), tales como **Herencia**, **Encapsulación** y **Polimorfismo**, bajo el estándar PEP 8 y con tipado de datos (Type Hinting).

---

## 2. Estructura del Proyecto
El proyecto sigue una estructura limpia, ordenada y modular para separar las responsabilidades del modelo de datos de la lógica de negocio y del punto de arranque:

```text
restaurante_app/
├── modelos/
│   ├── __init__.py      # Define la carpeta como paquete.
│   ├── producto.py      # Clase padre Producto con atributos y métodos comunes.
│   ├── platillo.py      # Clase hija Platillo (hereda de Producto).
│   └── bebida.py        # Clase hija Bebida (hereda de Producto).
├── servicios/
│   ├── __init__.py      # Define la carpeta como paquete de servicios.
│   └── restaurante.py   # Clase Restaurante (gestiona y muestra el menú).
└── main.py              # Punto de entrada principal (instanciación, pruebas y demostración).
```

---

## 3. Relación de Herencia Aplicada
Se implementó una jerarquía de clases para modelar los productos disponibles en el menú del restaurante:
- **`Producto` (Superclase / Clase Padre):** Contiene los atributos y comportamientos comunes a todos los productos (`nombre`, `disponible` y el precio protegido).
- **`Platillo` (Subclase / Clase Hija):** Hereda de `Producto` utilizando la función `super().__init__(nombre, precio, disponible)` y añade el atributo especializado `calorias` (tipo `int`).
- **`Bebida` (Subclase / Clase Hija):** Hereda de `Producto` utilizando la función `super().__init__(nombre, precio, disponible)` y añade el atributo especializado `volumen_ml` (tipo `int`).

---

## 4. Atributo Encapsulado y Validaciones
Para demostrar la protección de los datos internos y evitar estados inválidos:
- **Atributo Encapsulado:** El precio del producto está definido como un atributo privado (`__precio`) en la clase `Producto`. Esto impide que sea accedido o modificado directamente desde fuera de la clase.
- **Métodos de Acceso (Getter):** Se implementó el método `obtener_precio()` para retornar el valor de `__precio`.
- **Método de Modificación (Setter):** Se implementó el método `cambiar_precio(nuevo_precio)` que actúa como filtro seguro.
- **Validación:** El setter y el constructor de la clase `Producto` verifican que el precio sea mayor a cero (`nuevo_precio <= 0` lanza un `ValueError`). De esta manera, se impide registrar productos con precios gratuitos, negativos o inválidos.

---

## 5. Demostración de Polimorfismo
El polimorfismo se aplica mediante la sobrescritura del método `mostrar_informacion()`:
- La clase padre `Producto` define una implementación base de `mostrar_informacion()`.
- Las clases hijas `Platillo` y `Bebida` sobrescriben (`override`) este método para incorporar detalles específicos (calorías para `Platillo` y volumen en mililitros para `Bebida`).
- En la clase de servicio `Restaurante`, el método `mostrar_menu()` recorre una lista genérica de objetos de tipo `Producto` y ejecuta `producto.mostrar_informacion()`. En tiempo de ejecución, Python determina dinámicamente qué método invocar según la clase concreta de la instancia real (`Platillo` o `Bebida`), logrando un comportamiento polimórfico limpio y escalable.

---

## 6. Reflexión sobre la POO en Proyectos Modulares
La Programación Orientada a Objetos aplicada a proyectos de software modulares en Python ofrece grandes ventajas:
1. **Mantenibilidad y Escalabilidad:** Al separar las clases en archivos independientes y paquetes (`modelos/` y `servicios/`), es sumamente sencillo agregar nuevos tipos de productos (por ejemplo, `Postre`) sin alterar el funcionamiento de los productos existentes o la lógica de servicios.
2. **Reutilización del Código:** La herencia evita duplicar código común (como la lógica del nombre, disponibilidad y precio), reduciendo la posibilidad de bugs.
3. **Robustez mediante Encapsulación:** Validar datos en un único punto (los setters) protege la lógica de negocio, asegurando que las reglas del negocio del restaurante (como precios no negativos o iguales a cero) se cumplan estrictamente a lo largo de todo el ciclo de vida del software.
