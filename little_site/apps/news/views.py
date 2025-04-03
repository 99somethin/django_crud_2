from django.shortcuts import render, redirect
from django.views import View
from .models import Articles
from .forms import NewsForm
from django.views.generic import DeleteView, UpdateView, DeleteView

# Create your views here.

class NewsMainPageView(View):
    def get(self, request, *args, **kwargs):
        news = Articles.objects.all()
        return render(request, 'news/index.html', context={'news': news})


class UpdateNewsPageView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = NewsForm


class DeleteNewsPageView(DeleteView):
    model = Articles
    template_name = 'news/news-delete.html'
    success_url = '/news/'

class CreatePageView(View):
    def get(self, request, *args, **kwargs):
        form = NewsForm()
        return render(request, 'news/create.html', context={'form': form})
    def post(self, request, *args, **kwargs):
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
        else:
            return render(request, 'news/create.html', {'form': form})
        

class SelectNewsPageView(DeleteView):
    model = Articles
    template_name = 'news/selectednews.html'
    context_object_name = 'article'

