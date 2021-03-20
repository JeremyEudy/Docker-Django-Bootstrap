from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from generics.views import BaseView
import subprocess

class HomeView(BaseView):
    template_name = 'home.html'
    fortune = "/usr/games/fortune -s"

    def get(self, request, *args, **kwargs):
        motd = subprocess.check_output(self.fortune, shell=True).decode("utf-8")
        admin_status = request.user.groups.filter(name="Administrator").exists()
        page_dict = {
                'fileshare': [
                    [('common resources', 'resources'), ('download','download'),
                     ('upload', 'upload'), ('webroot downloads', 'webroot')],
                    'Upload, download, organize, and store files and resources.'
                    ]
#                'plex': [
#                    "Watch anything I might have floating around on my Plex server"
#                    ]
                }

        sorted_pages = {}
        for key in sorted(page_dict):
            sorted_pages[key] = page_dict[key]

        tile_list = self.tile_parser(sorted_pages)

        context = {'motd': motd, 'tile_list': tile_list}

        return render(request, self.template_name, context)

class LoginView(BaseView):
    template_name = 'login.html'
    username = password = ''

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                error = "Invalid username or password"
                context = {'error': error}
                return render(request, self.template_name, context)
        else:
            error = "Invalid username or password"
            context = {'error': error}
            return render(request, self.template_name, context)

class LogoutView(BaseView):
    template_name = 'logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')
