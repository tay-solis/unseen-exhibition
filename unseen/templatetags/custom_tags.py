from django import template


register = template.Library()

def unsecure_url(value):
  return value.replace('https', 'http')

register.filter('unsecure_url', unsecure_url)
