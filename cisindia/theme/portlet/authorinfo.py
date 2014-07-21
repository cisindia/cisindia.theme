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

from plone import api

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
    
    def getuserinfo(self):
	info = dict()
	user = api.user.get(username=self.context.Creator())

	if not user:
	    mtool = api.portal.get_tool('portal_membership')

	    info.update(fullname=self.context.Creator())
	    info.update(image=mtool.getPersonalPortrait())
	    info.update(description=u'')

	    return info

	info.update(fullname=user.getProperty('fullname'))
	info.update(description=user.getProperty('description'))
	info.update(image=user.getPersonalPortrait(user.id))

	return info



class AddForm(base.NullAddForm):
    form_fields = form.Fields(IAuthorInfo)
    label = _(u"Add Author Info")
    description = _(u"")

    def create(self):
        return Assignment()
