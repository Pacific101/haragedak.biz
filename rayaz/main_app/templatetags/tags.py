from django import template
register = template.Library()

def phonenumber(value):
    phone = '%s %s %s %s %s' %(value[0:3],value[3:5],value[5:8],value[8:10],value[10:12])
    return phone

def reviewfier(value):
    if value == 5.0:
        return int(value)
    elif value == 4.0:
        return int(value)
    elif value == 3.0:
        return int(value)
    elif value == 2.0:
        return int(value)
    elif value == 1.0:
        return int(value)
    else:
        return value

register.filter('phonenumber', phonenumber)
register.filter('reviewfier', reviewfier)
