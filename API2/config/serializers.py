from rest_framework import serializers

from config.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    def validate(self, data):
        """
        Проверяем не стоит ли конечная дата до начальной
        """
        if data['from_date'] > data['to_date']:
            raise serializers.ValidationError({"to_date": "конечная дата должна быть позже начальной"})
        return data

    class Meta:
        model = Service
        fields = ('from_date', 'to_date', 'views', 'clicks', 'cost', 'average_click', 'average_view')
