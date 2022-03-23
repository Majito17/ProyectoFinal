# Proyecto Final : Algoritmos y Programación

## Juego De Bingo
###### Este proyecto esta realizado por: 
    Nicolás Sánchez
    Sebastián Suárez
    María Paula Domínguez
    María José Gómez 
 
# Introducción
¿Alguna vez has querido saber cómo se programa un videojuego? 
La respuesta probablemente es sí, somos mentes curiosas en donde más de una vez nos hacemos preguntas a cosas que creemos nunca responderemos. Por tu mente al ver a tu hermano, algún familiar o incluso encontrándote a ti mismo jugando en la consola o computador cualquier estilo juego te preguntaste: ¿Cómo hacen para que los gráficos sean de una forma? ¿Por qué hay tamaños específicos para algunos objetos?  ¿Cómo funcionan en general? 
En algunos aspectos puede llegar a ser complejo, pero no tanto como se podrían imaginar. Sé que si hablamos de programación se vienen a la mente un sinfín de números, letras y cosas complejas que probablemente crees que no son para ti o demasiado complicadas de entender, pero aunque tengamos este tipo de prejuicios queremos demostrar por medio de este informe como podrás crear tu propio juego para poder divertirte y, en el proceso, aprender un poco sobre programación.
 Así que, ¿por qué no? Hagamos un bingo. Lo has jugado alguna vez, quizá con tu familia de forma repetitiva, y si no definitivamente lo has jugado por lo menos una vez con amigos. Sabemos perfectamente que, aunque no es tu favorito saca risas sinceras y momentos para recordar. Entonces, por qué no poder jugarlo de forma virtual y aun mejor haberlo hecho por ti mismo. Así que, con esto, traemos a algo tan común como el bingo a la virtualidad para que puedas jugarlo tan apasionadamente como si lo jugaras con tu familia alrededor.
 
# ¿Por qué Bingo?
  La decisión de realizar un bingo como proyecto final nace de la oportunidad de aplicar gran parte de lo aprendido a lo largo de la clase en un solo código, desde el uso de bucles con while y for, condicionales if, elif, else, hasta el uso de matrices, todo en un solo gran código. También reforzamos la lógica que se necesita para construir un juego que contiene un buen número de reglas y diversos caminos según la cantidad cartones a jugar y la forma de juego en el cartón. 
Por lo tanto, en nuestro bingo, es posible jugar con diversos cartones y varias personas y, a medida que vayan saliendo números que aparezcan en los cartones, estos van a ser reemplazados por una equis (X), asimismo, una vez que exista un cartón ganador, el código será capaz de detectarlo. Tomamos un juego clásico familiar, que es jugado físicamente y lo llevamos a un formato virtual.  

# Programas que usamos:
## Python:
![Captura de pantalla 2022-03-22 214042](https://user-images.githubusercontent.com/98360959/159613379-344d1fea-c0d0-4cd9-835a-d28f4f1d4370.png)


Es importante resaltar que Python es un lenguaje de programación imprescindible para cualquier persona que quiera empezar en el mundo del desarrollo web, ya que hablamos de aquel lenguaje dinámico que se desarrolla e implementa en una diversidad de plataformas, en este caso no solo plataformas si no también de aplicaciones. El objetivo principal es la automatización de procesos en el cual se pueda ahorrar el tiempo y por ende la dificultad de un problema, esta totalmente diseñado para trabajar con grandes volúmenes de datos, pues su procesamiento y amplia biblioteca de recursos es ideal para iniciar en la programación. Fue el lenguaje de programación usado en Visual Studio Code para la creacion del proyecto. 

## Visual Studio Code: 

![Captura de pantalla 2022-03-22 213758](https://user-images.githubusercontent.com/98360959/159613080-9c5fb34d-4ac7-4581-878f-92e3135f8981.png)

Es un editor de código fuente desarrollado por Microsoft para multiples plataformas. También es personalizable, de modo que los usuarios pueden cambiar el tema del editor, los métodos abreviados de teclado y las preferencias. Cuenta con herramientas de Debug hasta opciones para actualización en tiempo real de nuestro código en la vista del navegador y compilación en vivo de los lenguajes que lo requieran. Su papel fue ser el editor de texto que usamos para el desarrollo del proyecto.

## Tkinter

Se trata de un paquete de herramientas o librería de Python que nos permite la programación de interfaces graficas (GUI), ya viene por defecto, así que no es necesaria su instalación. Es una librería sencilla de entender y para crear interfaces de usuario prácticas, simples y rápidas. Importamos la librería como “Import tkinter”, ya que existen otras formas de importarla por completo, pero en este caso fuimos nombrando según los elementos de la librería que se iba utilizando.

## ¿Y la interfaz del Bingo?

Buscamos hacer un prototipo de interfaz sencillo de comprender, donde todos los jugadores puedan interactuar. Al ver la interfaz, lo que buscamos que sea más llamativo es el cartón, donde resaltamos las letras por colores y luego continuamos con una cuadricula 5x5 donde encontramos los números, a la letra B le corresponden de 1 al 15, a la letra I del 16 al 30, la letra N del 31 al 45, la letra G del 46 al 60 y la letra O del 61 al 75. 

<img src="https://user-images.githubusercontent.com/98360570/159751679-56650325-9302-4068-9a0f-5c584b462878.PNG" width="500" height="400" />

Utilizamos la clase “Label” para las letras y la clase “Button” para los números, cada una de estas clases contiene parámetros para que se le dé forma a la clase, como lo es texto, la fuente, color de texto, de fondo y como se quiere que luzca en general, de esta manera, cuando el cartón tenga uno de los números al sortear, al darle clic se reemplazará por una X, lo que en el código del Bingo vendría siendo el 0, y de esta manera llenar el cartón. Para que funcionara este procedimiento con cada uno utilizamos una función que utiliza un comando en cada una de las casillas. 

<img src="https://user-images.githubusercontent.com/98360570/159753595-793558d9-650e-4945-aafb-e4050a3e009c.PNG" width="600" height="200" />

Utilizamos una función para conectar el botón de sorteo al Label de que nos permite ver los números aleatorios, el botón contiene un comando para que cada vez que este sea oprimido, cambie el número aleatoriamente entre 1 y 75. También, para poder jugar con otros cartones tenemos el botón de “Nuevo cartón” que permitiría al usuario tener un nuevo cartón o si se está jugando con otros usuarios.

<img src="https://user-images.githubusercontent.com/98360570/159754275-d91b8621-6695-4df3-b085-17f99140e587.PNG" width="250" height="150" />

El código del prototipo de la interfaz se divide en tres, en la primera parte podemos encontrar la vista general de la ventana, cómo luce y su tamaño. En la segunda parte encontramos cómo se construyó el BINGO, utilizando la clase Label y distinguiendo cada letra colores diferentes, tenemos el relieve GROOVE para darle ese efecto de botón, aunque no lo sea. En la tercera parte, y la más larga, son los números, utilizando la clase Button para crear un ecosistema más interactivo y permitirle al usuario cubrir los números que ya han salido. Por último, encontramos los widgets de la derecha, el botón de “Nuevo cartón” y el de “Sortear” que también fueron usados con la clase Button y finalmente, encontramos la pantalla de los números, donde se utilizó la clase Label y para dar el efecto pantalla el relieve SUNKEN, con fondo blanco. 

# Conclusión

Al pensar en automatizacion de un bingo puedes pensar primero que es bastante sencillo o tiene una idea muy básica de cómo será pero luego comienzan a salir los errores, no que los numeros no se pueden repetir, que en los cartones no logramos organizarnos como eran, como hay que divividir en los cartones. Pero la forma de solucionar estos problemas  fue algo muy útil, la mente de todos, esta siempre estuvo trabajando y dando alguno algún tipo de idea y con estos comentarios, a alguno se le iluminara la mente hasta el punto en el que logramos compactar y llevar el error a un codigo funcional pero con las ideas de todos, nos pudimos dar cuenta que atraves de los errores cambio la forma de ver el codigo, pues para la ultima parte tuvimos un error en donde no servian varios cartones entonces lo que ayudo a solucionar el problema fue un debuggin, esto logro a solucionar ese problema y tambien  pudimos entender el por que existia el error, a demas de que es curioso como tuvimos que investigar pues usamos herramientas como la mezcla de conceptos, un ejemplo son las listas, tambien investigamos conceptos que efectivamente nuestro profesor no explico. 
Es una realidad que amplio nuestro conocimiento, nos puso al limite por errores y esa necesidad de que fuera perfecto, pero sin embargo pudimos mezclar algo que nos gusta a nosotros como el bingo, con la programacion, que anque no fue facil, los conceptos basicos, un poco de investigacion, prueba y error pero tambien importante el trabajo en equipo logramos un proyecto unico.

# Referencias:

-	Bingo como se Juega Paso a Paso. (2022, 22 marzo). Grand Hotelier. https://grandhotelier.com/bingo/
-	EcuRed. (2019, 3 septiembre). Visual Studio Code - EcuRed. https://www.ecured.cu/Visual_Studio_Code
-	Santander Universidades. (2022, 1 marzo). ¿Qué es Python? | Blog. Becas Santander. https://www.becas-santander.com/es/blog/python-que-es.html
