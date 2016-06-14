from django.views.generic.edit import CreateView
from hashids import Hashids
from .base import BitLinkBaseView
import random


class BitLinkCreateView(BitLinkBaseView, CreateView):
    template_name = "bitly/new.html"
    fields = ["origin_url"]

    def form_valid(self, form):
        hashids = Hashids(salt="bitlink", min_length=4)

        form.instance.user = self.request.user
        form.instance.shorten_hash = hashids.encode(
            random.randint(1, 1000)
        )

        return super(BitLinkCreateView, self).form_valid(form)
