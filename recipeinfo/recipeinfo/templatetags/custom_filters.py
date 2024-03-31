from django import template
from django.utils.safestring import mark_safe
import math

register = template.Library()

@register.filter
def split_text(value, delimiter=","):
    return value.split(delimiter)

@register.filter
def star_rating(value):
    string = ''
    if type(value) == int:
        for i in range(1, 6):
            if i + 0.5<= value:
                string += '<i class="bi bi-star-fill"></i>'
            elif i == value:
                string += '<i class="bi bi-star-half"></i>'
            else:
                string += '<i class="bi bi-star"></i>'
    else:
        length = 0
        sum = 0
        for comment in value:
            length += 1
            sum += float(comment.rating)

        if length == 0:
            string = 'No rating available'
        else:
            stars = int(math.floor((sum/length) + 0.5))
            for i in range(1, 6):
                if i + 0.5 <= stars/2:
                    string += '<i class="bi bi-star-fill"></i>'
                elif i == stars/2:
                    string += '<i class="bi bi-star-half"></i>'
                else:
                    string += '<i class="bi bi-star"></i>'
    return mark_safe(string)
