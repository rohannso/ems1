from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from first.models import Emp

def home(request):
    employee=Emp.objects.all()
    data={'employee':employee}
    
    return render(request,'home.html',data)
def index(request):
    return render(request,'index.html')

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('emp_phone')
        empid=request.POST.get('emp_id')
        adress=request.POST.get('emp_address')
        wk=request.POST.get('emp_working')
        dp=request.POST.get('emp_department')
        data=Emp(name=name,phone=phone,emp_id=empid,department=dp,address=adress)
        if wk is None:
            data.working=False
        else:
            data.working=True
        data.save()
        return redirect('home')
    return render(request,'addemp.html')

def deletemp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect('home')

def update(request,emp_id):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        e=Emp.objects.get(pk=emp_id)

        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
        return redirect('home')
    

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)

    return render(request,"update.html",{
        'emp':emp
    })


