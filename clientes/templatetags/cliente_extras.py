__author__ = 'Yusdenis'

from django import template
from django.contrib.admin.models import LogEntry

register = template.Library()

class CustomAdminLogNode(template.Node):
    def __init__(self, limit, varname, user):
        self.limit, self.varname, self.user = limit, varname, user

    def __repr__(self):
        return "<GetAdminLog Node>"

    def render(self, context):
        if self.user is None:
            context[self.varname] = LogEntry.objects.all().select_related('content_type', 'user')[:self.limit]
        else:
            user_id = self.user
            if not user_id.isdigit():
                user_id = context[self.user].id
            context[self.varname] = LogEntry.objects.filter(user__id__exact=user_id, content_type__name ='cliente').select_related('content_type', 'user')[:int(self.limit)]
        return ''


@register.tag
def client_logs(parser, token):
    tokens = token.contents.split()
    if len(tokens) < 4:
        raise template.TemplateSyntaxError(
            "'get_admin_log' statements require two arguments")
    if not tokens[1].isdigit():
        raise template.TemplateSyntaxError(
            "First argument to 'get_admin_log' must be an integer")
    if tokens[2] != 'as':
        raise template.TemplateSyntaxError(
            "Second argument to 'get_admin_log' must be 'as'")
    if len(tokens) > 4:
        if tokens[4] != 'for_user':
            raise template.TemplateSyntaxError(
                "Fourth argument to 'get_admin_log' must be 'for_user'")
    return CustomAdminLogNode(limit=tokens[1], varname=tokens[3], user=(len(tokens) > 5 and tokens[5] or None))