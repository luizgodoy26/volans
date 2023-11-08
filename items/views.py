from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Size, Category, Stock
from .forms import ItemForm, SizeForm, CategoryForm, StockForm

def is_manager(user):
    return user.manager



@login_required
def list_items(request):
    items = Item.objects.filter(user=request.user)
    return render(request, 'list_items.html', {'items': items})




@login_required
def list_sizes(request):
    sizes = Size.objects.filter(user=request.user)
    return render(request, 'list_sizes.html', {'sizes': sizes})



@login_required
def list_categories(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'list_categories.html', {'categories': categories})



@login_required
def list_stock(request):
    stocks = Stock.objects.filter(user=request.user)
    return render(request, 'list_stock.html', {'stocks': stocks})



@login_required
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('list_items')
    else:
        form = ItemForm()
    return render(request, 'create_item.html', {'form': form})



@login_required
def create_size(request):
    if request.method == 'POST':
        form = SizeForm(request.POST)
        if form.is_valid():
            size = form.save(commit=False)
            size.user = request.user
            size.save()
            return redirect('list_sizes')
    else:
        form = SizeForm()
    return render(request, 'create_size.html', {'form': form})



@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('list_categories')
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})



@login_required
def create_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.user = request.user
            stock.save()
            return redirect('list_stock')
    else:
        form = StockForm()
    return render(request, 'create_stock.html', {'form': form})



@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.user == item.user:
        if request.method == 'POST':
            form = ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('list_items')
        else:
            form = ItemForm(instance=item)
    else:
        return render(request, 'errors/error_page.html', {'message': 'Você não tem permissão para editar este item'})

    return render(request, 'edit_item.html', {'form': form, 'item': item})



@login_required
def edit_size(request, size_id):
    size = get_object_or_404(Size, pk=size_id)

    if request.user == size.user:
        if request.method == 'POST':
            form = SizeForm(request.POST, instance=size)
            if form.is_valid():
                form.save()
                return redirect('list_sizes')
        else:
            form = SizeForm(instance=size)
    else:
        return render(request, 'errors/error_page.html', {'message': 'Você não tem permissão para editar este tamanho'})

    return render(request, 'edit_size.html', {'form': form, 'size': size})



@login_required
def edit_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    if request.user == category.user:
        if request.method == 'POST':
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                return redirect('list_categories')
        else:
            form = CategoryForm(instance=category)
    else:
        return render(request, 'errors/error_page.html', {'message': 'Você não tem permissão para editar esta categoria'})

    return render(request, 'edit_category.html', {'form': form, 'category': category})



@login_required
def edit_stock(request, stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)

    if request.user == stock.user:
        if request.method == 'POST':
            form = StockForm(request.POST, instance=stock)
            if form.is_valid():
                form.save()
                return redirect('list_stock')
        else:
            form = StockForm(instance=stock)
    else:
        return render(request, 'errors/error_page.html', {'message': 'Você não tem permissão para editar este estoque'})

    return render(request, 'edit_stock.html', {'form': form, 'stock': stock})



@login_required
def detail_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'detail_item.html', {'item': item})