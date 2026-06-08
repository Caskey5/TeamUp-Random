from django.db import migrations


SPORTS = [
    ('football', 'Nogomet'),
    ('basketball', 'Košarka'),
    ('tennis', 'Tenis'),
    ('volleyball', 'Odbojka'),
    ('handball', 'Rukomet'),
]

FORMATIONS = [
    ('football_5_plus_1', 'football', '5 + 1', '5 + 1', 6, True, 'Idealno za male terene. 5 igrača u polju + 1 golman.', False),
    ('football_4_plus_1', 'football', '4 + 1', '4 + 1', 5, True, 'Najčešća opcija za mali nogomet. 4 igrača u polju + golman.', True),
    ('football_10_plus_1', 'football', '10 + 1', '10 + 1', 11, True, 'Standardna formacija za veliki teren. 10 igrača + golman.', False),
    ('basketball_6v6', 'basketball', '6v6', '6v6', 6, False, 'Puni teren sa rotacijama. 6 igrača po timu.', False),
    ('basketball_3v3', 'basketball', '3v3', '3v3', 3, False, 'Streetball format - brza i dinamična igra.', True),
    ('tennis_2v2', 'tennis', '2v2', 'Parovi (2v2)', 2, False, 'Tenis u parovima - dinamična timska igra.', False),
    ('handball_6_plus_1', 'handball', '6 + 1', '6 + 1', 7, True, 'Standardna rukometna formacija - 6 igrača u polju + golman.', True),
    ('handball_4_plus_1', 'handball', '4 + 1', '4 + 1', 5, True, 'Mala dvorana - 4 igrača u polju + golman.', False),
    ('volleyball_6v6', 'volleyball', '6v6', '6v6', 6, False, 'Standardna odbojka - 6 igrača po timu.', True),
    ('volleyball_4v4', 'volleyball', '4v4', '4v4', 4, False, 'Brža igra na manjem terenu.', False),
    ('volleyball_2v2', 'volleyball', '2v2', '2v2', 2, False, 'Beach volleyball format.', False),
]


def seed_data(apps, schema_editor):
    SportChoice = apps.get_model('pages', 'SportChoice')
    Formation = apps.get_model('pages', 'Formation')

    sport_map = {}
    for name, display_name in SPORTS:
        sport, _ = SportChoice.objects.get_or_create(
            name=name,
            defaults={'display_name': display_name},
        )
        sport_map[name] = sport

    for slug, sport_name, name, display_name, players_per_team, has_goalkeeper, description, is_popular in FORMATIONS:
        Formation.objects.get_or_create(
            slug=slug,
            defaults={
                'sport': sport_map[sport_name],
                'name': name,
                'display_name': display_name,
                'players_per_team': players_per_team,
                'has_goalkeeper': has_goalkeeper,
                'description': description,
                'is_popular': is_popular,
            },
        )


def unseed_data(apps, schema_editor):
    Formation = apps.get_model('pages', 'Formation')
    SportChoice = apps.get_model('pages', 'SportChoice')
    Formation.objects.filter(slug__in=[item[0] for item in FORMATIONS]).delete()
    SportChoice.objects.filter(name__in=[item[0] for item in SPORTS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_generatedteam_formation_generatedplayer_and_more'),
    ]

    operations = [
        migrations.RunPython(seed_data, unseed_data),
    ]
