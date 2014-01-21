# Create your views here.
from django.views.generic.detail import DetailView

from site_regions.models import pagefooter

class pagefoortDtlVw(DetailView):
    model = pagefooter

    def get_context_data(self, **kwargs):
        context = super(pagefoortDtlVw, self).get_context_data(**kwargs)
        return context