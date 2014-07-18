from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.cache import render_cachekey

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from cisindia.theme import MessageFactory as _

class IAuthorInfo(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    pass

class Assignment(base.Assignment):
    implements(IAuthorInfo)

    @property
    def title(self):
        return _('Author Info')

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('templates/authorinfo.pt')

    @property
    def available(self):
        return True

class AddForm(base.NullAddForm):
    form_fields = form.Fields(IAuthorInfo)
    label = _(u"Add Author Info")
    description = _(u"")

    def create(self):
        return Assignment()
