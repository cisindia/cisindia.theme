from five import grok
from Products.CMFCore.interfaces import IContentish

grok.templatedir('templates')

class event_summary_view(grok.View):
    grok.context(IContentish)
    grok.name('event_summary_view')
    grok.require('zope2.View')
    grok.template('event_summary_view')
