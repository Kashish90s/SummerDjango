from django.shortcuts import render,redirect
from .models import Blog,Contact
from .forms import BlogForm


# Create your views here.
def homepage(request):
    # return HttpResponse("Hello")
    blog = Blog.objects.all()
    print(blog)
    return render(request,"crud/index.html",{"blogs":blog})



def Create(request):

    forms = BlogForm(request.POST or None)

    if(forms.is_valid()):
        forms.save()
        return redirect("crud:home")
    return render(request,"crud/create.html",{"forms":forms})


def ParticularData(request,id):
    blog = Blog.objects.get(id=id)
    return render(request,"crud/index.html",{"blog":blog})

def DeleteData(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("crud:home")

def UpdateData(request,id):
    blog = Blog.objects.get(id=id)
    forms = BlogForm(request.POST or None, instance = blog)
    if(forms.is_valid()):
        forms.save()
        return redirect("crud:home")
    return render(request,"crud/create.html",{"forms":forms})

def Contacts(request):
    if(request.method == "POST"):
        name=request.POST.get("name")
        email = request.POST.get("email")
        message=request.POST.get("message")
        cont = Contact(
            name =name,
            email = email,
            message = message
        )
        cont.save()
    return render(request,"crud/contacts.html")