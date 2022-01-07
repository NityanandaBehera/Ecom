from django.http import request
from django.shortcuts import redirect, render
from datetime import datetime
from .models import  products,Comment
from django.core.paginator import Paginator
from .forms import commentForm
from django.contrib import auth
from django.contrib.auth.models import User





def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('Username exists! try another username...')
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    print('Email is already taken! try another one')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username, email=email, password1=password2)
                    user.save()
                    return redirect('login')   
        else:
            print('Password did not matched!..')
            return redirect('signup')
    else:
        return render(request, 'signup.html') 
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            print('Login Successfull!')
            return redirect('home')
        else:
            print('invalid credentials')
            return redirect('login') 
    else:
        return render(request, 'login.html')           


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print('logged out from websites..')
        return redirect('login')
def home(request):
    return render(request,'home.html')
def index(request):
    product_objects=products.objects.all()
    item_name=request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        product_objects=product_objects.filter(title__icontains=item_name)
    paginator = Paginator(product_objects,4)
    page_number=request.GET.get('page')
    product_objects=paginator.get_page(page_number)


    return render(request,'index.html',{'product_objects':product_objects})
    
def Details(request,id):
    product_objects=products.objects.get(id=id)
    print(product_objects)
    return render(request,'detail.html',{'product_objects':product_objects})

def add_comment(request,id):
    product_objects=products.objects.get(id=id)
    form=commentForm(instance=product_objects)
    if request.method=="POST":
        form=commentForm(request.POST,instance=product_objects)
        if form.is_valid():
            name=request.user.username
            body=form.cleaned_data['comment_body']
            c=Comment(product=product_objects,commenter_name=name,comment_body=body,date_added=datetime.now())
            c.save()
            return redirect('index')
        else:
            print('form is invalid')
    
    context={
        'form':form
    }
    return render(request,'add_comment.html',context)


# Create your views here.
