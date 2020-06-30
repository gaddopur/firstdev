from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Article, ArticleComment
from django.contrib.auth.decorators import login_required
from . import forms
from articles.templatetags import extrafilter
from . import utils

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles':articles})

def article_details(request, slug, can_comment=False):
    article = Article.objects.get(slug=slug)
    comments = ArticleComment.objects.filter(post=article, parent=None)
    replies = ArticleComment.objects.filter(post=article).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.id not in replyDict.keys():
            replyDict[reply.parent.id] = [reply]
        else:
            replyDict[reply.parent.id].append(reply)

    comment = forms.CommentForm()
    context = {
        'article':article,
        'comment':comment,
        'comments':comments,
        'replyDict':replyDict
    }
    template = 'articles/article_details.html'
    return render(request, template, context)

@login_required(login_url = "/accounts/login")
def article_create(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.slug = utils.link_generator()
            instance.save()
            return redirect("articles:articles_list")
    else:
        form = forms.CreateArticle()
    return render(request, "articles/article_create.html", {'form':form})

@login_required(login_url = "/accounts/login")
def postcomment(request):
    if request.method == "POST":
        comment = forms.CommentForm(request.POST)
        if comment.is_valid():
            instance = comment.save(commit=False)
            instance.user = request.user
            post_slug = request.POST.get('post_slug')
            par_id = request.POST.get('par_id')
            if par_id != None:
                par_comment = ArticleComment.objects.get(id=par_id)
                instance.parent = par_comment
            post = Article.objects.get(slug=post_slug)
            instance.post = post
            instance.save();
            return redirect(post.get_absolute_url())
