# Manual para la Creación de Usuarios en el Opportunity Portal de AIESEC

El propósito de este manual es proporcionar una guía detallada sobre cómo crear usuarios en el Opportunity Portal (OP) de AIESEC mediante la Autenticación Platform. Esto permitirá la conexión de formularios de registro al sistema.

## Creación de Usuarios 👤
Dentro de este repositorio, encontrarás dos archivos fundamentales: `expa.py` y `constant.py`. 

En el archivo `expa.py`, se ha definido una clase llamada `Person`, la cual te facilita el registro de usuarios a través del método `register_user()`. A continuación, te mostramos un ejemplo de cómo registrar un nuevo usuario:

```python
# Crear una instancia de Person
ep = Person(
    'Nombre',
    'Apellido',
    'correo@example.com',
    '9890000000',
    # LC que le dará seguimiento
    'Aguascalientes',
    'Facebook',
    'Sí',
    'Sí',
    [7]
)
ep.register_user()
```
El método register_user() generará un JSON con los datos del usuario y enviará una solicitud de registro. El JSON tendrá la siguiente estructura:
```json
{
 "user": {
   "first_name": "Nombre",
   "last_name": "Apellido",
   "email": "correo@example.com",
   "country_code": "+00",
   "phone": "9890000000",
   "password": "ContraseñaGenerada",
   "lc": 207,
   "referral_type": "Facebook",
   "mc": 0,
   "allow_phone_communication": "true",
   "allow_email_communication": "true",
   "selected_programmes": [7]
 }
}

```
Al finalizar el proceso, se mostrará un mensaje de éxito. En caso de producirse algún error, se proporcionarán detalles al respecto.

#### Opciones Disponibles
***selected_programmes:*** Puedes asignar al usuario a programas específicos utilizando los respectivos ID (7 para Global Volunteer, 8 para Global Talent y 9 para Global Teacher).

En el archivo `constant.py`, deberás actualizar los valores que corresponden a tu entidad, incluyendo los MC ID y LC IDs.

#### Identificadores (ID)
Log in ➔ Dashboard ➔ Committees ➔ Export
<p align="center">
<img src="https://github.com/xKary/AIESEC-EXPA/assets/38677830/ea0b9fae-606c-4c51-bb91-5db251831c38"/>
</p>

Para seleccionar la casilla de *ID*, simplemente marca la casilla correspondiente, y recibirás un archivo *.xlsx* en tu correo con los datos que has seleccionado. Luego, puedes utilizar la herramienta de filtro en Excel, Google Sheets o cualquier otro programa que prefieras para encontrar los IDs de tus comités locales y de tu entidad.

#### URL
La URL a la que debes enviar las solicitudes POST se encuentra en:

Log in ➔ Dashboard ➔ Resource Center ➔ #Platforms ➔ Signing up users through the API

**Nota** 🗒️: Para utilizar este código, simplemente debes realizar modificaciones en el archivo `constants.py` y luego agregar el archivo `expa.py` a tu flujo de trabajo, lo que permitirá que los registros se realicen de manera automática.

---
- El programa está escrito en python, pero es muy sencillo pasarlo a otro lenguaje de programación como JavaScript.
- Podrás encontrar información relacionada con el registro de usuarios en esta [página](https://expa.aiesec.org/resource-center/pages/1429).
- Si tienes dudas o preguntas puedes contactarme 😄
- Puedes exploarar las siguientes heramientas para hacer flujos de trabajos:
  - [Pipedream](https://pipedream.com/)
  - [Zapier](https://zapier.com/)


