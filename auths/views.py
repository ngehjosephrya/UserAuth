from django.shortcuts import render , redirect
from .forms import RegisterForm
from django.views import View

# Create your views here.
class SignupView(View):  #Sginup View get inputs from Signup Form ,refies its integrity and saves it
    template_name = 'sign_up.html'
    
    def get(self, request):
        form = RegisterForm()
        context = {'form':form}
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context = {'form':form}
        return render(request, self.template_name, context)
    
class homePage(View):
    template_name = 'home.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        return render(request)
    