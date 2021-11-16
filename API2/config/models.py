from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.forms import IntegerField

from config.validators import validate_number


class Service(models.Model):
    from_date = models.DateField()
    to_date = models.DateField()
    views = models.IntegerField(validators=[validate_number])
    clicks = models.IntegerField(validators=[validate_number])
    cost = models.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])

    class Meta:
        ordering = ['-from_date']

    """ Рассчитываем среднюю стоимость клика """

    def average_click(self):
        result = self.cost / self.clicks
        b = round(result, 2)  # оставляем после запятой 2 числа
        return f"{b} рублей"

    """ Рассчитываем среднюю стоимость 1000 показов"""

    def average_view(self):
        result = self.cost / self.views * 1000
        b = round(result, 2)  # оставляем после запятой 2 числа
        return f"{b} рублей"
