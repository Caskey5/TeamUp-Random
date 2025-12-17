from django.views.generic import TemplateView

# Home page
class HomePageView(TemplateView):
    template_name = "base/home.html"



# Additional page views
class AboutView(TemplateView):
    template_name = "base/about.html"

class ClientsView(TemplateView):
    template_name = "base/clients.html"

class ContactView(TemplateView):
    template_name = "base/contact.html"

class FooterView(TemplateView):
    template_name = "base/footer.html"

class MastheadView(TemplateView):
    template_name = "base/masthead.html"

class NavigationView(TemplateView):
    template_name = "base/navigation.html"

class PortfolioGridView(TemplateView):
    template_name = "base/portfolio_grid.html"

class PortfolioModelsView(TemplateView):
    template_name = "base/portfolio_models.html"

class ServicesView(TemplateView):
    template_name = "base/services.html"

class TeamView(TemplateView):
    template_name = "base/team.html"


