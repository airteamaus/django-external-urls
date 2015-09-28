from django.dispatch import Signal

external_click = Signal(providing_args=["url", "ip"])
