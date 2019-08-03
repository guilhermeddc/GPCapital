from django.utils.html import format_html
from django.contrib.admin.widgets import AdminFileWidget


class VideoShowWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = [super(AdminFileWidget, self).render(name, value, attrs)]

        if value and hasattr(value, 'url'):
            output.append('<video width="{0}" height="{1}" controls>'
                          '<source src="{2}" type="video/mp4">'
                          'Seu browser nâo suporta videos em HTML 5.'
                          '</video>'.format(320, 240, value.url))

        return format_html(''.join(output))
