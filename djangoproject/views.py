from django.shortcuts import HttpResponse,render,redirect

# Example index view function
from random import randint

from myapp.models import Mission,ContactData
from blog.models import BlogPost
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

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactData.objects.create(phone=phone,name=name,email=email,subject=subject,message=message)
    


        redirect('index')
    # if username is not None  and password is not None:
    #     user_data = f"Thanks for submitting! {username} - {password}"
    #     return HttpResponse(user_data)

    missions = Mission.objects.all()
    blogs = BlogPost.objects.filter(is_published=True)
    context = {
        'missions':missions,
        'blogs':blogs,

        
        'name':'RAM',
        'age':55,
        'is_married':False,
        'skills':['Python','Django','Flask','Java','C++']
        }
    
    return render(request,'flex_base.html',context)


    
