from django.shortcuts import render, redirect
from users.forms import UserForm
from users.forms import ReservationForm
from users.models import User
from users.models import Reservation

# USERS
def emp(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = UserForm()
    return render(request,'index.html',{'form':form})

def showuser(request):
    users = User.objects.all()
    return render(request,"show.html",{'users':users})

def edituser(request, id):
    user = User.objects.get(id=id)
    return render(request,'edit.html', {'user':user})

def updateuser(request, id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST, instance = user)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'update.html', {'user': user})

def destroyuser(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/show")

# RESERVATIONS

def showreserv(request):
    reservs = Reservation.objects.all()
    return render(request,"reservations.html",{'reservations':reservs})

def editreserv(request, id):
    reserv = Reservation.objects.get(id=id)
    return render(request,'editreservation.html', {'reservation':reserv})

def updatereserv(request, id):
    reserv = Reservation.objects.get(id=id)
    form = ReservationForm(request.POST, instance = reserv)
    if form.is_valid():
        form.save()
        return redirect("/reservations")
    return render(request, 'updatereservation.html', {'reservation': reserv})

def destroyreserv(request, id):
    reserv = Reservation.objects.get(id=id)
    reserv.delete()
    return redirect("/reservations")
