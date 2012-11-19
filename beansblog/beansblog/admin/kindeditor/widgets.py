from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

class KindEditor(forms.Textarea);

	class Media:
		css={
			'all': ('/static/kindeditor-4.1.4/themes/default/default.css',
			        '/static/kindeditor-4.1.4/plugins/code/prettify.js',),
		}
		js = (
				"/static/kindeditor-4.1.4/kindeditor.js",
				'/static/kindeditor-4.1.4/plugins/code/prettify.js'
		)
	
	def __init__(self, attrs = {}):

		super(KindEditor, self).__init__(attrs)

	def render(self, name, value, attrs=None):
		rendered = super(KindEditor, self).render(name, value, attrs)
		context = {
					'name': name,
					'MEDIA_URL': settings.MEDIA_URL,
				}
		return rendered + mark_safe(render_to_string('editor/kindeditor.html', contet))
