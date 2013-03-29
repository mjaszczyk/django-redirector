# -*- coding: utf-8 *-*
from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.utils.translation import ugettext as _


class Rule(models.Model):
    REDIRECTION_PERMANENT = 301
    REDIRECTION_FOUND = 302
    REDIRECTION_SEE_OTHER = 303
    REDIRECTION_TEMPORARY = 307

    REDIRECTION_TYPES = (
        (REDIRECTION_PERMANENT, u'301 Moved Permanently'),
        (REDIRECTION_FOUND, u'302 Found'),
        (REDIRECTION_SEE_OTHER, u'303 See Other'),
        (REDIRECTION_TEMPORARY, u'307 Temporary Redirect'),
    )

    redirection_type = models.SmallIntegerField(default=REDIRECTION_PERMANENT, choices=REDIRECTION_TYPES)
    pattern = models.CharField(max_length=300, help_text=_('simple URL without "/" at the beginning'
                                                           'or django urlconf style pattern'))
    target_url = models.CharField(max_length=300, null=True, blank=True,
                                  help_text=_('internal or external target URL'))
    target_url_name = models.CharField(max_length=50, null=True, blank=True,
                                       help_text=_('name of django urlconf pattern name'))
    target_view = models.CharField(max_length=50, null=True, blank=True,
                                   help_text=_('target view with can make proper redirection'))
    target_params = models.CharField(max_length=200, null=True, blank=True,
                                     help_text=_('Additional params.'))

    order = models.PositiveSmallIntegerField()
    site = models.ForeignKey(Site)

    on_site = CurrentSiteManager()

    class Meta:
        ordering = ('order',)
