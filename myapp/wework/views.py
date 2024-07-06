from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp

# Create your views here.
def wework_home(request):
    
    emps=Emp.objects.all()
    
    return render(request, "wework/home.html",{
        'emps':emps
    })



def add_emp(request):
    if request.method=="POST":
        
        #data fetch
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_addr=request.POST.get("emp_addr")
        emp_ph=request.POST.get("emp_ph")
        workig=request.POST.get("workig")
        emp_dept=request.POST.get("emp_dept")
        #create model object and set data
        
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_ph
        e.address=emp_addr
        e.workig=workig
        e.department=emp_dept
        if workig is None:
            e.workig=False
        else:
            e.workig=True
        
        
        #save the object
        e.save()
        #prepare msg
        return redirect("/wework/home")
    return render(request, "wework/add_emp.html",{})
    
    
def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/wework/home/")
    
def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request, "wework/update_emp.html",{
        'emp':emp
    })
    
 
def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_addr=request.POST.get("emp_addr")
        emp_ph=request.POST.get("emp_ph")
        workig=request.POST.get("workig")
        emp_dept=request.POST.get("emp_dept")
        
        e=Emp.objects.get(pk=emp_id)
        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_ph
        e.address=emp_addr
        e.workig=workig
        e.department=emp_dept
        if workig is None:
            e.workig=False
        else:
            e.workig=True
        
        
        e.save()    
    return redirect("/wework/home")
    