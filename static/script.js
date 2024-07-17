function updateExchangeRate() {
    // Make a request to the server to get the updated exchange rate
    fetch('/')
      .then(response => response.text())
      .then(data => {
        // Update the exchange rate paragraph with the new data
        document.getElementById('exchange-rate').innerHTML = data;
      });
  }

  // Set an interval to update the exchange rate every 10 seconds
  setInterval(updateExchangeRate, 10000);