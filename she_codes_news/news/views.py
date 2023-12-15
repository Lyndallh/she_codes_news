from typing import Any
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from .forms import CommentForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
CustomUser = get_user_model()


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        # context for 'other_stories' that are not in the 'latest_stories' to be used on index.html so that stories are not shown twice
        context['other_stories'] = NewsStory.objects.all().order_by('-pub_date')[4:]
        return context

class AuthorView(generic.ListView):
    model = NewsStory
    template_name = 'news/author.html'
    context_object_name = "author_stories"
    slug_feild = 'username'
    slug_url_kwarg = 'username'

    def get_queryset(self):
        '''Return all authors stories.'''
        return NewsStory.objects.all().order_by('-pub_date').filter(author_id=self.kwargs.get("author_id"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username']= self.kwargs.get(CustomUser) 
        return context
    
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form']= CommentForm()
        return context

class AddStoryView(LoginRequiredMixin, generic.CreateView):
    login_url = 'login'
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddCommentView(generic.CreateView):
    
    form_class = CommentForm

    def get(self, request, *args, **kwargs):
        return redirect("news:story", pk=self.kwargs.get("pk"))

    def form_valid(self, form):
        form.instance.author = self.request.user
        pk = self.kwargs.get("pk")
        form.instance.story = get_object_or_404(NewsStory, pk=pk)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('news:story',kwargs=
        {'pk':self.kwargs.get("pk")})
                   
