from django.shortcuts import render,redirect
from .models import employee
from django.utils.dateparse import parse_date
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def create_employee(request):
    if request.method == 'POST':
        first_name = request.POST.get("FirstName")
        last_name = request.POST.get("LastName")
        email = request.POST.get("EmailId")
        mobile = request.POST.get("MobileNo")
        dob=request.POST.get("DOB")
        address=request.POST.get("Address")
        Gender = request.POST.get("rdbGender")
        country = request.POST.get("CountryId")
        city = request.POST.get("cityName")

        emp=employee()
        emp.first_name=first_name
        emp.last_name=last_name
        emp.email=email
        emp.mobile=mobile
        dob = parse_date(dob)
        emp.dob=dob
        emp.address=address
        emp.Gender=Gender
        emp.country=country
        emp.city=city
        emp.save()
        messages.success(request, 'Data submitted successfully!')
        return redirect("/employee/search_employee")
    return render(request, 'Employee/create_employee.html')

@login_required
def search_employee(request):
    emp = employee.objects.all()

    nameQuery = request.GET.get('nameQuery')
    mobileQuery = request.GET.get('mobileQuery')

    if nameQuery:
        words = nameQuery.split()
        query = Q()
        for word in words:
            query |= Q(first_name__icontains=word) | Q(last_name__icontains=word)
        emp = emp.filter(query)
    elif mobileQuery:
        emp = emp.filter(mobile__icontains=mobileQuery)
    paginator=Paginator(emp,6)
    page_num=request.GET.get('page')
    if not page_num:
        page_num = 1
    empdata=paginator.get_page(page_num)
    totalPages=empdata.paginator.num_pages

    return render(request, 'Employee/search_employee.html',{'emp':empdata,'totalPages':totalPages,'currentPage':page_num})

@login_required
def delete_employee(request,id):
    emp=employee.objects.get(pk=id)
    emp.delete()

    return redirect("/employee/search_employee")

@login_required
def update_employee(request,id):
    emp=employee.objects.get(pk=id)
    return render(request,"Employee/update_employee.html",{'emp':emp})

@login_required
def do_update_employee(request,id):
     first_name = request.POST.get("FirstName")
     email = request.POST.get("EmailId")
     last_name = request.POST.get("LastName")
     mobile = request.POST.get("MobileNo")
     dob=request.POST.get("DOB")
     address=request.POST.get("Address")
     Gender = request.POST.get("rdbGender")
     country = request.POST.get("CountryId")
     city = request.POST.get("cityName")

     emp=employee.objects.get(pk=id)
     emp.first_name=first_name
     emp.last_name=last_name
     emp.email=email
     emp.mobile=mobile
     dob = parse_date(dob)
     emp.dob=dob
     emp.address=address
     emp.Gender=Gender
     emp.country=country
     emp.city=city
     emp.save()
     messages.success(request, 'Data updated successfully!')
     return redirect("/employee/search_employee")




