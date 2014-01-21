# Create your views here.
from django.views.generic import TemplateView
from site_regions.models import config
from django.views.generic.detail import DetailView

class indextemplate(DetailView):
    #template_name = 'index',
    model = config
    #model = config.objects.order_by('-odr')[:1],
    def get_context_data(self, **kwargs):
        #print 'Passou aqui no template'
        context = super(indextemplate, self).get_context_data(**kwargs)
        return context
def indexfunc(request, slug):
    slug='529cc7231c64520e18e3c43d';
    return indextemplate.as_view()(request,slug=slug)