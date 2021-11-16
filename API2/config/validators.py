from django.core.exceptions import ValidationError


def validate_number(value):
    """ Валидация полей чтобы нельзя было выставить число меньше 0 """
    if value < 0:
        raise ValidationError(message='Число не должно быть меньше нуля')
