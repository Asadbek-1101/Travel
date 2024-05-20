from django.contrib import admin
from .models import Categories, Davlatlar, Reys, Country

admin.site.register([Categories, Davlatlar])
admin.site.register([Reys, Country])

