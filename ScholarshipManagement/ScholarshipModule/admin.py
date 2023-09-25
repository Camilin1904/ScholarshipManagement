from django.contrib import admin
from .models import Scholarships
from .models import Donors

# Register your models here.
admin.site.register(Scholarships)
admin.site.register(Donors)
