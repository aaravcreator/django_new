from django.shortcuts import HttpResponse,render

# Example index view function
from random import randint


def base_page(request):
    return render(request,'base.html')



def index(request):
    random_value = randint(50,5000)
    print(random_value)

    return HttpResponse(f"<h1>HELLO FROM DJANGO , Random value is {random_value} </h1>")

def contact(request):
  
    name = "RAM"
    phone = "92342934729"
    return HttpResponse(f"<h1>This is contact page</h1> <p> {name}</p> <p> PHONE : {phone}</p>")


def services(request):
    services = ['Dgital Marketing','SEO','Content Writing']
    services_data = ' '.join(services)
    print(services_data)
    return HttpResponse(f"<h1>Services</h1> <p> {services_data}</p> ")

def profile_page(request,id):
    # Fetch user from database using the id
    print(id)
    return HttpResponse(f"<h1>Profile Page of #{id}</h1>")

def index_page(request):

    if request.method == "POST":
        print(request.POST)
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        print(username,password)
        return HttpResponse(f"<h1>Username : {username} , Password : {password}</h>")
    # if username is not None  and password is not None:
    #     user_data = f"Thanks for submitting! {username} - {password}"
    #     return HttpResponse(user_data)
    context = {
        
        'name':'RAM',
        'age':55,
        'is_married':False,
        'skills':['Python','Django','Flask','Java','C++']
        }
    
    return render(request,'index.html',context)


    
