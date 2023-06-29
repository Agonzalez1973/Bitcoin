def bitcoinToEuros(bitcoin_amount, bitcoin_value_euros):
    euros_value = bitcoin_amount * bitcoin_value_euros
    return euros_value

bitcoin_amount = 1.5
bitcoin_value_usd = 35000
bitcoin_value_euros = 0.85 * bitcoin_value_usd  # Suponiendo una tasa de cambio de 0.85 euros por dólar

euros_value = bitcoinToEuros(bitcoin_amount, bitcoin_value_euros)
print("Valor en Euros:", euros_value)

if euros_value < 30000:
    print("¡Alerta! El valor de Bitcoin está por debajo de 30,000€.")

