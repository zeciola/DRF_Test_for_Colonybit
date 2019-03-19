from django.contrib import admin
from .models import Comments, Replies

admin.site.register(Comments)
admin.site.register(Replies)