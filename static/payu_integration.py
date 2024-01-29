import requests

class PayU:
    def __init__(self, merchant_id, api_login, api_key, test_mode=True):
        self.base_url = 'https://sandbox.api.payulatam.com/payments-api/4.0/service.cgi' if test_mode else 'https://api.payulatam.com/payments-api/4.0/service.cgi'
        self.merchant_id = merchant_id
        self.api_login = api_login
        self.api_key = api_key

    def create_payment(self, data):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

        
        data['merchant']['apiLogin'] = self.api_login
        data['merchant']['apiKey'] = self.api_key
        data['merchant']['merchantId'] = self.merchant_id

       
        response = requests.post(f'{self.base_url}/payments-api/4.0/service.cgi', json=data, headers=headers)

     
        return response.json()
