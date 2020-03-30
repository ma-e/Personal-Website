from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
# from visits.models import Visits
from .models import Portfolio,Blog,Bio,Portfolio_game,Portfolio_painting,\
                    Portfolio_photo,Portfolio_other,Comment, Project, Post
def index(request):
    projects = Project.objects.all()
    portfolio = Portfolio.objects.all()
    blogs = Blog.objects.all()
    bio = Bio.objects.all()
    portfolio_game = Portfolio_game.objects.all()
    comments = Comment.objects.all()
    Posts = Post.objects.all()

    if request.method == "POST":
        if "volunteerSummit" in request.POST:
            v_form = Comment(name=request.POST.get("en_name"),\
                           email=request.POST.get("en_email"),\
                           content=request.POST.get("en_comment"),\
                           blog=request.POST.get("en_blog"))
            v_form.save()
        elif "seekerSummit" in request.POST:
            s_form = Post(name=request.POST.get("post_name"),\
                        email=request.POST.get("post_email"),\
                        content=request.POST.get("post_comment"),\
                        blog=request.POST.get("post_blog"))
            s_form.save()

    context = {
        "portfolios":portfolio,
        "blogs":blogs,
        "bio_images":bio,
        "comments":comments,
        "projects":projects,
        "posts":Posts,
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
    if name == "Data Visualization":
        return render(request,'personal/en_portfolio_game.html',context)
    elif name == "Painting":
        return render(request,'personal/en_portfolio_painting.html',context)
    elif name == "Photography":
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

# def some_object_view(request, pk):
#     Visits.objects.add_uri_visit(request, request.META["PATH_INFO"], APP_LABEL)