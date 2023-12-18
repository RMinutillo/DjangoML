// static/js/app.js
paypal.Buttons({
    createOrder: function(data, actions) {
        // Lógica para crear una orden en el lado del cliente
        return actions.order.create({
            purchase_units: [{
                amount: {
                    value: '1.00'  // Monto del pago
                }
            }]
        });
    },
    onApprove: function(data, actions) {
        // Lógica para cuando el pago es aprobado
        return actions.order.capture().then(function(details) {
            // Muestra un mensaje de éxito
            document.getElementById('result-message').innerText = 'Pago completado. Transacción ID: ' + details.id;
        });
    }
}).render('#paypal-button-container');
