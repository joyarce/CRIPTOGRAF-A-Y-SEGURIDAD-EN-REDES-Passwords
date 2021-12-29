# Criptografía y seguridad en redes: Passwords


## Descripción
Auditación de implementación de los sistemas de creación, actualización, acceso, transmisión y recuperación de contraseñas de dos sitios distintos (uno chileno y uno perteneciente a la comunidad europea), automatizando el proceso mediante [Dropwizard](http://www.dropwizard.io/1.0.2/docs/)Selenium.

El código en Python automatiza lo siguiente:

* Creación de una cuenta
* Inicio de sesión (permitirá recrear ataques por fuerza bruta)
* Restablecimiento de contraseña (no requiere *login* del usuario)
* Modificación de contraseña (requiere *login* del usuario)
