from pyramid_debugtoolbar.panels import DebugPanel
from pyramid_debugtoolbar.utils import dictrepr
import inspect
import json

_ = lambda x: x

class RenderValuesPanel(DebugPanel):
    """
    Render Values debug panel
    """
    name = 'RenderValues'
    has_content = True
    variables = {}
    event = None
    
    def process_beforerender(self, event):
        if not self.variables:
            self.variables = dict()
        
        if not self.event:
            self.event = event
            
        
    def nav_title(self):
        return _('Renderer Values')

    def url(self):
        return ''

    def title(self):
        return _('Renderer Values')

    def content(self):
        for (k,v) in self.event.items():
            self.variables[k] = flatten(v)

        vars = {'vars':self.variables, 'event': self.event}
        return self.render(
            'pyramid_debugtoolbar_rendervalues:templates/renderpanel.pt',
            vars, self.request)

def includeme(config):
    config.registry.settings['debugtoolbar.panels'].append(RenderValuesPanel)

def flatten(obj):
    if type(obj) is list:
        objs = [flatten(o) for o in obj]
        return objs
    if hasattr(obj,'_data'):
        return obj._data
    else:
        return obj
