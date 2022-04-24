from django.shortcuts import render
from generics.views import BaseView
import subprocess


class HomeView(BaseView):
    template_name = 'home.html'
    fortune = "/usr/games/fortune -s"

    def get(self, request, *args, **kwargs):
        motd = subprocess.check_output(self.fortune, shell=True).decode("utf-8")
        context = {'motd': motd}

        return render(request, self.template_name, context)
