# Estatura gráfica

#### Video Demo:  <URL HERE>
#### Description:
Este proyecto esta destinado a ayudar a los padres a llevar una control preciso de la evolucion de la estatura de sus hijos. En un pais como Bolivia, puede ser complicado para muchas familias acceder a servicios medicos de calidad para llevar un control de la estatura de sus hijos, existen tablas de estatura pero la posibilidad de guardar estos datos en una pagina web y poder a acceder a ellos a lo largo de los años resulta muy valioso



TODO
Se escogio Flask por que es un metodo eficiente de desarrollo web. Y por que resulta muy util en ciencia de datos para este proyecto en especifico.

### Arquitectura
Se usara HTML, CSS y JS en el frontend junto con paquetes de ayuda como Bootstrap y Jinja. Para el Backend se usara python con Flask. Todo correra en pythonanywhere de Conda, un servicio de host para paginas web en python. La Base de datos sera SQLite para guardar los registros de los usuarios. Se usara AWS congnito para la autenticacion de usuarios, ya que es un sistema robusto que permite a los usuarios crear una cuenta facilmente e inciar sesion con google, facebook, etc. 

###Home
Se muestra la tabla de evolucion de estatura con datos estadisticos generales. Y un boton de llamada a la accion para registrarse y comenzar a guardar un registro de estaturas.

###Login
Se implementara un sistema de login para cada usuario que quiera empezar a guardar un registro de estaturas

###Registro
En esta pagina el usuario podra crear un registro de una persona e ir guardando los registros, se podran guardar hasta 50 registros de una misma persona y el usuario podra crear varias personas para guardar sus registros.

###Graficas
Se escogera a una persona para poder ver sus graficas. Las graficas se haran en Seaborn al ser una libreria que simplifica el trabajo con graficas. Estas se renderizaran y mostraran en la interfaz en tiempo real. Con una opaciodad mas baja se mostraran los rangos de estatura promedios en la grafica. 

### Calculo de la estaura esperada
Se calculara la altura esperada a traves de datos estadisticos de varios factores, la hipotesis es que los factores mas importantes son altura del padre, altura de la madre, estatura de los abuelos, estatura de nacimiento, ciudad, deporte, consumo suplementos.

### Unidades de medida
Se usaran centimetros y meses, y/o años, para facilitar a los usuarios la interpretacion e ingreso de los datos.


