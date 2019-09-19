from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class memory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_("A Phrase for my thought"), max_length=50, blank=False)
    description = models.TextField(_("All I can think of my thought"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
