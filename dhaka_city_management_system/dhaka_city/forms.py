from django import forms
from dhaka_city.models import people_table

class people_tableForm(forms.ModelForm):
    class Meta:
        model = people_table
        fields = ['id', 'Full_name', 'Father_name','Mother_name', 'address', 'Age','Blood_group']