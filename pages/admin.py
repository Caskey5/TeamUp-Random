from django.contrib import admin

from pages.models import Formation, GeneratedPlayer, GeneratedTeam, SportChoice, TeamGeneration


class GeneratedPlayerInline(admin.TabularInline):
    model = GeneratedPlayer
    extra = 0


class GeneratedTeamInline(admin.TabularInline):
    model = GeneratedTeam
    extra = 0
    show_change_link = True


@admin.register(SportChoice)
class SportChoiceAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'name')
    search_fields = ('display_name', 'name')


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'sport', 'players_per_team', 'has_goalkeeper', 'is_popular')
    list_filter = ('sport', 'has_goalkeeper', 'is_popular')
    search_fields = ('name', 'display_name', 'slug')


@admin.register(TeamGeneration)
class TeamGenerationAdmin(admin.ModelAdmin):
    list_display = ('formation', 'user', 'is_saved', 'total_players', 'created_at', 'saved_at')
    list_filter = ('is_saved', 'formation__sport', 'created_at')
    inlines = [GeneratedTeamInline]


@admin.register(GeneratedTeam)
class GeneratedTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'generation', 'order', 'player_count')
    inlines = [GeneratedPlayerInline]
