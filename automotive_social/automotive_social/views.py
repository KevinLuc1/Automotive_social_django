from django.views.generic import TemplateView

class HomePage(TemplateView):
	template_name = 'index.html'

class LoggedInPage(TemplateView):
    template_name = 'login_msg.html'

class LoggedOutPage(TemplateView):
    template_name = 'logout_msg.html'
