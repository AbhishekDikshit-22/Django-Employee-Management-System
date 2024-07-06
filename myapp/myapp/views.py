from django.http import  HttpResponse
from django.shortcuts import render

def index(request):
    check="Abi"
    if request.method=='POST':
        
        check=request.POST['check']
        print(check)   
    
    print("test function is called")
    name="Abhishek Dikshit"
    d_name=check
    list_of_comp=['Apple','Meta','Microsoft','Netflix','Amazon','Google']
    details={
        'e_name':"Abhishek",
        'job':"sde",
        'age':34,
        'current_co':"Google",
        'years_of_exp':5
    }
    data={
        'name':name,
        'd_name':check,
        'loc':list_of_comp,
        'details':details
    }
    return render(request,"index.html",data)

def about(request):
    return render(request,"about.html",{})

def services(request):
    return render(request,"services.html",{})

