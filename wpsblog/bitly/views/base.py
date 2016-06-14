from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from bitly.models import BitLink


class BitLinkBaseView(LoginRequiredMixin, View):
    model = BitLink
