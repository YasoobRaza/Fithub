from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from home.models import Product,Order,Plan,Blog
from datetime import date

# Create your views here.
def main(request):
    if request.user.is_anonymous:
        return render(request,'main.html',{"loged_out":True})

    return render(request, 'main.html')

def account(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print (user)
            return redirect("/main")
        else:
            messages.warning(request, " wrong username or password ")
            return render(request,'account.html')

    return render(request, 'account.html')

def logoutUser(request):
        logout(request)
        return redirect("/")

def signup(request):
    if request.method=="POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        try:
            user = User.objects.get(username=username)
            if user is not None:
                messages.warning(request, " Username already taken ")
                return render(request,'signup.html')
        except:
            pass

        if len(username)>15:
            messages.warning(request, " Your user name must be under 15 characters")
            return redirect("signup")

        elif not username.isalnum():
            messages.warning(request, " User name should only contain letters and numbers")
            return redirect("signup")
        
        elif (password1!= password2):
            messages.warning(request, " Passwords do not match")
            return redirect("signup")

        elif len(password1) < 8:
            messages.warning(request, " password sould be atleast 8 characters")
            return redirect("signup")
        
        user= User.objects.create_user(username,email, password1)
        login(request, user)
        messages.success(request, 'Your account has been created!')
        return redirect('/main')

    return render(request, 'signup.html')

def products(request):
    if request.user.is_anonymous:
        return redirect('/account')
    
    products=Product.objects.all()
    num=len(products)
    params={'products':products,'product_count':num,}
    return render(request,'product.html',params)

def plan(request):
    if request.user.is_anonymous:
        return redirect('/account')
    
    if request.method == "POST":
        messages.success(request, 'The plan has been Subscribed!')

    plan=Plan.objects.all()
    num=len(plan)
    params={'plan':plan,'plan_count':num,}
    return render(request,'plan.html',params)

def blog(request):
    if request.user.is_anonymous:
        return redirect('/account')
    
    blog=Blog.objects.all()
    num=len(blog)
    params={'blog':blog,'blog_count':num,}
    return render(request,'blog.html',params)

def order(request):
    thank=False
    if request.method=="POST":
        cart=request.POST.get("order-info")
        cart=eval(cart)
        phone= request.POST.get("phone")
        address= request.POST.get("address")

        order=Order.objects.create(order_date=date.today(),phone=phone,address=address,customer_id=request.user.id)
        for item in cart.values():
            order.products.add(item[0])
        messages.success(request, 'Your Order has been placed!')
        thank=True
        return render(request,'order.html',{"thank":thank})
        
    return render(request,'order.html',{"thank":thank})