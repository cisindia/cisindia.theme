from five import grok
from Products.CMFCore.interfaces import IContentish

grok.templatedir('templates')


class blog_summary_view(grok.View):
    grok.context(IContentish)
    grok.name('blog_summary_view')
    grok.require('zope2.View')
    grok.template('blog_summary_view')
