from django.shortcuts import render, redirect
from app_poll.models import  User

# Create your views here.
def index(request):
    return render(request,'index.html')

def login_user(request):
    try:
        request.session['email']
        session_user_data = User.objects.get(email = request.session['email'])
        return render(request,'index.html',{'user_data':session_user_data})
    except:
        if request.method == 'POST':
            try:
                uid = User.objects.get(email = request.POST['email'])
                if request.POST['password'] ==  uid.password:
                    request.session['email'] = request.POST['email']
                    session_user_data = User.objects.get(email = request.session['email'])
                    return render(request, 'poll_list.html')
                else:
                    return render(request, 'login.html',{'msg':'Password Incorrect!!'})
            except:
                return render(request, 'login.html', {'msg':'Email is not Registered!!'})
        return render(request, 'login.html')

def logout_user(request):
    return render(request, 'login.html')


def create_user(request):
    if request.method == 'POST':
        try:
            User.objects.get(email = request.POST['email'])
            return render(request, 'register.html',{'msg':'Email is already registered'})
        except:
            User.objects.create(
                fullname = request.POST['fname'],
                email = request.POST['email'],
                password = request.POST['password'],
            )
            return render(request, 'register.html', {'msg': 'Successfully Registered!!'})
    else:
        return render(request, 'register.html')

def polls_list(request):
    return render(request,'poll_list.html')