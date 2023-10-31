from django.test import TestCase
from django.urls import reverse
from .models import Client
from accounts.models import User
from .forms import ClientCreationForm, ClientEditForm

class ClientTests(TestCase):
    def setUp(self):
        # Crie um usuário
        self.user = User.objects.create_user(
            email='testuser@example.com',
            full_name='Test User',
            password='testpassword',
        )

        # Crie um cliente associado ao usuário
        self.client = Client.objects.create(
            client_name='Test Client',
            email_primary='testclient@example.com',
            user=self.user,
        )

    def test_create_client_view(self):
        self.client.login(email='testuser@example.com', password='testpassword')
        response = self.client.post(reverse('create_client'), {
            'client_name': 'New Client',
            'email_primary': 'newclient@example.com',
            'user': self.user.id,
        })
        self.assertEqual(response.status_code, 302)  # Deve redirecionar para a página de detalhes do cliente
        new_client = Client.objects.get(client_name='New Client')
        self.assertEqual(new_client.email_primary, 'newclient@example.com')

    def test_edit_client_view(self):
        self.client.login(email='testuser@example.com', password='testpassword')
        response = self.client.post(reverse('edit_client', args=[self.client.id]), {
            'client_name': 'Updated Client',
            'email_primary': 'updatedclient@example.com',
        })
        self.assertEqual(response.status_code, 302)  # Deve redirecionar para a página de detalhes do cliente
        updated_client = Client.objects.get(pk=self.client.id)
        self.assertEqual(updated_client.client_name, 'Updated Client')
        self.assertEqual(updated_client.email_primary, 'updatedclient@example.com')

    def test_detail_client_view(self):
        self.client.login(email='testuser@example.com', password='testpassword')
        response = self.client.get(reverse('detail_client', args=[self.client.id]))
        self.assertEqual(response.status_code, 200)  # Deve retornar um código 200
        self.assertContains(response, 'Test Client')  # Verifica se o nome do cliente está na resposta

    def test_detail_client_view_with_associated_user_data(self):
        self.client.login(email='testuser@example.com', password='testpassword')
        response = self.client.get(reverse('detail_client', args=[self.client.id]))
        self.assertEqual(response.status_code, 200)  # Deve retornar um código 200
        self.assertContains(response, 'Test Client')  # Verifica se o nome do cliente está na resposta
        self.assertContains(response, 'testuser@example.com')  # Verifica se o email do usuário está na resposta
        self.assertContains(response, 'Test User')  # Verifica se o nome completo do usuário está na resposta
