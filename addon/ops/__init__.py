import bpy
from . import overdrive

def register():
    bpy.utils.register_class(overdrive.OD_OT_timer)


def unregister():
    bpy.utils.unregister_class(overdrive.OD_OT_timer)