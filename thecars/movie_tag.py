from django import template
from .models import Brand, Car, Type


register = template.Library()


@register.simple_tag()
def get_types():
    return Type.objects.all()

@register.simple_tag()
def get_brands():
    return Brand.objects.all()