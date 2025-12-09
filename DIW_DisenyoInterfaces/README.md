# REPOSITORIO DE PRÁCTICAS DE "MODULO DE DISEÑO DE INTERFACES WEB"

## [EJERCICIOS](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/tree/08ddc8b240bcf893f1c46da7f01fd12b384c98a6/DIW_DisenyoInterfaces/Ejercicios)

>Dentro de esta carpeta encontraremos todos los ejercicios que hemos hecho hasta el momento enumerados desde el más antiguo al más reciente.>

## [01-Primer Ejercicio](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/tree/85d52073564aef25469bbe51d9c5897e330641d8/DIW_DisenyoInterfaces/Ejercicios/01_PrimerEjercicio)

### DESCRIPCIÓN:

Ejercicio práctico que consiste en usar las diferentes etiquetas para centrar imagenes con enlaces, hacer listas numeradas y no numeradas, y crear tablas manejando el espacio de las columnas y filas a traves de sus atributos (colspan, rowspan).

### RESULTADO:

![imagen_resultado1](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/blob/main/DIW_DisenyoInterfaces/Ejercicios/01_PrimerEjercicio/img/Resultado_Ejercicio1.png?raw=true)

## [02-Segundo Ejercicio](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/tree/fbde076e73dc9dfd314a8676b65eac818a0aef6e/DIW_DisenyoInterfaces/Ejercicios/02_SegundoEjercicio)

### DESCRIPCIÓN:

Ejercicio practico que consiste en crear un formulario y utilizar las etiquetas propias dentro de este (legend, label, fieldset, etc). Además de utilizar más el css para posicionar los elementos de la manera deseada y con los colores especificados.

### RESULTADO:

![imagen_resultado2](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/blob/main/DIW_DisenyoInterfaces/Ejercicios/02_SegundoEjercicio/img/Resultado_Ejercicio2.png?raw=true)

## [03-Tercer Ejercicio](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/blob/fbde076e73dc9dfd314a8676b65eac818a0aef6e/DIW_DisenyoInterfaces/Ejercicios/03_TercerEjercicioSelectores)

### DESCRIPCIÓN:

Este ejercicio consiste en crear una página web con dos tablas, la diferencia es que utilizaremos selectores para aplicar los estilos, además de usar algunas etiquetas nuevas como "span".


### RESULTADO:

![imagen_resultado3](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/blob/main/DIW_DisenyoInterfaces/Ejercicios/03_TercerEjercicioSelectores/img/Resultado_Ejercicio3.png?raw=true)

>Nota: Este ejercicio tiene una hoja de estilos separada del html. En estos casos se utiliza en el head la etiqueta "link" para conectar con la hoja de estilos y llamar a las clases o id's.

## [04-Cuarto Ejercicio - Maquetación Clasica](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/tree/fbde076e73dc9dfd314a8676b65eac818a0aef6e/DIW_DisenyoInterfaces/Ejercicios/04_MaquetacionClasica)

### DESCRIPCIÓN:

En este ejercicio el objetivo es crear una página web utilizando todas las etiquetas de maquetación clásica, antes de flexbox y grid.

Las etiquetas que usamos en esta página web fueron:


    >DISPLAY
    -inline
    -inline block
    -block

    >LAYOUT
    -fixed
    -elastic
    -fluid
    -hibrido

    >BOX-SIZING
    -border-box

    >CENTRADO
    -horizontal-inline
    -horizontal-bloque
    -vertical-inline
    -vertical-bloque

    >POSITION
    -static
    -relative
    -fixed
    -absolute
    -sticky
    -z-index

    >COLUMNAS
    -column-count
    -column-gap
    -column-rule

    >FLOTANTES
    -float:left
    -float:right
    -clear:both
    -clearfix hack

### RESULTADO:

![imagen_resultado4](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/blob/main/DIW_DisenyoInterfaces/Ejercicios/04_MaquetacionClasica/img/Resultado_Ejercicio4.png?raw=true)

### CODIGO:

Un pequeño ejemplo del css utilizado:

```css
* {
  /* Usamos border-box en todo para que las 5 tarjetas esten en fila*/
  box-sizing: border-box;
}

body {
  margin: 0;
  min-height: 100vh;
  font-family: Arial, sans-serif;
  background: linear-gradient(to right bottom, #2c3e50, #276e9d);

  /* El body es 'relative' para que 'absolute' del wrapper funcione */
  position: relative;
}


/*---------ENCABEZADO-----------*/
header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 60px;
  background: rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(10px);
  padding: 20px 5%;

  /* z-index: 10 lo pone en una capa alta */
  z-index: 10;
}

header h1 {
  margin: 0;
  font-size: 1.5rem;
  color: white;
  /* Por defecto, 'h1' es 'block' */
}


/* --- CONTENEDOR= Es en el que estarán todas las cosas y las organizará --- */
.contenedor {
  width: 90%;
  max-width: 1600px;

  /* Centrado 'absolute' horizontal y vertical */
  position: absolute;
  top: 54%;
  left: 50%;
  transform: translate(-50%, -50%);

  z-index: 5;
}

.contenedor::after {
  content: "";
  display: table;
  clear: both;
}

/* --- TARJETAS (float: left) --- */
.card {
  background-color: #e0e0e0;
  border-radius: 16px;
  padding: 20px;
  height: 590px;

  float: left;
  width: 19.1%;
  margin-right: 1.125%;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);

}

.card:last-child {
  margin-right: 0;
}
```

## [05-Quinto Ejercicio - Maquetación Flex-Grid](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/tree/fbde076e73dc9dfd314a8676b65eac818a0aef6e/DIW_DisenyoInterfaces/Ejercicios/05_MaquetacionFlexGrid)

### DESCRIPCIÓN:

En esta carpeta encontraras una serie de ejercicios utilizando maquetación con Flexbox y Grid, creando barras de navegación, alineando imagenes con flexbox, utilizando grid para crear figuras o distribuir el espacio por medio de columnas, etc.

### ALGUNOS RESULTADOS:

![imagen_resultadoEjercicios5](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/blob/main/DIW_DisenyoInterfaces/Ejercicios/05_MaquetacionFlexGrid/img/Resultado_Ejercicios5.png?raw=true)


## [06-Sexto Ejercicio - Web Responsive](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/tree/5bf5aa4219c86edebdd2a5d4bc2914780e3658bf/DIW_DisenyoInterfaces/Ejercicios/06_WebResponsive)

### DESCRIPCIÓN:

En este ejercicio se propone hacer una web al gusto, pero esta web debe tener una nueva función css llamada media-querys. Con estas funcionalidades podemos definir como va a responder nuestro sitio web dependiendo del tamaño del dispositivo en el que se abra.

### EJEMPLO DE MEDIA-QUERY:

```css
  @media (max-width: 1385px) {

  .card {
    flex-basis: calc(50% - 7.5px);
  }

  .card h1 {
    font-size: 1.8em;
  }

  .imagenTarjeta {
    height: 300px;      /* <-- 1. Le da una altura fija en píxeles */
    object-fit: cover; /* <-- 2. Evita que la imagen se distorsione */

  }
}
```

### RESULTADO:

![imagen_resultadoEjercicios6](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/blob/main/DIW_DisenyoInterfaces/Ejercicios/06_WebResponsive/img/Resultado_Ejercicio6.png?raw=true)

## [07-Septimo Ejercicio - Inicio con Sass](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/tree/5bf5aa4219c86edebdd2a5d4bc2914780e3658bf/DIW_DisenyoInterfaces/Ejercicios/07_SCSS)

### DESCRIPCIÓN:

En este ejercicio empezamos a utilizar el procesador de css "Sass", que nos permitirá facilitar muchas cosas dentro de nuestras hojas de estilo, ya que nos permite crear variables en las que podemos añadir cosas y llamarlas en cualquier lugar de nuestro documento. En este ejercicio solo exploramos como funciona.

### COMO USAR SASS:

Para empezar a utilizar Sass primero debemos instalarlo, se puede hacer con los siguientes comandos:

```cmd
  npm install -g sass
  choco install sass
```

Para comprobar que la instalación fue correcta utilizamos:

```cmd
  sass --version
```

## [08-Octavo Ejercicio - Conociendo Sass](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/tree/5bf5aa4219c86edebdd2a5d4bc2914780e3658bf/DIW_DisenyoInterfaces/Ejercicios/08_Ejercicio1_Sass)

### DESCRIPCIÓN:

Este ejercicio consiste en conocer y utilizar la herramienta Sass de forma eficiente, creando las variables necesarias para nuestra web, que es sencilla, con un menú en la parte superior y dos imagenes alineadas.

### RESULTADO:

![imagen_resultadoEjercicios8](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/blob/main/DIW_DisenyoInterfaces/Ejercicios/08_Ejercicio1_Sass/img/Ejercicio_Resultado.png?raw=true)

## [09-Noveno Ejercicio - ](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/tree/74e468647da8933fd7cb0ee146ec787ef5bdc3ef/DIW_DisenyoInterfaces/Ejercicios/09_Ejercicio2_EstructurasDeControlSass)

### DESCRIPCIÓN:

Este ejercicio consiste en utilizar todas las herramientas que conocemos para crear una web, usamos:

* Variables
* Mixin -> Para no redundar en codigo.
* SassDocs -> Para comentar los grupos de variables, las diferentes funciones y qué hacen, además de especificar al autor del codigo.

### RESULTADO:

![imagen_resultadoEjercicios9](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/blob/main/DIW_DisenyoInterfaces/Ejercicios/09_Ejercicio2_EstructurasDeControlSass/img/Resultado_ejercicio9.png?raw=true)

## [09-Noveno Ejercicio - Maquetacion Landing de Abogados](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/tree/5bf5aa4219c86edebdd2a5d4bc2914780e3658bf/DIW_DisenyoInterfaces/Ejercicios/10_Ejercicio3_maquetacion_landing_abogadosSass)

### DESCRIPCIÓN:

En este Ejercicio se propone hacer una página web de abogados lo más parecido a lo presentado en Figma, utilizando grid, flexbox, y todo esto incluido en Sass. Aplicamos todo lo aprendido anteriormente para hacer una gestión precisa de lo solicitado.

### RESULTADO:

![imagen_resultadoEjercicios10](https://github.com/Alejandro-RHBits/AsignaturasLorenzo/blob/main/DIW_DisenyoInterfaces/Ejercicios/10_Ejercicio3_maquetacion_landing_abogadosSass/assets/img/Resultado_Ejercicio10.png?raw=true)

