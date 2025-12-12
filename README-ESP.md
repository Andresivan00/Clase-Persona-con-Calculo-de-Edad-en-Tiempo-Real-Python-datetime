# Clase Persona con Cálculo de Edad en Tiempo Real (Python + datetime)

Ejemplo educativo y funcional de **Programación Orientada a Objetos** que crea una clase `Persona` capaz de almacenar datos personales y calcular automáticamente la **edad actual** usando la fecha del sistema.

### Qué hace exactamente este código
- Define una clase `Persona` con los atributos:
  - Nombre, apellido, cédula, año de nacimiento, país y género
- Usa la librería `datetime` para obtener el **año actual** automáticamente
- Incluye dos métodos útiles:
  - `.imprimir()` → muestra toda la información de la persona de forma bonita
  - `.calcularEdad()` → resta el año actual al año de nacimiento y devuelve la edad real
- Crea un objeto de ejemplo y muestra sus datos + edad en pantalla
