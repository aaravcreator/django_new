from django.shortcuts import render,redirect
from .models import Person
from .forms import PersonForm
from django.contrib.auth import login,logout
from django.db.models import Q
# Create your views here.
def person_list(request):
    print(request.GET)

    query = request.GET.get('query')
    if query and query != '':
        persons = Person.objects.filter(Q(name__icontains=query) | Q(phone = query))
    else:
        persons = Person.objects.all().order_by('age')

    male_count = persons.filter(gender="MALE").count()
    female_count = persons.filter(gender="FEMALE").count()
    # print(persons)
    context = {
        'male_count':male_count,
        'female_count':female_count,
        'persons':persons
    }
    return render(request,'person_list_bs.html',context)


def create_person(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('person_list')

    context = {
        'form':form

    }
    return render(request,'create_person.html',context)

def update_person(request,id):
    person  =  Person.objects.get(id=id)
    form = PersonForm(instance=person)
    if request.method == 'POST':
        form = PersonForm(request.POST,instance=person)
        if form.is_valid():
            form.save() 
            return redirect('person_list')

    context = {
        'form':form,
        'person':person

    }
    return render(request,'update_person.html',context)


def delete_person(request,id):
    person  =  Person.objects.get(id=id)
    person.delete()
    return redirect('person_list')



