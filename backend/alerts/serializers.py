# Convert the models to JSON

from rest_framework import serializers

from .models import Alert, AlertNotification

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = [
            'id',
            'user',
            'crypto',
            'target_price',
            'condition',
            'is_active',
            'created_at',
            'triggered_at',
        ]
        
class AlertNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertNotification
        fields = [
            'id',
            'alert',
            'price_at_trigger',
            'status',
            'notified_at',
        ]