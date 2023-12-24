from django.templatetags.static import static
from django.utils import translation
from django.urls import reverse_lazy

from jinja2 import Environment


def environment(**options):
    env = Environment(extensions=["jinja2.ext.i18n"], **options)
    env.globals.update(
        {
            "static": static,
            "url": reverse_lazy,
        }
    )
    env.install_gettext_translations(translation, newstyle=True)
    return env
