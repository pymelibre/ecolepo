from django.contrib import admin
from .models import (
    Cooperative,
    Farmer,
    Distributor
)

admin.site.register(Cooperative)
admin.site.register(Farmer)
admin.site.register(Distributor)
