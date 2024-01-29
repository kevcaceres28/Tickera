from flask import Flask, render_template, request, jsonify
from payu import PayU
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)

app = Flask(__name__)

payu = PayU(
    merchant_id='tu_id_de_comercio',
    api_login='tu_login_de_api',
    api_key='tu_clave_privada',
    test_mode=True 
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar_evento', methods=['GET', 'POST'])
def agregar_evento():
    if request.method == 'POST':
        titulo = request.form['titulo']
        fecha = request.form['fecha']

        return render_template('exito.html')  

@app.route('/procesar_pago', methods=['POST'])
def procesar_pago():
    try:
        
        evento_id = request.form['evento_id']
        monto = 1000 

        response = payu.payments.create({
            'reference_code': 'codigo_de_referencia_unico',
            'description': 'Pago por evento',
            'value': monto,
            'currency': 'USD',  
            'buyer_email': 'correo@ejemplo.com',  
            'test_mode=True'
        })

        
        return jsonify({'redirect_url': response['payment_url']})
    except Exception as e:
        logging.error(f'Error al procesar el pago: {str(e)}')
        return jsonify({'error': 'Error al procesar el pago'})

if __name__ == '__main__':
    app.run(debug=True)
