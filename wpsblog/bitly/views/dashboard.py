from django.views.generic.list import ListView

from .base import BitLinkBaseView


class BitLinkDashBoardView(BitLinkBaseView, ListView):
    template_name = "bitly/dashboard.html"
    context_object_name = "bitlink"

    def get_queryset(self):
        bitlink = self.model.objects.get(
            shorten_hash=self.kwargs.get("shorten_hash")
        )

        return bitlink
