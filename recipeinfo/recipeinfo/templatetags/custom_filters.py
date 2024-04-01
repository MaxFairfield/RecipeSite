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
    if type(value) == int or type(value) == float:
        stars = value/2
        for i in range(1, 6):
            if i <= stars:
                string += '<i class="bi bi-star-fill"></i>'
            elif i - 0.5 <= stars:
                string += '<i class="bi bi-star-half"></i>'
            else:
                string += '<i class="bi bi-star"></i>'
                
        #debug:
        #string += f' ({value})'
    else:
        length = 0
        sum = 0
        for comment in value:
            length += 1
            sum += float(comment.rating)

        if length == 0:
            string = 'No rating available'
        else:
            stars = (sum / (length * 1))  # Adjusted for half-star ratings
            for i in range(1, 6):
                if i <= stars/2:
                    string += '<i class="bi bi-star-fill"></i>'
                elif i - 0.5 <= stars/2:
                    string += '<i class="bi bi-star-half"></i>'
                else:
                    string += '<i class="bi bi-star"></i>'

            #debug:
            #string += f' (average: {stars})'
    return mark_safe(string)
