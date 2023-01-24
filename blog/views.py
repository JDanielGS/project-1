from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView
from .forms import PostCreateForm
from .models import post
from django.urls import reverse_lazy

# Create your views here.

class BlogListView(View):
    def get(self, request, *args, **kwargs):

        posts=post.objects.all()

        context = {

            'posts':posts

        }

        return render(request, 'BlogList.html', context)

class blogCreateView(View):
    def get(self, request, *args, **kwargs):
        form=PostCreateForm()
        context={
            'form':form
        }
        return render(request, 'blog_create.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            form=PostCreateForm(request.POST)
            
            if form.is_valid():
                title=form.cleaned_data.get('title')
                content=form.cleaned_data.get('content')

                p, created = post.objects.get_or_create(title=title, content=content)

                p.save()

                return redirect('blog:home')

        context={
            
        }
        return render(request, 'blog_create.html', context)

class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        Post=get_object_or_404(post, pk=pk)
        context={
            'post':Post
        }

        return render(request, 'blog_detail.html', context)

class BlogUpdateView(UpdateView):
    model=post
    fields=['title', 'content']
    template_name='blog_update.html'

    def get_success_url(self):
        pk=self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs={'pk':pk})

class BlogDeletView(DeleteView):
    model=post
    template_name='blog_delete.html'

    success_url=reverse_lazy('blog:home')