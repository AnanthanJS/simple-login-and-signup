from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from login_project import settings
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request,"login_app/index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        #form validation
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exists! Please try some other Username")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('home')
        
        if len(username)>10:
            messages.error(request, "Username must be less than 10 characters")
            
        if pass1 != pass2:
            messages.error(request, "Password doesnot match!")
            
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('home')
        
        #form validation end

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request,"Your Account has been created successfully.")
        
        
        #Welcome Mail
        
        subject = "Welcome to Ak's Login Page!!"
        message = "Hello" + myuser.first_name + "!\n" + "Thank you for visiting my login page \n I have also sent you a confirmation email, please confirm your email address in order to activate your account. \n\n Thanking you, Ak  "
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        

        return redirect('signin')

    return render(request,"login_app/signup.html")

def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "login_app/index.html", {'fname':fname})

        else:
            messages.error(request, "Bad credentials!")
            return redirect('home')
    return render(request,"login_app/signin.html")

def signout(request):
    
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')
