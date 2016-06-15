from django.views.generic.edit import CreateView

from .base import BitLinkBaseView


class BitLinkCreateView(BitLinkBaseView, CreateView):
    template_name = "bitly/new.html"
    fields = ["origin_url"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BitLinkCreateView, self).form_valid(form)
