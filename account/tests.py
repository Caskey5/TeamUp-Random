from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from pages.models import Formation, TeamGeneration
from pages.services.team_generator import create_team_generation


class AccountFlowTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.formation = Formation.objects.get(slug='football_5_plus_1')

    def _create_generation(self):
        post_data = {
            'goalkeeper_1': 'GK1',
            'goalkeeper_2': 'GK2',
            **{f'player_{index}': f'Player {index}' for index in range(1, 11)},
        }
        return create_team_generation(self.formation, post_data)

    def test_anonymous_user_redirected_to_login_when_saving(self):
        generation = self._create_generation()
        client = Client()
        response = client.get(reverse('account:save_generation', kwargs={'pk': generation.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/account/login/', response['Location'])

    def test_authenticated_user_can_save_generation(self):
        user = User.objects.create_user(username='testuser', password='testpass123')
        generation = self._create_generation()
        client = Client()
        client.login(username='testuser', password='testpass123')

        response = client.get(reverse('account:save_generation', kwargs={'pk': generation.pk}))
        self.assertRedirects(response, reverse('account:history'))

        generation.refresh_from_db()
        self.assertTrue(generation.is_saved)
        self.assertEqual(generation.user, user)
        self.assertIsNotNone(generation.saved_at)

    def test_history_shows_only_own_saved_generations(self):
        owner = User.objects.create_user(username='owner', password='testpass123')
        other = User.objects.create_user(username='other', password='testpass123')

        saved_generation = self._create_generation()
        saved_generation.user = owner
        saved_generation.is_saved = True
        saved_generation.save()

        other_generation = self._create_generation()
        other_generation.user = other
        other_generation.is_saved = True
        other_generation.save()

        client = Client()
        client.login(username='owner', password='testpass123')
        response = client.get(reverse('account:history'))
        self.assertContains(response, 'Nogomet')
        self.assertEqual(len(response.context['generations']), 1)

    def test_cannot_view_other_users_saved_generation(self):
        owner = User.objects.create_user(username='owner', password='testpass123')
        other = User.objects.create_user(username='other', password='testpass123')

        generation = self._create_generation()
        generation.user = owner
        generation.is_saved = True
        generation.save()

        client = Client()
        client.login(username='other', password='testpass123')
        response = client.get(reverse('account:saved_generation', kwargs={'pk': generation.pk}))
        self.assertEqual(response.status_code, 404)

    def test_logout_redirects_to_home(self):
        User.objects.create_user(username='logoutuser', password='testpass123')
        client = Client()
        client.login(username='logoutuser', password='testpass123')

        response = client.get(reverse('account:logout'))
        self.assertRedirects(response, reverse('pages:home'))
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_register_and_login_flow(self):
        client = Client()
        response = client.post(
            reverse('account:register'),
            {
                'username': 'newuser',
                'email': 'new@example.com',
                'password1': 'ComplexPass123!',
                'password2': 'ComplexPass123!',
            },
        )
        self.assertRedirects(response, reverse('account:history'))
        self.assertTrue(User.objects.filter(username='newuser').exists())
