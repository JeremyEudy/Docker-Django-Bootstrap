class TableQueryMixin:
    # Override get_context_data() for ListViews

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['query'] = self.request.GET.get('q')
        context['view'] = self.request.GET.get('all')
        context['count'] = self.request.GET.get('count')

        if context['query']:
            context['view'] = "True"

        return context
