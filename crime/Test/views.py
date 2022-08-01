from django.shortcuts import render
from test.models import AuthUsers
import hashlib

# Create your views here.
def homepage(request):
    return render(request, "index.html", {})

def register(request):
    return render(request, "registration.html", {})

def signin(request):
    return render(request, "signin.html", {})

def dosignup(request):
    if request.method == "POST":
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        em = request.POST["emailid"]
        pwd = request.POST["passwd"]
        addr = request.POST["address"]

        encpwd = hashlib.md5(pwd.encode("utf-8")).hexdigest()

        authusers = AuthUsers(
            fname = fn,
            lname = ln,
            emailid = em,
            password = encpwd,
            address = addr
        )

        authusers.save()

    return render(request, "index.html", {"message": "Registration successful! PLease sign in"})

def dosignin(request):
    if request.method == "POST":
        em = request.POST["emailid"]
        pwd = request.POST["passwd"]

        encpwd = hashlib.md5(pwd.encode("utf-8")).hexdigest()

        checkuser = AuthUsers.objects.get(emailid=em)

        if encpwd == checkuser.password:
            request.session["sess_user"] = checkuser.fname + " " + checkuser.lname
            request.session["emailid"] = checkuser.emailid
            return render(request, "index.html", {})

        else:
            return render(request, "signin.html", {"error": "Wrong credentials"})

    #return render(request, "index.html", {"message": "Registration successful! PLease sign in"})

def logout(request):
    del request.session["sess_user"]

    return render(request, "index.html", {})