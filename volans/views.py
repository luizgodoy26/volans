from django.shortcuts import render


def forbidden_access(request, message="Oops! Você não tem acesso à esta página."):
    context = {'message': message}
    return render(request, 'errors/forbidden_access.html', context)