from django.contrib import admin
from .models import WorkingClass, Word, Voice, FullData

admin.site.register(WorkingClass)
admin.site.register(Word)
admin.site.register(Voice)
admin.site.register(FullData)