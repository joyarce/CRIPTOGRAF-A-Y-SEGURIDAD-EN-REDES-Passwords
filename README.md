# Criptografía y seguridad en redes: Passwords

## Descripción
Auditación de implementación de los sistemas de creación, actualización, acceso, transmisión y recuperación de contraseñas de dos sitios distintos (uno chileno y uno perteneciente a la comunidad europea), automatizando el proceso mediante [Selenium](https://www.selenium.dev/documentation/webdriver/)

El código en Python automatiza lo siguiente:

* Creación de una cuenta
* Inicio de sesión (permitirá recrear ataques por fuerza bruta)
* Restablecimiento de contraseña (no requiere *login* del usuario)
* Modificación de contraseña (requiere *login* del usuario)

## Código

Funciones principales:

* Crear cuenta
* Inicio de Sesión.
* Restablecer contraseña sin necesidad de identificar previamente al usuario en cuestión.
* Modificación de contraseña identificando previamente al usuario en cuestión.

Funciones secundarias:

* Generador aleatorio de correos electrónicos que satisfacen los requisitos de los sitios auditados.
* Generador aleatorio de contraseña
* Generador aleatorio de nombres y apellidos

## Resultados
### Sitio Chileno




La contraseña admitida en este sitio debe poseer un largo mínimo de 5 caracteres y un máximo de 72. La base permitida son todos los caracteres del teclado (base 94), UNICODE, EMOJIS y UTF-8. Esto se verifica al ver el código HTML tanto al momento de querer registrar un usuario y en el proceso de modificación de contraseña.

_El largo máximo (72) se determinó modificando la contraseña de un usuario registrado a una de largo 73 para posteriormente ingresar la contraseña sin el último carácter._

Para el restablecimiento de esta, se necesita una dirección de correo electrónico para comprobar si existe registro en la base de datos. Esta ultima información no será notificada al usuario y, por ende, no existe información expuesta. Si existe el registro, se envía un link de restablecimiento al correo señalado en donde se podrá ingresar una nueva contraseña con las características ya señaladas.

**Fuerza bruta**: Se inicia por registrar un usuario. Luego, se automatiza 100 intentos de ingresar a esta cuenta con una contraseña que no es la que corresponde al registro previo.

<p align="center">
![](images/fbcode_chile.png)
![](images/fb_chile.png)
</p>

#### Conclusión
No se bloquea de ninguna forma el intento de ingreso durante los 100 ciclos. Al modificar el código sin tiempos de espera entre procesos, la página no presenta ningún sistema de bloqueo a comparación con la página de la Unión Europea. 

Por otra parte, la gestión de datos personales es la misma que el sitio de Unión Europea: al intentar restablecer la contraseña de un usuario introduciendo el correo electrónico asociado, el sitio chileno no confirma en el momento si este está registrado.

### Sitio Unión Europea
La contraseña de este sitio tiene un largo mínimo de 6 caracteres y un máximo que no pudo ser definido. La base permitida son todos los caracteres del teclado (base 94), UNICODE, EMOJIS y UTF-8. El máximo largo de contraseña permitido no pudo ser comprobado. Se generó una cadena de caracteres de 1,5 millones de largo. Luego, se intenta ingresar la contraseña sin el último dígito.

Para el restablecimiento de esta, se necesita una dirección de correo electrónico para verificar existe su registro en la base de datos. Esta última información no será notificada al usuario y, por ende, no existe información expuesta. Si existe el registro, se envía un link de restablecimiento al correo señalado en donde se podrá ingresar una nueva contraseña con las características ya señaladas.

**Fuerza bruta**: Se inicia por registrar un usuario. Luego, se automatiza 100 intentos de ingresar a esta cuenta con una contraseña que no es la que corresponde al registro previo.

![](images/fbcode_chile.png)

#### Conclusión
No se bloquea de ninguna forma el intento de ingreso durante los 100 ciclos. Cuando se detecta un conjunto de datos ingresados de manera casi instantánea se bloquea por SPAM. Debido a esto, se añadió al código un tiempo de espera para vulnerar esta regla.

Por otro lado, la gestión de datos personales es la misma que el sitio nacional. Al intentar restablecer la contraseña de un usuario introduciendo su correo electrónico asociado este no confirma en el momento si este está registrado.
