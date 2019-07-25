from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Post
# from .models import PostListView

User = get_user_model()

def home(request):
	return render(request,"home.html",{})

@login_required
def announcement(request):
	context = {
		'posts':Post.objects.all()
	}
	return render(request,"announcement.html",context)

# def send_notification(request):
# 	return render(request,"send_notif.html")

class PostListView(ListView):
	model = Post
	template_name = 'announcement.html'#<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 6

class UserPostListView(ListView):
	model = Post
	template_name = 'user_posts.html'#<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	paginate_by = 1

	def get_queryset(self):
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title','content']
	template_name = 'post_form.html'

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title','content']
	template_name = 'post_form.html'
	
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/announcement'
	template_name = 'post_confirm_delete.html'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	from pages.namer import namer
	return render(request,"about.html",{"my_stuff":namer})

def contact(request):
	return render(request,"contact.html",{})

def register(request):
	return render(request,"register_user.html",{})
