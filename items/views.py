from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ItemCreationForm, ItemEditForm
from .models import Item

def is_manager(user):
    return user.manager



@login_required
def list_items(request):
    items = Item.objects.filter(user=request.user)
    return render(request, 'list_items.html', {'items': items})



@login_required
@user_passes_test(is_manager)  # Apenas usuários "gerentes" podem criar
def create_item(request):
    if request.method == 'POST':
        form = ItemCreationForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('detail_item', item_id=item.id)
    else:
        form = ItemCreationForm()
    return render(request, 'create_item.html', {'form': form})



@login_required
@user_passes_test(is_manager)  # Apenas usuários "gerentes" podem editar
def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.user == item.user:
        if request.method == 'POST':
            form = ItemEditForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('detail_item', item_id=item_id)
        else:
            form = ItemEditForm(instance=item)
    else:
        return render(request, 'errors/error_page.html', {'message': 'Você não tem permissão para editar este item'})

    return render(request, 'edit_item.html', {'form': form, 'item': item})



@login_required
def detail_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'detail_item.html', {'item': item})
