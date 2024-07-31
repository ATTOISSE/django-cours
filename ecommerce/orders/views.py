from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from django.views import View
from .models import Product
from .models import Client

def hello(request):
    products = Product.objects.all()
    lists = []
    for p in products:
        lists.append(f"<li>{p.wording}</li>")
    res = "".join(lists)
    html = f"""
        <ul>{res}</ul>
    """
    return HttpResponse(html)

def client_info(request,id):
    client = get_object_or_404(Client,id=id)
    # try:
    #     client = Client.objects.get(pk=id)
    # except Client.DoesNotExist:
    #     raise Http404('Le client n\'existe pas 404')
    orders_client = client.orders.all()[3]
    products = orders_client.products.all()
    divs =[
        f"""
            <div>
               <p>{p.wording.title()}</p> 
               <p>{p.price}</p> 
               <p>{p.is_disponibility}</p> 
            </div>
        """
        for p in products
    ]
    
    html = f"""
        <h3>Client</h3>
        <p>Nom : {client.first_name.title()} </p>
        <p>Prenom :{client.last_name.title()}</p>
        <h3>Commande</h3>
        <p>N° : {orders_client.command_number} </p>
        <p>Date : {orders_client.created_at} </p>
        <h3>Produits</h3>
        <div>
            {"".join(divs)}
        </div>
    """
    return HttpResponse(html)

class HomeView(View):
    def get(self,request):
        return HttpResponse('This is get')

def index(request):
    return render(request,'orders/index.html')

def get_client(request, id):
    client = get_object_or_404(Client,pk=id)
    if client:
        products = list()
        if client.orders.exists():
            orders = client.orders.all()
            for order in orders:
                products.extend(order.products.all())
        else:
            orders = None
    else:
        print('hello')
        return redirect(request,'not_found.html')
    
    return render(request,'orders/catalog.html',{'client':client,'orders':orders,'products':products})