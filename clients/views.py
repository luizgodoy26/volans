from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import ClientCreationForm, ClientEditForm
from .models import Client


#TODO: Adicionar filtros


@login_required
def list_clients(request):
    clients = Client.objects.filter(user=request.user)
    #contracts = Contract.objects.filter(user=request.user)
    #company_filter = CompanyFilter(request.GET, queryset=clients)


    #total_received = 0
    #total_pending = 0

    #for client in clients:
        #total_received += Contract.objects.filter(user=request.user, company_client=client, status='PD').aggregate(sum=Sum('value'))['sum'] or 0
        #total_pending += Contract.objects.filter(user=request.user, company_client=client, status='PN').aggregate(sum=Sum('value'))['sum'] or 0

        #client.received_payments = Contract.objects.filter(user=request.user, company_client=client, status='PD').aggregate(sum=Sum('value'))['sum'] or 0
        #client.pending_payments = Contract.objects.filter(user=request.user, company_client=client, status='PN').aggregate(sum=Sum('value'))['sum'] or 0

    client_count = Client.objects.filter(user=request.user).count()
    return render(request, 'list_clients.html', {'clients': clients,
                                                       #'company_filter': company_filter,
                                                       'client_count': client_count})




@login_required
def create_client(request):
    if request.method == 'POST':
        form = ClientCreationForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save(commit=False)
            client.user = request.user
            client.save()
            return redirect('detail_client', client_id=client.id)

    else:
        form = ClientCreationForm()
    return render(request, 'create_client.html', {'form': form})



@login_required
def edit_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    if request.user == client.user:
        if request.method == 'POST':
            form = ClientEditForm(request.POST, instance=client)
            if form.is_valid():
                form.save()
                return redirect('detail_client', client_id=client_id)
        else:
            form = ClientEditForm(instance=client)
    else:
        return render(request, 'errors/error_page.html', {'message': 'Você não tem permissão acessar esta página'})

    return render(request, 'edit_client.html', {'form': form, 'client': client})



@login_required
def detail_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.user == client.user:
        return render(request, 'detail_client.html', {'client': client})
    return render(request, 'errors/error_page.html', {'message': 'Você não tem permissão para editar esta empresa'})