from django.http import request
from django.shortcuts import render,redirect
from . models import Product,Card,OrderPlaced,Customer
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout,hashers
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import RegisterForm,LoginForm,ProfileForm
from app import forms


def home(request):
 topwear=Product.objects.filter(category= 'TW' )
 bottomwear=Product.objects.filter(category='BW')
 mobile=Product.objects.filter(category='M')
 
 return render(request, 'app/home.html',{'topwear':topwear,'bottomwear':bottomwear,'mobile':mobile})

# class product_detailView(View):
#     if request.user.is_authenticated:
#         def get(self,request,pk):

#             product=Product.objects.get(pk=pk)
        
#             return render(request, 'app/productdetail.html',{'product':product})
#         else:   
#             return redirect('/login')


def product_detailView(request,pk):
    if request.user.is_authenticated:
        

        product=Product.objects.get(pk=pk)
        
        return render(request, 'app/productdetail.html',{'product':product})
    else:   
        return redirect('/login')


       

class RegisterView(View):
    def get(self,request):

        form= RegisterForm()
 
        return render(request,'app/customerregistration.html',{'form':form})
    def post(self,request):

        form= RegisterForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request, 'Registration complited!...')
            # messages.SUCCESS(request,'congratulations registration successfully complited...')
            return redirect('/login/')
        return render(request,'app/customerregistration.html',{'form':form})






class LoginView(View):
    form= LoginForm()
    def get(self,request):

        
 
        return render(request,'app/login.html',{'form':self.form})
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect('/')
            else:
                messages.info(request, 'username and pasword not match ...')
                return redirect('/registration/')
        else:
            return render(request,'app/login.html',{'form':self.form})
            

        
def add_to_cart(request):
    if request.user.is_authenticated:
        user=request.user
        prod=request.GET.get('prod_id')
        product=Product.objects.get(id=prod)
        Card(user=user,product=product).save()
        return redirect('/showcart')
    else:
        return redirect('/')
    
def showcart(request):
    if request.user.is_authenticated:
        pro=Card.objects.filter(user=request.user)
        amount=0.0
        shiping_charge=40.0
        total_amount=0.0
        shiping_discount = 0.0
        current_user_cart=[i for i in Card.objects.all() if i.user == request.user]
        
            
               
        if current_user_cart:
            
            for p in current_user_cart:
                if p.product.discounted_price < 499:
                    tepAmount=(p.quantity * p.product.discounted_price)
                    amount+=tepAmount
                    
                   
                    shiping_charge = 40.0
                    total_amount=amount+shiping_charge
                else:
                    tepAmount=(p.quantity * p.product.discounted_price)
                    amount+=tepAmount
                    total_amount=amount
                    shiping_discount = 40
                    
        

        return render(request, 'app/addtocart.html',{'pro':pro,'total_amount':total_amount,'shiping':shiping_charge,'amount':amount,'shiping_discount':shiping_discount})
    else:
        redirect('/login/')


def buy_now(request):
    if request.user.is_authenticated:
        pro=Card.objects.filter(user=request.user)
        amount=0.0
        shiping_charge=40.0
        total_amount=0.0
        shiping_discount = 0.0
        current_user_cart=[i for i in Card.objects.all() if i.user == request.user]
        
            
               
        if current_user_cart:
            
            for p in current_user_cart:
                if p.product.discounted_price < 499:
                    tepAmount=(p.quantity * p.product.discounted_price)
                    amount+=tepAmount
                    
                   
                    shiping_charge = 40.0
                    total_amount=amount+shiping_charge
                else:
                    tepAmount=(p.quantity * p.product.discounted_price)
                    amount+=tepAmount
                    total_amount=amount
                    shiping_discount = 40
                    
        

        return render(request, 'app/buynow.html',{'pro':pro,'total_amount':total_amount,'shiping':shiping_charge,'amount':amount,'shiping_discount':shiping_discount})
    else:
        redirect('/login/')
 
 

class PrifileView(View):
    
    form=ProfileForm()
    def get(self,request):
            
        return render(request, 'app/profile.html',{'form':self.form,'active':'btn-primary'})
   
    def post(self,request):
        if request.user.is_authenticated:
            form=ProfileForm(request.POST)
            if form.is_valid():
                user=request.user
                name=form.cleaned_data['name']
                city=form.cleaned_data['city']
                locality=form.cleaned_data['locality']
                state=form.cleaned_data['state']
                
                zipcode=form.cleaned_data['zipcode']
                data=Customer(user= user,name=name,locality=locality,city=city ,state=state,zipcode=zipcode)
                data.save()
                return redirect('/address') 
            else:
                return redirect('/profile')    
        return render(request, 'app/profile.html',{'form':self.form,'active':'btn-primary'})
def address(request):
    data=Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'data':data,'active':'btn-primary'})

    

def orders(request):
    if request.user.is_authenticated:
        all=OrderPlaced.objects.filter(user=request.user)
        return render(request, 'app/orders.html',{'all':all})
    else:
        return redirect('/')


def change_password(request):
 return render(request, 'app/changepassword.html')


# filter mobile through category
def mobile(request , data=None):
    if data == None:
        mobiles=Product.objects.filter(category='M')
        return render(request, 'app/mobile.html',{'mobiles':mobiles})
    
    else:
        return render(request, 'app/mobile.html',{'mob':"No  Smartphone Available" })

# filter topwear through category
def topwear(request , data=None):
    if data == None:
        topwears=Product.objects.filter(category='TW')
        return render(request, 'app/topwear.html',{'topwears':topwears})
    
    else:
        return render(request, 'app/topwear.html',{'mob':"No  Smartphone Available" })


# filter bottomwear through category
def bottomwear(request , data=None):
    if data == None:
        bottomwears=Product.objects.filter(category='BW')
        return render(request, 'app/botomwear.html',{'bottomwears':bottomwears})
    
    else:
        return render(request, 'app/botomwear.html',{'mob':"No  Smartphone Available" })


# filter laptop through category
def laptop(request , data=None):
    if data == None:
        laptops=Product.objects.filter(category='L')
        return render(request, 'app/laptop.html',{'laptops':laptops})
    
    else:
        return render(request, 'app/laptop.html')




# Create your views here.
def pmode(request):
    return render(request,'app/payment_page.html')

def checkout(request):
    if request.user.is_authenticated:
        user=request.user
        add=Customer.objects.filter(user=user)
        card_item=Card.objects.filter(user=user)
        amount=0.0
        shiping_charge=40.0
        total_amount=0.0
        shiping_discount = 0.0
        current_user_cart=[i for i in Card.objects.all() if i.user == request.user]
            
                
                
        if current_user_cart:
            # print(current_user_cart)
            for p in current_user_cart:
                if p.product.discounted_price < 499:
                    tepAmount=(p.quantity * p.product.discounted_price)
                    amount+=tepAmount
                        
                    
                    shiping_charge = 40.0
                    total_amount=amount+shiping_charge
                else:
                    tepAmount=(p.quantity * p.product.discounted_price)
                    amount+=tepAmount
                    total_amount=amount               
    else:
        return redirect('/')        

    return render(request, 'app/checkout.html',{'add':add,'card_item':card_item,'total_amount':total_amount})
 
  
def user_logout(request):
    logout(request)
    # Redirect to a success page.
    messages.success(request,'Logout Succesfully')
    return redirect('/')
def payment_done(request):
    user=request.user
    cust=request.GET.get('custid')
    custm=Customer.objects.get(id=cust)
    cart=Card.objects.filter(user=request.user)
    for c in cart:
        OrderPlaced(user=user,customer=custm,product=c.product,quantity=c.quantity).save()
        c.delete()
    messages.success(request, ' congratulations Order palaced!...')    
    return redirect('orders')
