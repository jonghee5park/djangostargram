from django.contrib import admin
from .models import Dsuser
from .models import Post

# Register your models here.

class DsuserAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dsuser,DsuserAdmin)
admin.site.register(Post,PostAdmin)