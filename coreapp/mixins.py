from django.shortcuts import redirect
from django.urls import reverse_lazy

class AnonymousRequiredMixin:
    anonymous_redirect_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.anonymous_redirect_url)
        return super().dispatch(request, *args, **kwargs)