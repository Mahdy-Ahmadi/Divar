import requests
import json

class DivarAuthenticator:
    def __init__(self):
        self.base_url_authenticate = "https://api.divar.ir/v5/auth/authenticate"
        self.base_url_confirm = "https://api.divar.ir/v5/auth/confirm"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            "Origin": "https://divar.ir",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
            "Referer": "https://divar.ir/"
        }
    
    def send_code(self, phone):
        payload = {
            "phone": phone
        }
        response = requests.post(self.base_url_authenticate, data=json.dumps(payload), headers=self.headers)
        
        if response.status_code == 200:
            print("Code sent successfully!")
            return True
        else:
            print(f"Failed to send code. Status code: {response.status_code}")
            print(response.text)
            return False
    
    def confirm_code(self, phone, code):
        payload = {
            "phone": phone,
            "code": code
        }
        response = requests.post(self.base_url_confirm, data=json.dumps(payload), headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            print("Authentication successful!")
            print("Response Data:", data)
        else:
            print(f"Authentication failed with status code {response.status_code}")
            print(response.text)

    def get_phone_and_code(self):
        phone = input("Enter your phone number: ")
        
        if self.send_code(phone):
            code = input("Enter the confirmation code you received: ")
            self.confirm_code(phone, code)

authenticator = DivarAuthenticator()
authenticator.get_phone_and_code()
