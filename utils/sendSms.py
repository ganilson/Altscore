import requests
import os

class SMSController:
    def __init__(self):
        self.base_url = 'https://app.smshub.ao/api/'  
        self.api = requests.Session()
        self.auth_token = None

    def enviar_mensagem(self, number, mensagem):
        authentication_data = {
            'authId': "223910707423150512",
            'secretKey': "s7fA9c5FhczE0EHI54PZ2d3c6U7HaQHwFdtn7WzrABa2TkqypBqHxUHA05qJ0F6Y9HylLDdRx75EmRirSJR6vrj13EeUBybpQz8W"
        }

        authentication_response = self.api.post(f'{self.base_url}authentication', json=authentication_data)
        auth_data = authentication_response.json()
        if 'data' in auth_data:
            self.auth_token = auth_data['data'].get('authToken')
            headers = {
                'accessToken': f'{self.auth_token}',
                'Content-Type': 'application/json'
            }
            user_data = { 
                'contactNo': [number],
                'message': mensagem
            }

            send_sms_response = self.api.post(f'{self.base_url}sendsms', json=user_data, headers=headers)
            if send_sms_response.text == 'Oops, SMS wallet is low':
                print("Você ficou sem mensagens")
            else:
                print("Mensagem enviada com sucesso")
        else:
            print('Falha na autenticação')


sms = SMSController()
