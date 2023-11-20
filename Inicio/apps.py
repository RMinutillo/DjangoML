from django.apps import AppConfig
import paypal



class InicioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Inicio'


class PayPalConfig(AppConfig):
    name = 'paypal'