from django.shortcuts import render, redirect
from .forms import AttendForm, SignUpForm
import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from .models import Attendance, Date, CustomUser

def signupfunc(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        raw_password = request.POST['password']
        user = authenticate(username=username, password=raw_password)
        if user is not None:
            login(request, user)
            return redirect('index')            
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def indexfunc(request):
    if request.method == "POST":
        form = AttendForm(request.POST)
        object = Attendance.objects.all()
        user = request.user
        if form.is_valid():
            object = form.save(commit=False)
            object.user_id = user.id
            object.time = datetime.datetime.now().time()
            object.save()
            return redirect('result', pk=object.pk)
    else:
        form = AttendForm()
    return render(request, 'index.html', {'form': form})

def resultfunc(request, pk):
    object = Attendance.objects.get(pk=pk)
    return render(request, 'result.html', {'object':object})

def listfunc(request):
    # object = Date.objects.all()
    object = Date.objects.all()
    # attend_object = Attendance.objects.all()
    # print(attend_object[0].time)
    # print(object[0].attendance_set.get(id=1).attend)
    # print(object[0].attenddate)

    return render(request, 'list.html', {'object':object})