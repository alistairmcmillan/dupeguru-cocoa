# Created On: 2012-05-30
# Copyright 2015 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "GPLv3" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.gnu.org/licenses/gpl-3.0.html

from objp.util import dontwrap
from cocoa.inter import PyGUIObject, GUIObjectView

class DeletionOptionsView(GUIObjectView):
    def updateMsg_(self, msg: str): pass
    def show(self) -> bool: pass
    def setHardlinkOptionEnabled_(self, enabled: bool): pass

class PyDeletionOptions(PyGUIObject):
    def setLinkDeleted_(self, link_deleted: bool):
        self.model.link_deleted = link_deleted
    
    def setUseHardlinks_(self, use_hardlinks: bool):
        self.model.use_hardlinks = use_hardlinks
    
    def setDirect_(self, direct: bool):
        self.model.direct = direct
    
    #--- model --> view
    @dontwrap
    def update_msg(self, msg):
        self.callback.updateMsg_(msg)
    
    @dontwrap
    def show(self):
        return self.callback.show()
    
    @dontwrap
    def set_hardlink_option_enabled(self, enabled):
        self.callback.setHardlinkOptionEnabled_(enabled)
