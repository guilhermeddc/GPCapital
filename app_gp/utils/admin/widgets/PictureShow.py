from django.utils.html import format_html
from django.contrib.admin.widgets import AdminFileWidget


class PictureShowWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        html_file_admin = super(AdminFileWidget, self).render(name, value, attrs)

        output = []
        # if value and hasattr(value, 'url'):
        #     output.append(format_html('<p>{}x{}</p>',
        #                               value.width,
        #                               value.height))
        #     output.append(format_html('<img src="{}" width="{}" height="{}" alt="No image"/>',
        #                               value.url,
        #                               value.width,
        #                               value.height))
        #
        # output.append(html_file_admin)

        if value and hasattr(value, 'url'):

            output.append('<div class="container">')
            output.append('<div class="row">')
            output.append('<div class="col-md-6">{0}x{1}</div>'.format(value.width, value.height))
            output.append('<div class="col-md-6"><img src="{0}" width="{1}" height="{2}" alt="No image"/></div>'.format(value.url, value.width, value.height))
            output.append('<div class="col-md-6">{0}</div>'.format(html_file_admin))
            output.append('</div></div>')

        return format_html(''.join(output))
