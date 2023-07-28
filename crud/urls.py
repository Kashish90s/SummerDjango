from django.urls import path
from .views import homepage,Create,ParticularData,Contacts,DeleteData,UpdateData


app_name="crud"
urlpatterns = [
    path("",homepage, name="home"),
    path("create/",Create),
    path("<int:id>/",ParticularData,name = 'particular'),
    path("contacts/",Contacts),
    path("delete/<int:id>",DeleteData,name='deleteData'),
    path("update/<int:id>",UpdateData,name='updateData')
]