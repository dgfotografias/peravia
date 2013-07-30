__author__ = 'Yusdenis'

from django import template

register = template.Library()


@register.filter
def contiene(posible,id):
    return id in posible

@register.filter
def texto(textos,respuesta):
    if textos.has_key(respuesta):
        return textos[respuesta]
    else:
        return ''
