from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404

from .models import Customer,help
from .admin_models import Admin , Product,Product_order

def home_page(request):
    return render(request,'index.html')

def about_page(request):
    return render(request,'about.html')

def contact_page(request):
    return render(request,'contact.html')

def customer_login_page(request):
    return render(request,'login.html')

def customer_signup_page(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        gender=request.POST.get("gen")
        state=request.POST.get("state")
        mobile=request.POST.get("mobile")
        photo=request.FILES.get("photo")
        addr=request.POST.get("address")
        Customer.objects.create(name=name,email=email,password=password,gender=gender,state=state,mobile=mobile,photo=photo,address=addr)
        messages.success(request,name+" Signup Successfully")
        return render(request,'signup.html')
    
    
def customer_login_page(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        try:
            customer=Customer.objects.get(email=email,password=password)
            request.session['customer_email']=customer.email
            request.session['customer_name']=customer.name 
            messages.success(request,f"Welcome {customer.name}")
            return redirect('customer_home')
        except Customer.DoesNotExist:
            messages.success(request,"Invalid Email-Id and Password")
            return render(request,'login.html')
    
    
def customer_home(request):
    if 'customer_email' not in request.session:
         messages.success(request,"Please Login First....")
         return render(request,'login.html')
    else:
        product_data=Product.objects.all()
        return render(request,'dashboard.html',{'data':product_data})

def customer_profile(request):
   if 'customer_email' not in request.session:
            messages.success(request,"Please Login First....")
            return render(request,'login.html') 
   else:
       email=request.session.get('customer_email')
       data=Customer.objects.get(email=email)
       return render(request,"myprofile.html",{'record':data})

def customer_order(request):
    email=request.session.get('customer_email')
    data=Product_order.objects.filter(customer_email=email)
    return render(request,'myorder.html',{'data':data})

def customer_tickets(request):
    if 'customer_email' not in request.session:
                messages.success(request,"Please Login First....")
                return render(request,'login.html') 
    else:
        if request.method=='GET':
            email=request.session.get('customer_email')
            record=help.objects.filter(customer_email=email)
            return render(request,'help.html',{'data':record})
        else:
            cust_email=request.session.get('customer_email')
            subj=request.POST.get('subject')
            query=request.POST.get('query')
            help.objects.create(subject=subj,query=query,customer_email=cust_email)
            messages.success(request,"Ticket Generated Successfully")
            return render(request,'help.html')
            

def customer_signout(request):
    storage=get_messages(request)
    storage.used=True
    request.session.flush()
    messages.success(request,"Logout Successfully")
    return render(request,'login.html')

def admin_login(request):
    if request.method=='GET':
            return render(request,'Admin_login.html')
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
            
        try:
            admin=Admin.objects.get(email=email,password=password)
            request.session['admin_email']=admin.email
            request.session['admin_name']=admin.name 
            messages.success(request,f"Welcome {admin.name}")
            return redirect('admin_home')
        except Admin.DoesNotExist:
            messages.success(request,"Invalid Email-Id and Password")
            return render(request,'Admin_login.html')

def admin_home(request):
    if 'admin_email' not in request.session:
             messages.success(request,"Please Login First....")
             return render(request,'Admin_login.html')
    else:
        return render(request,'adminhome.html')

def add_product(request):
    if 'admin_email' not in request.session:
                 messages.success(request,"Please Login First....")
                 return render(request,'Admin_login.html')
    else:
        if request.method=='GET':
            return render(request,'Add_Product.html')
        else:
            pname=request.POST.get('pname')
            ptype=request.POST.get('ptype')
            pprice=request.POST.get('pprice')
            pphoto=request.FILES.get("pphoto")
            pdesc=request.POST.get("pdesc")
            Product.objects.create(name=pname,type=ptype,price=pprice,photo=pphoto,description=pdesc)
            messages.success(request,pname+" Product Added Successfully")
            return render(request,'Add_Product.html')
            

def manage_product(request):
    if 'admin_email' not in request.session:
                     messages.success(request,"Please Login First....")
                     return render(request,'Admin_login.html')
    else:
        record=Product.objects.all()
        return render(request,'Manage_Product.html',{'data':record})
    
def delete_product(request,id):
    product=get_object_or_404(Product,id=id)
    product.delete()
    record=Product.objects.all()
    return render(request,'Manage_Product.html',{'data':record})


def close_ticket(request,rid):
    hl=get_object_or_404(help,id=rid)
    hl.delete()
    email=request.session.get('customer_email')
    record=help.objects.filter(customer_email=email)
    return render(request,'help.html',{'data':record})
    
    
def update_product(request):
    pid=request.POST.get('pid')
    pname=request.POST.get('pname')
    ptype=request.POST.get('ptype')
    pprice=request.POST.get('pprice')
    pphoto=request.FILES.get("pphoto")
    pdesc=request.POST.get('pdesc')
    
    product=get_object_or_404(Product,id=pid)
    product.name=pname
    product.type=ptype
    product.price=pprice
    if pphoto:
        product.photo=pphoto
    product.description=pdesc
    product.save()
    
    record=Product.objects.all()
    return render(request,'Manage_Product.html',{'data':record})
    
    

def admin_tickets(request):
    record=help.objects.all()
    return render(request,'Managetickets.html',{'data':record})

def admin_signout(request):
    storage=get_messages(request)
    storage.used=True
    
    request.session.flush()
    messages.success(request,"Logout Successfully")
    return render(request,'Admin_login.html')

def viewproduct(request,pid):
    data=Product.objects.get(id=pid)
    return render(request,'detail_product.html',{'data':data})

def buy_product(request):
    cust_email=request.session.get('customer_email')
    
    pid=request.POST.get('pid')
    total_qnty=request.POST.get('qnty')
    
    pr=Product.objects.get(id=pid)
    price=pr.price
    final_price=int(total_qnty)*int(price)
    
    Product_order.objects.create(customer_email=cust_email,name=pr.name,
                                 type=pr.type,qnty=total_qnty,price=final_price,
                                 photo=pr.photo,description=pr.description)
    return render(request,'detail_product.html',{'data':pr,'message':'Product Order Successfully'})
    
    