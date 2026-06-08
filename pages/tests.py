from django.core.exceptions import ValidationError
from django.test import Client, TestCase
from django.urls import reverse

from pages.models import Formation, SportChoice
from pages.services.team_generator import (
    build_teams,
    create_team_generation,
    parse_player_input,
    regenerate_teams,
    validate_player_input,
)


class TeamGeneratorTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        sport = SportChoice.objects.get(name='football')
        cls.formation = Formation.objects.create(
            slug='test_football',
            sport=sport,
            name='5 + 1',
            display_name='5 + 1',
            players_per_team=6,
            has_goalkeeper=True,
        )
        basketball = SportChoice.objects.get(name='basketball')
        cls.basketball_formation = Formation.objects.create(
            slug='test_basketball',
            sport=basketball,
            name='3v3',
            display_name='3v3',
            players_per_team=3,
            has_goalkeeper=False,
        )

    def test_parse_player_input_with_goalkeepers(self):
        post_data = {
            'goalkeeper_1': ' GK1 ',
            'goalkeeper_2': 'GK2',
            'player_1': 'Ana',
            'player_2': 'Ivan',
            'player_3': '',
        }
        goalkeepers, field_players = parse_player_input(post_data, has_goalkeeper=True)
        self.assertEqual(goalkeepers, ['GK1', 'GK2'])
        self.assertEqual(field_players, ['Ana', 'Ivan'])

    def test_validate_minimum_players(self):
        with self.assertRaises(ValidationError):
            validate_player_input(self.formation, ['GK1'], ['Ana', 'Ivan'])

    def test_build_teams_assigns_goalkeepers(self):
        teams = build_teams(
            self.formation,
            ['GK1', 'GK2'],
            [f'Player {index}' for index in range(1, 11)],
        )
        self.assertEqual(len(teams), 2)
        self.assertEqual(teams[0]['goalkeeper'], 'GK1')
        self.assertEqual(teams[1]['goalkeeper'], 'GK2')
        self.assertEqual(len(teams[0]['players']) + len(teams[1]['players']), 10)

    def test_create_and_regenerate_generation(self):
        post_data = {
            'goalkeeper_1': 'GK1',
            'goalkeeper_2': 'GK2',
            **{f'player_{index}': f'Player {index}' for index in range(1, 11)},
        }
        generation = create_team_generation(self.formation, post_data)
        self.assertEqual(generation.teams.count(), 2)
        first_split = [
            list(team.players.values_list('name', flat=True))
            for team in generation.teams.order_by('order')
        ]

        regenerate_teams(generation)
        second_split = [
            list(team.players.values_list('name', flat=True))
            for team in generation.teams.order_by('order')
        ]

        self.assertEqual(
            sorted(first_split[0] + first_split[1]),
            sorted(second_split[0] + second_split[1]),
        )

    def test_create_generation_without_goalkeepers(self):
        post_data = {f'player_{index}': f'Player {index}' for index in range(1, 7)}
        generation = create_team_generation(self.basketball_formation, post_data)
        self.assertEqual(generation.teams.count(), 2)
        self.assertFalse(
            generation.teams.first().players.filter(is_goalkeeper=True).exists()
        )


class FormationInputViewTests(TestCase):
    def test_football_input_creates_results(self):
        client = Client()
        post_data = {
            'goalkeeper_1': 'GK1',
            'goalkeeper_2': 'GK2',
            **{f'player_{index}': f'Player {index}' for index in range(1, 11)},
        }
        response = client.post(
            reverse('pages:first_football_formation_input'),
            post_data,
        )
        self.assertEqual(response.status_code, 302)
        results_response = client.get(response['Location'])
        self.assertContains(results_response, 'Timovi Generirani')
        self.assertContains(results_response, 'Tim 1')
