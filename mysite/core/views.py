from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .forms import PostForm
from .models import Book
from .models import Post
from .models import Question
from .forms import QuestionForm
from .models import Tutorials,TutorialCategory,TutorialSeries
from .models import CV
from .forms import CVsForms
# API code
from rest_framework import viewsets
from .serializers import BookSerializer# API code
from .serializers import PostSerializer
from .serializers import TutiCateSerializer, TutorialSeriesSerializer


#userprofile


# Create your views here.
def home(request):
    count = User.objects.count()
    return render(request,'home.html',{
        'count': count
    })

def signup(request):
    if request.method =='POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage_learn')
    else:
        form = NewUserForm
    return render(request,'registration/signup.html',{ 
        'form': form
    })
@login_required
def secret_page(request):
    return render (request,'secret_page.html')  
@login_required
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request,'upload.html',context)
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request,'book_list.html',{
        'books':books
    })
@login_required
def upload_book(request):
    if request.method=='POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request,'upload_book.html',{
        'form':form

    }
     
    )
@login_required
def create_post(request):
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request,'create_post.html',{
        'form':form

    }
     
    )
@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request,'posts_list.html',{
        'posts':posts
    })

@login_required
def create_question(request):
    if request.method=='POST':
        form = QuestionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request,'create_question.html',{
        'form':form

    }
     
    )
@login_required
def aboutMI(request):
    return render(request,"aboutMI.html")

def donate(request):
    return render(request,"donate.html")
@login_required
def Learn_more(request):
    return render(request,"learn_more.html")
@login_required
def homepage_learn(request):
    return render(request,"categories.html",context={"categories":TutorialCategory.objects.all()})
@login_required
def user_list(request):
    users = User.objects.all()
    return render(request,'user_list.html',{
        'users':users
    })
@login_required
def user_profile(request):
    users_profile = User.objects.all()
    return render(request,'user_profile.html',{
        'users_profile':users_profile
    })

@login_required
def cv_upload(request):
    if request.method=='POST':
        form = CVsForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<marquee>Cv uploaded Successfullys</marquee>")
    else:
        form = CVsForms()
    return render(request,'cvs.html',{
        'form':form

    })
#learning python code

def webDevelopment(request):
    numbers = [1,2,3,4,5,6,7,8]
    name = 'Web development by Emmanuel Mhetu'
    args = {'name_of_tutor':name,'numbers':numbers}
    return render(request,'learning/webdevelopment.html',args)
# API code for all models
#@login_required
class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
#@login_required
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class TutiCateView(viewsets.ModelViewSet):
    queryset = TutorialCategory.objects.all()
    serializer_class = TutiCateSerializer

class TutorialSeriesView(viewsets.ModelViewSet):
    queryset = TutorialSeries.objects.all()
    serializer_class = TutorialSeriesSerializer

#Function to edit user profile
def edit_profile(request):
    if request.method=='POST':
        form = NewUserForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/users_profile')
    else:
        form = NewUserForm(instance=request.user)
        args = {'form':form }
        return render(request,'edit_profile.html',args)
       