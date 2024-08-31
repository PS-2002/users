from django.shortcuts import render, redirect
from .models import BlogPost
from .form import BlogPostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.doctor = request.user
            blog_post.save()
            return redirect('doctor_blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_blog_post.html', {'form': form})

@login_required
def doctor_blog_list(request):
    posts = BlogPost.objects.filter(doctor= request.user)
    return render(request, 'blog/doctor_blog_list.html', {'posts': posts})


@login_required
def patient_blog_list_by_category(request, category):
    posts = BlogPost.objects.filter(category=category, is_draft=False)
    return render(request, 'blog/blog_list_by_category.html', {'posts': posts, 'category': category})