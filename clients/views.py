from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import ClientCreationForm, ClientEditForm
from .models import Client

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