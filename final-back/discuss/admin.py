from django.contrib import admin
from .models import Discuss, DiscussComment

# Register your models here.

admin.site.register(Discuss)
admin.site.register(DiscussComment)