from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test  # 🟢 ADD THIS LINE
from .models import Post
from .forms import PostForm

def index(request):
    all_posts = Post.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'posts': all_posts})

def post_detail(request, pk):
    post_item = get_object_or_404(Post, id=pk)
    return render(request, 'post.html', {'post': post_item})

# 🟢 ADD THIS PROTECTIVE FILTER LAYER (Only your superuser can enter!)
@user_passes_test(lambda u: u.is_superuser, login_url='/admin/login/')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})
