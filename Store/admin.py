from django.contrib import admin
from .models import Book
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    prepopulated_fields = {"slug":  ('title',) }
admin.site.register(Book,MemberAdmin)