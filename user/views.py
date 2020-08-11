from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, FormView

from user.forms import RegisterUserForm, LoginForm
from user.models import User


class RegisterUserView(CreateView):
    template_name = "user/register.html"
    model = User
    form_class = RegisterUserForm

    def get_success_url(self):
        messages.success(self.request, 'jestes zarejstrowany' )
        return reverse("login")

class LoginView(View):
    template_name = 'user/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        return render(request, self.template_name, {'form': LoginForm})

    def post(self, request):
        username: str = request.POST.get('username')
        password: str = request.POST.get('password')

        user: User or None= authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'jesteś zalogowany')
            return redirect('home')


        messages.error(request, 'nie znam takiego usera')
        return redirect('login')

def logout_view(request):
    logout(request)
    messages.success(request, 'zostałeś wylogowany')
    return redirect('home')

