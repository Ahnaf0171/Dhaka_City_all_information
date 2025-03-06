from django.contrib import admin
from dhaka_city.models import people_table

# Register your models here.
class people_tableAdmin(admin.ModelAdmin):
    list_display = ('id', 'Full_name', 'Father_name','Mother_name', 'address', 'Age','Blood_group')


admin.site.register(people_table, people_tableAdmin)

