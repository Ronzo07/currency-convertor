from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Get the selected currency from the form submission
    selected_currency = request.form.get('currency')

    # Set the default currency to EUR if no currency is selected
    if selected_currency is None:
        selected_currency = 'EUR'

    # Make a request to the API to get the exchange rate data
    response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{selected_currency}')
    data = response.json()

    # Get the exchange rate for the given currency
    exchange_rate = data['rates']['USD']

    # Render the template and pass in the exchange rate data and selected currency
    return render_template('index.html', exchange_rate=exchange_rate, selected_currency=selected_currency)

if __name__ == '__main__':
    app.run(debug=True)