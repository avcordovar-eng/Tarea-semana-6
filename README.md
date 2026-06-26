# Sistema de Gestión de Restaurante (POO en Python)

**Estudiante:** Alex Vinicio Cordova Romero  
**Materia:** Programación Orientada a Objetos  
**Institución:** Universidad Estatal Amazónica (UEA)  

---

## 1. Descripción del Sistema
Este proyecto consiste en una aplicación modular de consola desarrollada en Python que simula de forma simplificada el funcionamiento interno de un restaurante. El objetivo principal es demostrar la correcta aplicación de conceptos fundamentales de la Programación Orientada a Objetos (POO), tales como clases, objetos, constructores, métodos especiales, tipos de datos básicos y compuestos (listas), control de visibilidad/importaciones e identificadores descriptivos bajo el estándar PEP 8.

El sistema modela tres entidades esenciales:
- **Producto:** Representa cada platillo, bebida o postre disponible en el menú de alimentos, con su precio y estado de disponibilidad.
- **Cliente:** Modela la información de contacto y membresía de una persona registrada en la base de datos de clientes del restaurante.
- **Restaurante:** Actúa como el servicio/controlador del negocio, encargándose de agrupar y organizar las listas de productos y clientes utilizando métodos específicos para su administración.

---

## 2. Estructura del Proyecto
El proyecto sigue una estructura limpia, ordenada y modular para separar las responsabilidades del modelo de datos de la lógica de negocio y del punto de arranque:

```text
restaurante_app/
├── modelos/
│   ├── __init__.py      # Define la carpeta como paquete y documenta su propósito.
│   ├── producto.py      # Contiene la clase Producto (modelo del menú).
│   └── cliente.py       # Contiene la clase Cliente (modelo de usuarios).
├── servicios/
│   ├── __init__.py      # Define la carpeta como paquete de servicios.
│   └── restaurante.py   # Contiene la clase Restaurante (servicio/controlador).
└── main.py              # Punto de entrada principal (instanciación y prueba).
```

---

## 3. Tipos de Datos Utilizados en las Clases

A continuación, se detalla la firma de los atributos definidos en cada una de las clases, su tipo de dato y su propósito:

| Clase | Atributo | Tipo de Dato | Propósito |
| :--- | :--- | :--- | :--- |
| **`Producto`** | `nombre` | `str` | Nombre identificador del platillo o bebida. |
| | `precio` | `float` | Costo monetario unitario del producto. |
| | `categoria` | `str` | Clasificación gastronómica (ej. "Bebida", "Plato Fuerte"). |
| | `disponible` | `bool` | Estado lógico que indica si está disponible para pedidos. |
| **`Cliente`** | `nombre_completo` | `str` | Nombre y apellido del comensal. |
| | `correo_electronico`| `str` | Correo electrónico de contacto. |
| | `telefono` | `str` | Número telefónico de contacto. |
| | `es_frecuente` | `bool` | Estado lógico para indicar si forma parte del club VIP. |
| **`Restaurante`**| `nombre` | `str` | Nombre comercial del restaurante. |
| | `lista_productos` | `list[Producto]` | Colección compuesta que almacena objetos de tipo `Producto`. |
| | `lista_clientes` | `list[Cliente]` | Colección compuesta que almacena objetos de tipo `Cliente`. |

---

## 4. Reflexión sobre las Buenas Prácticas en Python

### La Importancia de los Identificadores Descriptivos
El uso de nombres significativos y autoexplicativos (como `nombre_completo` en lugar de `n`, o `lista_productos` en lugar de `l`) es indispensable para escribir un código mantenible y auto-documentado. Al seguir la convención de Python (PascalCase para clases y snake_case para variables/métodos), se reduce drásticamente la carga cognitiva de cualquier desarrollador que lea el código, permitiendo entender su funcionamiento a primera vista sin adivinar la utilidad de cada elemento.

### Tipos de Datos Adecuados
Utilizar los tipos nativos correctos (`float` para precios, `bool` para estados lógicos de disponibilidad o fidelidad y `str` para cadenas de texto) garantiza la integridad de los datos y previene errores en tiempo de ejecución. El tipado estático opcional (Type Hinting) introducido en las firmas de los métodos y constructores actúa como un contrato claro que formaliza cómo debe ser utilizada cada clase.

### Modularidad y el uso de Listas en Python
Dividir el proyecto en carpetas (`modelos` y `servicios`) evita el acoplamiento y promueve la reutilización del código. A su vez, el uso de colecciones compuestas como las **listas (`list`)** permite modelar relaciones de uno a muchos de forma natural y escalable (un restaurante tiene muchos productos y muchos clientes), facilitando operaciones de búsqueda, agregado y visualización dentro de un entorno estructurado.
