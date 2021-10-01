from django.contrib import admin

# Register your models here.
from .models import Sujet


admin.site.site_url = "/polls"
admin.site.register(Sujet)