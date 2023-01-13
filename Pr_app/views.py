from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Pr_form
from .models import Property_detail

#  add our property


def All_Property(request):
    if request.method == "POST":
        formdata = Pr_form(request.POST)
        if formdata.is_valid():
            formdata.save()
            messages.success(request, 'Your Property added Successfully!')
            return redirect("/")
    else:
        formdata = Pr_form()

    # fetch all properties
    Properties = Property_detail.objects.all()

    context = {"form": formdata, "Porperties": Properties}
    return render(request, 'pr_app/Home.html', context)

# update property details


def Update_Property(request, id):
    Pr_data = Property_detail.objects.get(Pr_id=id)
    if request.method == "POST":
        formdata = Pr_form(request.POST, instance=Pr_data)
        if formdata.is_valid():
            formdata.save()
            messages.success(request, "Your Property Updated Successfully!")
            return redirect("/")

    else:
        formdata = Pr_form(instance=Pr_data)
    context = {"form": formdata}
    return render(request, "pr_app/Update.html", context)


# Fetch property by city name


def Fetch_Property(request):
    if request.method == "POST":
        cityname = request.POST['city']
        properties = Property_detail.objects.filter(City_name=cityname)
        context = {"properties": properties}
        return render(request, 'pr_app/Fetch_pr.html', context)

    return render(request, 'pr_app/Fetch_pr.html')


# fetch cities by state


def Find_cities(request):
    if request.method == "POST":
        statename = request.POST['state']
        cities = Property_detail.objects.filter(State_name=statename)
        context = {"cities": cities}
        return render(request, 'pr_app/Find_city.html', context)

    return render(request, 'pr_app/Find_city.html')


# find all similiar city name properties by propertyid

def Find_similiar_pr(request):
    if request.method == "POST":
        pr_id = request.POST['id']
        try:
            pr_data = Property_detail.objects.get(Pr_id=pr_id)
        except Exception:
            messages.warning(request, "Please give a valid id ! ")
            return redirect("Find_similiar")
        cityname = pr_data.City_name
        similiar_data = Property_detail.objects.filter(City_name=cityname)
        context = {"Similiar_city_data": similiar_data}
        return render(request, 'pr_app/Find_similiar.html', context)

    return render(request, 'pr_app/Find_similiar.html')
