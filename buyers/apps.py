from django.apps import AppConfig


class BuyersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'buyers'

    def ready(self):
        """
        Registers buyer's signals
        :return:
        """
        import buyers.signals
