

from django.shortcuts import render,HttpResponse,redirect
from studentapp.models import stud,log

# Create your views here.

def create(request):
    print("request is :",request.method)
    if request.method=="GET":
        return render(request,'index.html')
   # else:
    #    return HttpResponse("insert form data into db")
    else:
        n=request.POST['name']
        n2=request.POST['roll_no']
        n3=request.POST['email']
        n4=request.POST['branch']
        n5=request.POST['year']
        n6=request.POST['attendance_date']
        n7=request.POST['attendance_status']
       # print("name is",n)
        m=stud.objects.create(name=n,roll_no=n2,email=n3,branch=n4,year=n5,attendance_date=n6,attendance_status=n7)
        m.save()
       # return HttpResponse("insert data")
        return redirect('/dashboard')
        


def login(request):
    print("request is :",request.method)
    if request.method=="GET":
        return render(request,'login.html')
   # else:
    #    return HttpResponse("insert form data into db")
    else:
        n=request.POST['name']
        n2=request.POST['password']
        m=log.objects.create(name=n,password=n2)
        m.save()
       # return HttpResponse("insert data")
        return redirect('/index')
    
def home(request):
        return render(request,'home.html')
    

def dashboard(request):
    m=stud.objects.all()
    #print(m)
    context={}
    context['data']=m
   # return HttpResponse("msg is display")
    return render(request,'dashboard.html',context)

def edit(request,id):
   # return HttpResponse(id)
    if request.method=="GET":
        m=stud.objects.filter(id=id)
        print(m)
        context={}
        context['data']=m
        return render(request,'edit.html',context)
    
    else:
        n=request.POST['name']
        n2=request.POST['roll_no']
        n3=request.POST['email']
        n4=request.POST['branch']
        n5=request.POST['year']
        n6=request.POST['attendance_date']
        n7=request.POST['attendance_status']
       # print("name is",n)
       # print(n2)
        m=stud.objects.filter(id=id)
        m.update(name=n,roll_no=n2,email=n3,branch=n4,year=n5,attendance_date=n6,attendance_status=n7)
        return redirect('/dashboard')


def delete(request,id):
    #return HttpResponse(id)
    m=stud.objects.filter(id=id)
    print(m)
    m.delete()
    return redirect('/dashboard')

