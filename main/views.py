from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from main import models
from main import forms

def index(request):
    articles = models.Article.objects.all().order_by('-created_at')[:10]
    context = {
        "articles" : articles
    }
    return render(request, 'main/index.html', context)

def article(request,pk):
    article = get_object_or_404(models.Article, pk = pk)
    context = {
        "article" : article
    }
    return render(request, 'main/article.html', context)

def author(request,pk):
    try:
        author = models.Author.objects.get(pk=pk)
    except:
        raise Http404('Author doesnt exist ')

    context = {
        "author" : author
    }
    return render(request, 'main/author.html', context)

def create_article(request):
    form = forms.ArticleForm
    if request.method == "POST":
        form = forms.ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return HttpResponseRedirect('/')

    context = {
        "form" : form
    }
    return render(request, 'main/create_article.html', context)
