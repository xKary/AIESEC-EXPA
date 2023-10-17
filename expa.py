import constant as con
import requests
import random
import string
import json

class Person:
    # Constructor de la clase 'Person' para inicializar los atributos de una persona.
    def __init__(self, first_name, last_name, email, phone, lc, referral_type, allow_phone_communication, allow_email_communication, selected_programmes):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        # Asignar 'lc' basado en el diccionario de códigos de ubicación en el módulo 'constant'.
        self.lc = con.LCS_ID[lc]
        self.referral_type = referral_type
        # Convertir los valores 'allow_phone_communication' y 'allow_email_communication' a 'true' o 'false'.
        self.allow_phone_communication = self.allow_value(allow_phone_communication)
        self.allow_email_communication = self.allow_value(allow_email_communication)
        self.selected_programmes = selected_programmes

    # Método para convertir 'Sí' a 'true' y cualquier otro valor a 'false'.
    def allow_value(self, value):
        if value == 'Sí':
            return 'true'
        return 'false'
    
    # Método para generar una contraseña aleatoria.
    def generate_password(self, length=8):
        lowercase = [random.choice(string.ascii_lowercase) for _ in range(length)]
        uppercase = [random.choice(string.ascii_uppercase) for _ in range(length)]
        digits = [random.choice(string.digits) for _ in range(length)]

        password_list = lowercase + uppercase + digits
        random.shuffle(password_list)

        return ''.join(password_list)

    # Método para convertir los datos de la persona a formato JSON.
    def get_json(self):
        # Generar un diccionario con los datos de la persona.
        user_data = {
            'user': {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'country_code': con.COUNTRY_CODE,
                'phone': self.phone,
                'password': self.generate_password(),
                'lc': self.lc,
                'referral_type': self.referral_type,
                'mc': con.MC_ID,
                'allow_phone_communication': self.allow_phone_communication,
                'allow_email_communication': self.allow_email_communication,
                'selected_programmes': self.selected_programmes
            }
        }
        print(user_data)
        return user_data
    
    # Método para registrar al usuario realizando una solicitud POST.
    def register_user(self):
        # Realizar la solicitud POST para registrar al usuario.
        response = requests.post(con.URL, json=self.get_json())

        # Verificar el estado de la respuesta.
        if response.status_code == 201:
            print('Usuario registrado exitosamente.')
        else:
            print(f'Error al registrar el usuario. Código de estado: {response.status_code}')
            print(response.text)
