from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import CompanyCreationForm, CompanyEditForm
from .models import Company

@login_required
def create_company(request):
    if request.method == 'POST':
        form = CompanyCreationForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save()
            request.user.company = company
            request.user.save()
            return redirect('detail_company', company_id=company.id)

    else:
        form = CompanyCreationForm()
    return render(request, 'create_company.html', {'form': form})



@login_required
def edit_company(request, company_id):
    company = get_object_or_404(Company, pk=company_id)

    if request.user.company == company:
        if request.method == 'POST':
            form = CompanyEditForm(request.POST, instance=company)
            if form.is_valid():
                form.save()
                return redirect('detail_company', company_id=company_id)
        else:
            form = CompanyEditForm(instance=company)
    else:
        return render(request, 'errors/error_page.html', {'message': 'Você não tem permissão acessar esta página'})

    return render(request, 'edit_company.html', {'form': form, 'company': company})



@login_required
def detail_company(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    if request.user.company == company:
        return render(request, 'detail_company.html', {'company': company})
    return render(request, 'errors/error_page.html', {'message': 'Você não tem permissão para editar esta empresa'})