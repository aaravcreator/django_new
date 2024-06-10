"""
URL configuration for djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from .views import index,contact,services,profile_page
from .views import *
from myapp.views import person_list,create_person,update_person,delete_person


from django.conf import settings
from django.conf.urls.static import static
# from djangoproject import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # mapping the view function to root directory
    path('',index_page,name="index"),
    path('base/',base_page),
    path('contact/',contact,name="contact"),
    path('services/',services),
    path("person_list/",person_list,name="person_list"),
    path("personcreate/",create_person,name="create_person"),
    path('person_update/<int:id>/',update_person,name="update_person"),
    path('person_delete/<int:id>/',delete_person,name="delete_person"),
    path('profile/<int:id>/',profile_page)
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
