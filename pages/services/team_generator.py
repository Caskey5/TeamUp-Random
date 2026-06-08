import random

from django.core.exceptions import ValidationError
from django.db import transaction

from pages.models import Formation, GeneratedPlayer, GeneratedTeam, TeamGeneration


def _clean_names(values):
    seen = set()
    cleaned = []
    for value in values:
        name = value.strip()
        if not name:
            continue
        key = name.lower()
        if key in seen:
            continue
        seen.add(key)
        cleaned.append(name)
    return cleaned


def parse_player_input(post_data, has_goalkeeper):
    goalkeepers = []
    if has_goalkeeper:
        goalkeepers = _clean_names([
            post_data.get('goalkeeper_1', ''),
            post_data.get('goalkeeper_2', ''),
        ])

    field_players = _clean_names(
        value for key, value in post_data.items()
        if key.startswith('player_')
    )

    return goalkeepers, field_players


def validate_player_input(formation, goalkeepers, field_players):
    if formation.has_goalkeeper:
        if len(goalkeepers) < 2:
            raise ValidationError('Unesi imena oba golmana.')
    else:
        if goalkeepers:
            raise ValidationError('Ova formacija ne koristi golmane.')

    min_field = formation.players_per_team * 2
    if formation.has_goalkeeper:
        min_field -= 2

    if len(field_players) < min_field:
        raise ValidationError(
            f'Potrebno je najmanje {min_field} igrača u polju za ovu formaciju.'
        )


def _split_players(players):
    shuffled = players[:]
    random.shuffle(shuffled)
    midpoint = len(shuffled) // 2
    if len(shuffled) % 2:
        midpoint += 1
    return shuffled[:midpoint], shuffled[midpoint:]


def build_teams(formation, goalkeepers, field_players):
    if formation.has_goalkeeper:
        team_one_field, team_two_field = _split_players(field_players)
        return [
            {'goalkeeper': goalkeepers[0], 'players': team_one_field},
            {'goalkeeper': goalkeepers[1], 'players': team_two_field},
        ]

    team_one, team_two = _split_players(field_players)
    return [
        {'goalkeeper': None, 'players': team_one},
        {'goalkeeper': None, 'players': team_two},
    ]


@transaction.atomic
def create_team_generation(formation, post_data):
    goalkeepers, field_players = parse_player_input(post_data, formation.has_goalkeeper)
    validate_player_input(formation, goalkeepers, field_players)

    generation = TeamGeneration.objects.create(
        formation=formation,
        goalkeepers=goalkeepers,
        field_players=field_players,
    )
    _save_teams(generation, build_teams(formation, goalkeepers, field_players))
    return generation


@transaction.atomic
def regenerate_teams(generation):
    formation = generation.formation
    teams_data = build_teams(
        formation,
        generation.goalkeepers,
        generation.field_players,
    )
    generation.teams.all().delete()
    _save_teams(generation, teams_data)
    return generation


def _save_teams(generation, teams_data):
    icon = generation.formation.sport_icon
    for index, team_data in enumerate(teams_data, start=1):
        team = GeneratedTeam.objects.create(
            generation=generation,
            name=f'{icon} Tim {index}',
            order=index,
        )
        order = 1
        if team_data['goalkeeper']:
            GeneratedPlayer.objects.create(
                team=team,
                name=team_data['goalkeeper'],
                is_goalkeeper=True,
                order=order,
            )
            order += 1

        for player_name in team_data['players']:
            GeneratedPlayer.objects.create(
                team=team,
                name=player_name,
                is_goalkeeper=False,
                order=order,
            )
            order += 1
