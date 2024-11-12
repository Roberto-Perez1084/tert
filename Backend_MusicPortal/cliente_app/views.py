from django.shortcuts import render
from .models import cliente

# Create your views here.

def index_view(request):
    clientes=cliente.objects.all()
    return render(request, 'manageCli.html',{'clt':clientes})

def saveCli(request):
    id_cliente=request.POST['txtid']
    nom_cliente=request.POST['txtnombre']
    apelli_cliente=request.POST['txtapellido']
    edad_cliente=request.POST['numedad']
    tel_cliente=request.POST['numtel']
    email_cliente=request.POST['txtemail']
    fech_reg=request.POST['datereg']

    guardarCli=cliente.objects.create(id_cliente=id_cliente,nom_cliente=nom_cliente,apelli_cliente=apelli_cliente,edad_cliente=edad_cliente,tel_cliente=tel_cliente,email_cliente=email_cliente,fech_reg=fech_reg)
    return redirect('/')

