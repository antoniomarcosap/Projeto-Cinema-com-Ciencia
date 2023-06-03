from django.shortcuts import redirect, render
from django.views.generic import ListView

from . import models


class GalleryView(ListView):
    model = models.Gallery
    template_name = 'gallery/gallery.html'
    context_object_name = 'gallery'
