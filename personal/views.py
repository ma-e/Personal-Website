from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from .models import Portfolio,Blog,Bio,Portfolio_game,Portfolio_painting,\
                    Portfolio_photo,Portfolio_other,Comment
def index(request):
    portfolio = Portfolio.objects.all()
    blogs = Blog.objects.all()
    bio = Bio.objects.all()
    portfolio_game = Portfolio_game.objects.all()
    comments = Comment.objects.all() 
    if request.method == "POST":
        comment_ = Comment(name=request.POST.get("name"),\
                           email=request.POST.get("email"),\
                           content=request.POST.get("comment"),\
                           blog=request.POST.get("blog"))
        comment_.save()
    context = {
        "portfolios":portfolio,
        "blogs":blogs,
        "bio_images":bio,
        "comments":comments,
    }
    return render(request, 'personal/header.html', context)

# def blog_detail(request,name):
#     blogs = Blog.objects.all()
#     context = {
#         "blogs":blogs
#     }
#     return render(request,'personal/en_blog_detail.html',context)

def portfolio(request,name):
    portfolio = Portfolio.objects.all()
    context = {
        "portfolios":portfolio
    }
    if name == "game":
        return render(request,'personal/en_portfolio_game.html',context)
    elif name == "painting":
        return render(request,'personal/en_portfolio_painting.html',context)
    elif name == "photography":
        return render(request,'personal/en_portfolio_photo.html',context)
    else :
        return render(request,'personal/en_portfolio_other.html',context)



# def cn_portfolio_game(request,name="游戏"):
#     portfolio_game = Portfolio_game.objects.all()
#     context = {
#         "portfolio_game": portfolio_game
#     }
#     return render(request,'cn_portfolio_game.html',context)

# def cn_portfolio_painting(request,name):
#     portfolio_painting = Portfolio_painting.objects.all()
#     context = {
#         "portfolio_painting": portfolio_painting
#     }
#     return render(request,'cn_portfolio_painting.html',context)

# def cn_portfolio_photo(request,name):
#     portfolio_photo = Portfolio_photo.objects.all()
#     context = {
#         "portfolio_photo": portfolio_photo
#     }
#     return render(request,'cn_portfolio_photo.html',context)

# def cn_portfolio_other(request,name):
#     portfolio_other = portfolio_other.objects.all()
#     context = {
#         "portfolio_other": portfolio_other
#     }
#     return render(request,'cn_portfolio_other.html',context)
