from django.shortcuts import render
from django.views import View

# Create your views here.

class MainPageView(View):

    def get(self, request, *args, **kwargs):
        data = {
            'title': 'Главная страница',
            'values': ['some text', 'hello']
        }

        return render(request, 'main/index.html', data)
    

class AboutPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'main/about.html')
