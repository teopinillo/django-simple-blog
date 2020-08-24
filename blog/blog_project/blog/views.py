from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from . models import Post

class BlogListView (ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView (DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class BlogCreateView (CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ['title','author','body']

class BlogUpdateView (UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView (DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    #we use reverse_lazy as opposed to just reverse so that it won't execute the URL redirect until our view has finishe
    #deleting the blog post
    success_url = reverse_lazy ('home')


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "blog/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "blog/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "blog/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "blog/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "blog/register.html")