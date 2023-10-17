# [AIESEC - EXPA]((https://expa.aiesec.org/resource-center/pages/1429))
El propósito de este manual es proporcionar una guía detallada sobre cómo crear usuarios en el Opportunity Portal (OP) de AIESEC mediante la Autenticación Platform, con el fin de permitir la conexión de formularios de registro al sistema.

Podrás encontrar está información en:

---
Log in &rarr; Resource Center &rarr; #Platforms &rarr; Signing up users through the API

### Creación de Usuarios


Ejemplo de JSON:
```
{
 "user": {
   "first_name": "Sedhu",
   "last_name": "Madhavan",
   "email": "sedhu+852625@commutatus.com",
   "country_code": "+91",
   "phone": "9890000000",
   "password": "FKADNAKDNq9",
   "lc":630,
   "referral_type": "friends",
   "allow_phone_communication": "true",
   "allow_email_communication": "true",
   "selected_programmes": [7]
 }
}
```
#### Opciones disponibles
- **selected_programmes:** Puede asignar al usuario a programas específicos mediante la inclusión de sus respectivos ID (7 para Global Volunteer, 8 para Global Talent y 9 para Global Teacher).

#### Contraseña
La contraseña debe cumplir con los siguientes requisitos:
- Debe tener al menos 8 caracteres.
- Debe contener al menos una letra minúscula.
- Debe contener al menos una letra mayúscula.
- Debe contener al menos un dígito.

Ejemplo de registro de un nuevo usuario:
```
# Crear una instancia de Persona
ep = Person(
    "Sedhu",
    "Madhavan",
    "harok99235@cindalle.com",
    "9890000000",
    'Aguascalientes',
    "friends",
    "Sí",
    "Sí",
    [7, 8, 9]
)

ep.register_user()
```
