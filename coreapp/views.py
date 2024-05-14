from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class IndexView:
  @staticmethod
  def index(request):
    return render(request, 'index.html', {})

@login_required(login_url='login')
class RestaurnantView:
  @staticmethod
  def index(request):
    return render(request, 'index.html', {})
