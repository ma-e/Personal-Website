from django.shortcuts import render,get_object_or_404
from .models import Portfolio,Blog,Bio,Portfolio_game,Portfolio_painting,Portfolio_photo,Portfolio_other

def cnIndex(request):
    portfolio = Portfolio.objects.all()
    blogs = Blog.objects.all()
    bio = Bio.objects.all()
    portfolio_game = Portfolio_game.objects.all()
    context = {
        "portfolios":portfolio,
        "blogs":blogs,
        "bio_images":bio,
    }
    return render(request, 'cn_main.html', context)

def cnBlog_detail(request,name):
    blogs = Blog.objects.all()
    context = {
        "blogs":blogs
    }
    return render(request,'cn_blog_detail.html',context)

def cn_portfolio(request,name):
    portfolio = Portfolio.objects.all()
    context = {
        "portfolios":portfolio
    }
    if name == "游戏":
        return render(request,'cn_portfolio_game.html',context)
    elif name == "彩铅":
        return render(request,'cn_portfolio_painting.html',context)
    elif name == "摄影":
        return render(request,'cn_portfolio_photo.html',context)
    else :
        return render(request,'cn_portfolio_other.html',context)



def cn_portfolio_game(request,name="游戏"):
    portfolio_game = Portfolio_game.objects.all()
    context = {
        "portfolio_game": portfolio_game
    }
    return render(request,'cn_portfolio_game.html',context)

def cn_portfolio_painting(request,name):
    portfolio_painting = Portfolio_painting.objects.all()
    context = {
        "portfolio_painting": portfolio_painting
    }
    return render(request,'cn_portfolio_painting.html',context)

def cn_portfolio_photo(request,name):
    portfolio_photo = Portfolio_photo.objects.all()
    context = {
        "portfolio_photo": portfolio_photo
    }
    return render(request,'cn_portfolio_photo.html',context)

def cn_portfolio_other(request,name):
    portfolio_other = portfolio_other.objects.all()
    context = {
        "portfolio_other": portfolio_other
    }
    return render(request,'cn_portfolio_other.html',context)
