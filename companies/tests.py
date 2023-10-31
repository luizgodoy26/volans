from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Company

class CompanyTest(TestCase):
    def setUp(self):
        # Crie um usuário de teste
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            full_name='Test User',
            password='testpassword'
        )
        self.client.login(username='testuser@example.com', password='testpassword')

    def test_create_company_view(self):
        response = self.client.post(reverse('create_company'), {
            'company_name': 'New Company',
            'cnpj': '98765432109876',
            'address': '456 Elm St',
            'city': 'New City',
            'neighborhood': 'New Neighborhood',
            'logo': '',
            'bio': 'New bio'
        })
        self.assertEqual(response.status_code, 200)  # Deve retornar 200 para sucesso

    def test_edit_company_view(self):
        # Crie uma empresa associada ao usuário
        company = Company.objects.create(
            company_name='Test Company',
            cnpj='12345678901234',
            address='123 Main St',
            city='City',
            neighborhood='Neighborhood',
            logo='',
            bio='Test bio',
            user=self.user
        )

        response = self.client.post(reverse('edit_company', args=[company.pk]), {
            'company_name': 'Updated Company',
            'address': 'Updated Address',
            'city': 'Updated City',
            'neighborhood': 'Updated Neighborhood',
            'logo': '',
            'bio': 'Updated bio'
        })
        self.assertEqual(response.status_code, 200)  # Deve retornar 200 para sucesso

    def test_detail_company_view(self):
        # Crie uma empresa associada ao usuário
        company = Company.objects.create(
            company_name='Test Company',
            cnpj='12345678901234',
            address='123 Main St',
            city='City',
            neighborhood='Neighborhood',
            logo='',
            bio='Test bio',
            user=self.user
        )

        response = self.client.get(reverse('detail_company', args=[company.pk]))
        self.assertEqual(response.status_code, 200)  # Deve retornar 200 para sucesso

    def test_edit_company_view_without_permission(self):
        # Crie outro usuário sem empresa associada
        user2 = get_user_model().objects.create_user(
            email='testuser2@example.com',
            full_name='Test User 2',
            password='testpassword2'
        )
        self.client.login(username='testuser2@example.com', password='testpassword2')

        # Tente acessar a página de edição da empresa do primeiro usuário (não deve ter permissão)
        # Aqui é esperado um redirecionamento para uma página de erro (código 302)
        response = self.client.get(reverse('edit_company', args=[self.user.company.pk]))
        self.assertEqual(response.status_code, 302)

    def test_detail_company_view_without_permission(self):
        # Crie outro usuário sem empresa associada
        user2 = get_user_model().objects.create_user(
            email='testuser2@example.com',
            full_name='Test User 2',
            password='testpassword2'
        )
        self.client.login(username='testuser2@example.com', password='testpassword2')

        # Tente acessar a página de detalhes da empresa do primeiro usuário (não deve ter permissão)
        # Aqui é esperado um redirecionamento para uma página de erro (código 302)
        response = self.client.get(reverse('detail_company', args=[self.user.company.pk]))
        self.assertEqual(response.status_code, 302)
