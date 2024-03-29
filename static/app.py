from flask import Flask, render_template, request, jsonify, redirect, url_for
from static.payu_integration import PayU
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)

app = Flask(__name__)


payu = PayU(
    merchant_id='tu_id_de_comercio',
    api_login='tu_login_de_api',
    api_key='tu_clave_privada',
    test_mode=True  
)



if __name__ == '__main__':
    app.run(debug=True)

