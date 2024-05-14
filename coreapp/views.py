from django.shortcuts import render

# Create your views here.
class IndexView:
  @staticmethod
  def index(request):
    return render(request, 'index.html', {})
