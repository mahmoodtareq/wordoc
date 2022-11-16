from django.apps import AppConfig
from wordoc.data import load_words


class WordicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wordoc'

    def ready(self):
        load_words()
