from django.shortcuts import render
from .forms import LoginForm, RegistrationForm
from .models import AppUser
from datetime import datetime


# Create your views here.
def landing(request):
    context = {
        'page_content_title': 'Home Page',
        'msg_welcome': 'Welcome to Weather App.'
    }
    return render(request, "index.html")


def user_login(request):
    # creating form object
    lf = LoginForm()
    template = 'users/login.html'
    if request.method == "POST":
        # getting the user email from database
        user = AppUser.objects.get(email=request.POST.get('email'))
        if request.POST.get('password') == user.password:
            # storing user credentials in session
            request.session.setdefault('user_email', user.email)
            # request.session['user_email'] = user.email
            # request.session.update({"user_email": user.email})

            # checking the session value and redirecting it to index page
            if request.session.has_key("user_email"):
                template = "users/index.html"
                context = {
                    "form": lf,
                    "page_content_title": "User Dashboard",
                    "page_content_body": "Welcome to the Weather App Dashboard."
                }
                return render(request, template, context)
        else:
            context = {
                'form': lf
            }
            return render(request, template, context)
    else:
        context = {'form': lf}
        return render(request, template, context)


def user_logout(request):
    if request.session.has_key('user_email'):
        del request.session['user_email']
        login_form = LoginForm()
        template = "users/login.html"
        context = {
            'form': login_form
        }
        return render(request, template, context)


def user_register(request):
    template = "users/create.html"
    rf = RegistrationForm()
    if request.method == "POST":
        # creating AppUser Object
        # parametrized constructor
        user = AppUser(first_name=request.POST.get('first_name'),
                       middle_name=request.POST.get('middle_name'),
                       last_name=request.POST.get('last_name'),
                       email=request.POST.get('email'),
                       contact=request.POST.get('contact'),
                       dob=request.POST.get('dob'),
                       password=request.POST.get('password'),
                       address=request.POST.get('address'),
                       created_at=datetime.now())

        # Non parameterized constructor
        # user.first_name = request.POST.get('first_name')
        # user.middle_name = request.POST.get('middle_name')
        # user.last_name = request.POST.get('last_name')
        # user.email = request.POST.get('email')
        # user.contact = request.POST.get('contact')
        # user.dob = request.POST.get('dob')
        # user.password = request.POST.get('password')
        # user.address = request.POST.get('address')
        # user.created_at = datetime.now()

        # to store data
        user.save()

        context = {
            'form': rf,
            "success": "Registered Successfully"
        }
        return render(request, template, context)
    else:
        context = {'form': rf}
        return render(request, template, context)


def user_index(request):
    # render() - this function is used to render pages in django
    # takes three parameter
    # 1. request
    # 2. template
    # 3. data (which can be null) - must be a dict
    if request.session.has_key('user_email'):
        context = {"page_content_title": "User Dashboard",
                   "page_content_body": "Welcome to the Weather App Dashboard."}
        template = 'users/index.html'
        return render(request, template, context)
    else:
        lf = LoginForm()
        template = 'users/login.html'
        context = {'form': lf}
        return render(request, template, context)
