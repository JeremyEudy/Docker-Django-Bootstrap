from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.models import User

# Generic view with helper function used to boilerplate template construction
class BaseView(View):
    def tile_parser(self, pages):
        # Parses page dictionary into sub lists for 2 column tile presentation
        # Makes a 2 element sub list from dictionaries such that the list is as follows:
        # [[dict1, dict2], ...]
        #
        # Explicit ending format for navbar page_dict:
        #       [[{page: [(subpage, subpage_link), description]}, 
        #        {page2: [(subpage, subpage_link), description]}],
        #        ...]
        #
        # Explicit ending format for tile pages (launchpad, home, etc):
        #       [[{'page': ['link', 'description']}, {'page2': ['link', 'description']}],
        #       ...]

        double_list = []

        for key,val in pages.items():
            try:
                # This should never be triggered, but just in case, check for dupes
                if any({key: pages[key]} in sub_list for sub_list in double_list):
                    pass
                else:
                    try:
                        next_key = list(pages.keys())[list(pages.keys()).index(key)+1]
                        double_list.append([{key: val}, {next_key: pages[next_key]}])

                    except:
                        double_list.append([{key: val}, None])

            except Exception as e:
                double_list.append(e)

        return double_list

""" This is broken and unimportant for now
class CSRFFailure(View):
    template_name = 'csrf_failure.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class BadRequest(View):
    template_name = '400_bad_request.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Forbidden(View):
    template_name = '403_forbidden.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class NotFound(View):
    template_name = '404_not_found.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class InternalError(View):
    template_name = '500_internal_error.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
"""
