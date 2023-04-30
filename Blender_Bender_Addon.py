bl_info = {
    "name": "Blender Bender panel",
    "author": "Backy3D",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > UI",
    "description": "Reminds you of the Weekly theme.",
    "warning": "",
    "doc_url": "https://github.com/Backy3D/Blender-bender-Addon.git",
    "category": "OBJECT",
}


import bpy
from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
    PropertyGroup
)

links = {"Weekly theme" : "https://www.youtube.com/@GreenHatAnimation"}



class BBPanel(bpy.types.Panel):
    """Click for the weekly theme"""
    bl_label = "Blender Bender panel"
    bl_idname = "BBPnnl"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Blender Bender"


    
    def draw(self, context):
        layout = self.layout
  
        row = layout.row()
        row.label(text= "   Good morning blender bender")
        for i in range (1,4):
            row = layout.row()
            
        col = layout.column()
        for name, url in links.items():
            op = col.operator('wm.url_open', text=name, icon = "BLENDER")
            op.url = url
            
        for i in range (1,2):
            row = layout.row()
        row.label(text= " Sergey's advice coming soon)")
        

def register():
    bpy.utils.register_class(BBPanel)
    
def unregister():
    bpy.utils.unregister_class(BBPanel)
    
    
if __name__ == "__main__":
    register()