from django.views.generic import TemplateView

# Home page
class HomePageView(TemplateView):
    template_name = "base/home.html"



# Additional page views
class AboutView(TemplateView):
    template_name = "pages/about.html"

class ClientsView(TemplateView):
    template_name = "pages/clients.html"

class ContactView(TemplateView):
    template_name = "pages/contact.html"

class FooterView(TemplateView):
    template_name = "pages/footer.html"

class MastheadView(TemplateView):
    template_name = "pages/masthead.html"

class NavigationView(TemplateView):
    template_name = "pages/navigation.html"

class PortfolioGridView(TemplateView):
    template_name = "pages/portfolio_grid.html"

class PortfolioModelsView(TemplateView):
    template_name = "pages/portfolio_models.html"

class ServicesView(TemplateView):
    template_name = "pages/services.html"

class TeamView(TemplateView):
    template_name = "pages/team.html"


