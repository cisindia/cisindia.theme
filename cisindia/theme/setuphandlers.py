from collective.grok import gs
from cisindia.theme import MessageFactory as _

@gs.importstep(
    name=u'cisindia.theme', 
    title=_('cisindia.theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('cisindia.theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
