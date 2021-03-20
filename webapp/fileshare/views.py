from django.shortcuts import render
from generics.views import BaseView

class FileshareView(BaseView):
    template_name = 'fileshare.html'
    pages = {
            'common resources': ['resources', 'View and download resources and utilities used by clients that have been saved for convenience.'],
            'download': ['download', 'View and download files temporarily stored on the server.'],
            'upload': ['upload', 'Upload files to the resources storage, or temporary storage.'],
            'webroot': ['webroot', 'Download executables for Webroot.']
            }

    def get(self, request, *args, **kwargs):
        # Get user data from parent function to pass in context
        tile_list = self.tile_parser(self.pages)
        context = {'tile_list': tile_list}
        return render(request, self.template_name, context)
