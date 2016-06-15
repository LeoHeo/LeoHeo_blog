from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404
from bitly.models import BitLinkLog


class BitLinkRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        bitlink = get_object_or_404(
            self.request.user.bitlink_set,
            shorten_hash=self.kwargs.get("shorten_hash")
        )

        bitlink_log = bitlink.bitlinklog_set.create(
            http_referer=self.request.META.get("HTTP_REFERER"),
            http_user_agent=self.request.META.get("HTTP_USER_AGENT"),
            http_remote_address=self.request.META.get("REMOTE_ADDR"),
            http_meta_json=str(self.request.META),
        )

        return bitlink.origin_url
