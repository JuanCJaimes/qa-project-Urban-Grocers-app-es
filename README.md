# Urban Grocers: Automatización de Pruebas de Creación de Kits de Productos

## Descripción del Proyecto

Este proyecto automatiza las pruebas para la funcionalidad de creación de kits de productos en la API de **Urban Grocers**, una aplicación diseñada para facilitar la gestión de compras y organización de productos. 

### Propósito
- Probar que la API permite la creación de kits de productos siguiendo los parámetros definidos en la documentación.
- Identificar posibles errores en el campo `name` durante la solicitud de creación de un kit.

### Problema que Resuelve
La creación de kits en la API debe cumplir con restricciones específicas para garantizar la integridad de los datos. Este proyecto asegura que:
- Los nombres de los kits cumplen con las reglas de longitud, caracteres permitidos y tipo de datos.
- Los errores son correctamente manejados por la API.

### Funcionalidades Principales
- Automatización de pruebas con `pytest`.
- Verificación de restricciones en el campo `name`:
  - Longitud mínima y máxima.
  - Aceptación de caracteres especiales, números y espacios.
  - Gestión de errores cuando el campo está vacío, no es enviado o tiene un tipo de dato incorrecto.

---

## Tecnologías Utilizadas

- **Lenguajes de Programación**: Python 3.8+
- **Frameworks de Pruebas**: pytest
- **Librerías**: requests
- **Control de Versiones**: Git y GitHub

---

## Instrucciones para Ejecutar el Proyecto

### 1. Instalación de Dependencias
1. Asegúrate de tener Python 3.8 o superior instalado. Verifica la versión con:
   ```bash
   python3 --version

