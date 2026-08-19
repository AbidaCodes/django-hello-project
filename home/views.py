from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def index(request):
    if "user_id" not in request.session:
        return redirect("/login")

    search = request.GET.get("search", "")

    if search:
        users = User.objects.filter(
            name__icontains=search
        ) | User.objects.filter(
            email__icontains=search
        ) | User.objects.filter(
            city__icontains=search
        )
    else:
        users = User.objects.all()

    return render(request, "index.html", {"users": users})
def about(request):
    if "user_id" not in request.session:
        return redirect("/login")
    
    return render(request, "about.html")

def registration(request):
     
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        city = request.POST.get("city")
        password = request.POST.get("password")
        image = request.FILES.get("image")

        user = User(name=name, email=email, age=age, city=city, password=make_password(password), image=image)
        user.save()
        
        messages.success(request, "Registration successful! Please login")
        return redirect("/login")

    return render(request, "registration.html")

def edit(request, id):
    if "user_id" not in request.session:
        return redirect("/login")
    
    user = User.objects.get(id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        city = request.POST.get("city")
        image = request.FILES.get("image")

        user.name = name
        user.email = email
        user.age = age
        user.city = city

        if image:
            user.image = image

        user.save()

        messages.info(request, "Registration edited successfully!")

        return redirect("/")

    return render(request, "edit.html", {"user": user})

def delete(request, id):
    if "user_id" not in request.session:
        return redirect("/login")
    
    user = User.objects.get(id=id)
    user.delete()

    messages.error(request, "Registration deleted successfully!")

    return redirect("/")

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)

            if check_password(password, user.password):
                request.session["user_id"] = user.id
                return redirect("/")

            messages.error(request, "Invalid password!")

        except User.DoesNotExist:
            messages.error(request, "User with this email does not exist!")

    return render(request, "login.html")

def contact(request):
    if "user_id" not in request.session:
        return redirect("/login")   
    
    return render(request, "contact.html")

def logout(request):
    if "user_id" in request.session:
        del request.session["user_id"]
    
    return redirect("/login")