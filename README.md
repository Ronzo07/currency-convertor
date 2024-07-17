# Exchange Rate Display

#### Description:

This project is a web application that allows users to view the current exchange rate of various currencies with respect to the US dollar. The exchange rate data is obtained from the Exchange Rate API, which provides up-to-date information on currency exchange rates.

The app provides a simple and easy-to-use interface that allows users to select a currency from a dropdown list and view the current exchange rate. The exchange rate is updated automatically every minute using an API request and JavaScript, so users always have access to the most current data.

The app is built using the Flask web framework and uses Bootstrap for a responsive and visually appealing user interface.

## Features

- Allows the user to select a currency from a dropdown list and display the current exchange rate for that currency
- Updates the exchange rate automatically every minute using an API request and JavaScript
- Uses Bootstrap for a responsive and visually appealing user interface

## Requirements

- Flask
- Requests
- jQuery

## Setup

### Prerequisites

Before you can run the app, you will need to have the following software installed on your system:

- Python 3: You can download Python from the official website (https://www.python.org/) or use a package manager like `apt` or `brew` to install it.
- Flask: Flask is a Python web framework that is used to build the app. You can install it using `pip`, the Python package manager: `pip install flask`
- Requests: Requests is a Python library for making HTTP requests. You can install it using `pip`: `pip install requests`
- jQuery: jQuery is a JavaScript library that is used to make API requests and update the exchange rate on the page. It is included in the app's static files, so you don't need to install it separately.

### Running the app

To run the app, follow these step:


1. Clone the repository: `git clone https://github.com/user/exchange-rate-display.git`
2. Install the required libraries: `pip install -r requirements.txt`
3. Run the app: `python app.py`
4. Open the app in your web browser: `http://localhost:5000`

### Usage

1. Select a currency from the dropdown list
2. Click the "Go" button to display the exchange rate for that currency
3. The exchange rate will update automatically every minute

### Credits

- Exchange Rate API: https://www.exchangerate-api.com/
- Bootstrap: https://getbootstrap.com/

## Reason
This was the conclusion of CS50x with a final project where everything tie together. In fact, this course is first step that a computer scientist pass throughout. This was CS50. :)