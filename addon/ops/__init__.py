import bpy
from . import overdrive

def register():
    bpy.app.driver_namespace['grmbl'] = OD_OT_timer
    bpy.utils.register_class(overdrive.OD_OT_timer)


def unregister():
    bpy.utils.unregister_class(overdrive.OD_OT_timer)