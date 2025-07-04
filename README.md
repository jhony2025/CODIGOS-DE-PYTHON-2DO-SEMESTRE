# Sistema de Gestión de Biblioteca – Aplicación de POO en Python

## Autor
**Johnny Vera**  
Estudiante de programación – Proyecto de Programación Orientada a Objetos (POO) en Python


## Objetivo del Proyecto

Este programa tiene como objetivo demostrar la aplicación de los conceptos fundamentales de la **Programación Orientada a Objetos (POO)** en el lenguaje **Python**, incluyendo:

- **Definición de clases y objetos**
- **Herencia**
- **Encapsulación**
- **Polimorfismo**

Fue desarrollado en el entorno de desarrollo **PyCharm** y subido a este repositorio como parte de una entrega académica.

## Tecnologías Utilizadas

- Python 3.x
- PyCharm (IDE)
- Git y GitHub

## Descripción del Programa

El programa simula un **Sistema de Gestión de Biblioteca**, donde se manejan bibliotecarios, usuarios y libros. A través de diferentes clases se aplican los principios de la POO:

### Clases y Funcionalidades

- **Clase `Persona`**  
  Clase base que contiene los atributos `nombre` e `identificación`.

- **Clase `Bibliotecario` (hereda de `Persona`)**  
  Representa al encargado de una sección de la biblioteca. En este caso, el bibliotecario es **Johnny Vera**, quien está a cargo de la sección de Tecnología.

- **Clase `Usuario` (hereda de `Persona`)**  
  Representa a los lectores registrados en la biblioteca, incluyendo información como nombre, ID y correo electrónico.

- **Clase `Libro`**  
  Aplica **encapsulación** mediante atributos privados (`__titulo`, `__autor`, `__isbn`). Esta clase representa los libros disponibles en el sistema.

### Aplicación de Conceptos POO

| Concepto | Aplicación |
|----------|------------|
| **Herencia** | `Bibliotecario` y `Usuario` heredan de `Persona` |
| **Encapsulación** | Los atributos de la clase `Libro` son privados |
| **Polimorfismo** | El método `mostrar_info()` se comporta de forma distinta en cada clase hija |

## Ejecución del Programa

El programa crea instancias reales con los siguientes datos:

- Bibliotecario: `Johnny Vera`, ID: `B007`, Sección: `Tecnología`
- Usuario: `Ana Torres`, ID: `U123`, Correo: `ana.torres@gmail.com`
- Libro: `"Python para Todos"` por `Charles Severance`, ISBN: `9781492339243`

Cada objeto muestra su información con el método `mostrar_info()` adaptado a su tipo.

## Cómo ejecutar este proyecto

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
