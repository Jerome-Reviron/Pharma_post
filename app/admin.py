from django.contrib import admin
from app.models import Flux, D_TYPE_VACCIN, D_DATE, D_LOCATION, F_FLUX

# Register your models here.
admin.site.register(Flux)
admin.site.register(D_TYPE_VACCIN)
admin.site.register(D_DATE)
admin.site.register(D_LOCATION)
admin.site.register(F_FLUX)