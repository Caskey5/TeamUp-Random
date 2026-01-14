from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "base/additional_pages/about.html"

class ClientsView(TemplateView):
    template_name = "base/additional_pages/clients.html"

class ContactView(TemplateView):
    template_name = "base/additional_pages/contact.html"

class FooterView(TemplateView):
    template_name = "base/additional_pages/footer.html"

class MastheadView(TemplateView):
    template_name = "base/additional_pages/masthead.html"

class NavigationView(TemplateView):
    template_name = "base/additional_pages/navigation.html" 
    
class PortfolioGridView(TemplateView):
    template_name = "base/additional_pages/portfolio_grid.html"

class PortfolioModelsView(TemplateView):
    template_name = "base/additional_pages/portfolio_models.html"
    
class ServicesView(TemplateView):
    template_name = "base/additional_pages/services.html"

class TeamView(TemplateView):
    template_name = "base/additional_pages/team.html"