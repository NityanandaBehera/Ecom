from django.shortcuts import redirect, render
from datetime import datetime
from .models import  products,Comment
from django.core.paginator import Paginator
from .forms import commentForm


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
