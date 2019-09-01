from django.shortcuts import render,get_object_or_404
from .models import Portfolio,Blog,Bio

def cnIndex(request):
    portfolios = Portfolio.objects.all()
    blogs = Blog.objects.all()
    bio_imgs = Bio.objects.all()
    context = {
        "portfolios":portfolios,
        "blogs":blogs,
        "bio_images":bio_imgs,
    }
    return render(request, 'cn_main.html', context)

def cnBlog_detail(request,name):
    blogs = Blog.objects.all()
    context = {
        "blogs":blogs
    }
    return render(request,'cn_blog_detail.html',context)