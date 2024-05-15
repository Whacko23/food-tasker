from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from .models import Restaurant
from .forms import RestaurantForm

class IndexView(TemplateView):
    template_name = 'index.html'

class RestaurantView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = 'login'

class RestaurantSignupView(LoginRequiredMixin, CreateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'restaurant/signup.html'
    success_url = reverse_lazy('signup_success')
    login_url = 'login'

    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session['signed_up'] = True
        return response

class SignupSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'restaurant/signup_success.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('signed_up', False):
            return redirect('index')
        
        del request.session['signed_up']
        return super().dispatch(request, *args, **kwargs)
