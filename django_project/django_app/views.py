from django.views.generic import ListView, DetailView

from django_app.models import Thing

class ThingList(ListView):
    model = Thing
    template_name = "django_app/thing-list.html"

class ThingDetail(DetailView):
    model = Thing
    template_name = "django_app/thing-detail.html"

