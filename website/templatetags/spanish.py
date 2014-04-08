from django import template
register = template.Library()


@register.simple_tag
def smonth(month):
    try:
        return (
            'Ene', 'Feb', 'Mar', 'Abr',
            'May', 'Jun', 'Jul', 'Ago',
            'Sep', 'Oct', 'Nov', 'Dic',
        )[int(month - 1)]
    except IndexError:
        return month


@register.simple_tag
def sday(day):
    try:
        return (
            'Lunes', 'Martes', 'Miercoles', 'Jueves',
            'Viernes', 'Sabado', 'Domingo'
        )[int(day)]
    except IndexError:
        return day