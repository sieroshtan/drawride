from django.templatetags.static import static
from django.utils import translation
from django.urls import reverse_lazy
from django.conf import settings
from django.utils.formats import localize
from django.utils.timezone import template_localtime

from jinja2 import Environment
from jinja2.ext import Extension


class DjangoL10n(Extension):
    """
    Implements localization of template variables with respect to
    `USE_L10N` and `USE_TZ` settings::

        >>> from datetime import datetime
        >>> from django.utils import timezone, translation
        >>> from jinja2 import Extension
        >>> env = Environment(extensions=[DjangoL10n])
        >>> template = env.from_string("{{ a_number }} {{ a_date }}")
        >>> context = {
        ...     'a_number': 1.23,
        ...     'a_date': datetime(2000, 10, 1, 14, 10, 12, tzinfo=timezone.utc),
        ... }
        >>> translation.activate('en')
        >>> timezone.activate('America/Argentina/Buenos_Aires')
        >>> template.render(context)
        '1.23 Oct. 1, 2000, 11:10 a.m.'
        >>> translation.activate('de')
        >>> translation.activate('Europe/Berlin')
        >>> template.render(context)
        '1,23 1. Oktober 2000 16:10'

    """

    def __init__(self, environment):
        super(DjangoL10n, self).__init__(environment)
        finalize = []
        if settings.USE_TZ:
            finalize.append(template_localtime)
        if settings.USE_L10N:
            finalize.append(localize)

        if finalize:
            fns = iter(finalize)
            if environment.finalize is None:
                new_finalize = next(fns)
            else:
                new_finalize = environment.finalize
            for f in fns:
                new_finalize = self._compose(f, new_finalize)

            environment.finalize = new_finalize

    @staticmethod
    def _compose(f, g):
        return lambda var: f(g(var))


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {
            "static": static,
            "url": reverse_lazy,
        }
    )
    env.install_gettext_translations(translation, newstyle=True)
    return env
