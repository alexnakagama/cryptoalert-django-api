from django.contrib import admin

from .models import Alert, AlertNotification

# Register your models here.
admin.site.register(Alert)
admin.site.register(AlertNotification)