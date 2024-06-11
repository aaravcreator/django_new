from django.contrib import admin

# Register your models here.
from .models import Person,Mission,ContactData

admin.site.register([Person,Mission])

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','subject','message','timestamp')
    search_fields = ('name',)

admin.site.register(ContactData,ContactAdmin)