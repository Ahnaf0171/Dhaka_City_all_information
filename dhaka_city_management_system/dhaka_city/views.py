from django.shortcuts import render, redirect
from .models import people_table
from .forms import people_tableForm

# Create your views here.
def home(request):
    return render(request, "index.html")
def people_info(request):
    people = people_table.objects.all()
    return render(request, 'people.html', {'people_key' : people})

def add_person(request):
    if request.method == 'POST':
        person = people_tableForm(request.POST)
        if person.is_valid():
            person.save()
            return redirect("people_info_u")
    else: 
        person = people_tableForm()
    return render(request,'add_person.html',{"form":person})

def update_person(request, id):
    person = people_table.objects.get(pk=id)
    if request.method == 'POST':
        one_person = people_tableForm(request.POST, instance = person)
        if one_person.is_valid():
            one_person.save()
            return redirect('people_info_u')
    else:
        person = people_tableForm(instance=person)
        return render(request, 'add_person.html', {"form" : person})
def delete_person(request, id):
    person1 = people_table.objects.get(pk=id)
    person1.delete()
    return redirect('people_info_u')



        
    