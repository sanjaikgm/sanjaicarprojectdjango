from django.shortcuts import render,redirect
from . models import signuplog,addcarlog
# Create your views here.
def login(request):
    return render(request,"login.html")

def accounts(request):
    return render(request,"accounts.html")
def home(request):
    return render(request,"home1.html")
def rent(request):
    return render(request,"rent.html")
def rentnext(request):
    return render(request,"rentnext.html")
def mechanic(request):
    return render (request,"mechanic.html")
def mechanic(request):
    return render (request,"mechanic.html")

def manager(request):
    return render (request,"manager.html")

def book(request):
    return render (request,"book.html")
def your(request):
    return render(request,"yourorders.html")
def addpage(request):
    return render(request,"addcar.html")

def signup(request):
    val={'key':""}
    

    if request.method=='POST':
        user=request.POST.get("username")
        pas=request.POST.get("password")
        con=request.POST.get("confirm")
        em=request.POST.get("email")
        oc=request.POST.get("occupation")
        if signuplog.objects.filter(username=user,password=pas,occupation=oc).exists():
            val={'key':"Already account exists"}
            return render(request,'signup.html',val)
        
        if pas==con and oc=="mechanic":
            signuplog.objects.create(username=user,password=pas,email_id=em,occupation=oc)
            return render(request,"mechanic.html",val)
        
        if pas==con and oc=="customer":
            signuplog.objects.create(username=user,password=pas,email_id=em,occupation=oc)
            return render(request,"home1.html",val)
        
        if pas==con and oc=="manager":
            signuplog.objects.create(username=user,password=pas,email_id=em,occupation=oc)
            return render(request,"manager.html",val)
        
        else:
            val={'key':" ! password does not match !"}
            return render(request,"signup.html",val)
    return render(request,"signup.html",val)
def loginnew(request):
    val={'key':""}
    user=request.POST.get("username")
    pas=request.POST.get("password")
    if signuplog.objects.filter(username=user,password=pas).exists():
        obj=signuplog.objects.get(username=user,password=pas)
        occ=obj.occupation
        if occ=="mechanic":
            return render(request,"mechanic.html",val)
        
        if  occ=="customer":
            return render(request,"home1.html",val)
        
        if  occ=="manager":
            return render(request,"manager.html",val)
        

        return  render(request,"home1.html",val)
    else:
        val={'key':" ! username or password doest not match !"}
        return render(request,"login.html",val)

def add(request):
    if request.method=='POST':
        name=request.POST.get("name")
        img=request.POST.get("img")
        price=request.POST.get("price")
        addcarlog.objects.create(name=name,img=img,price=price)
        log=addcarlog.objects.get(name=name,price=price)
        carname=log.name
        carprice=log.price
        carimg=log.img
        val={'name':carname,'img':carimg,'price':carprice}
        request.session['carname']=carname
        request.session['carimg']=carimg
        request.session['carprice']=carprice
    return render(request,"addcar.html",val)

