import bpy
from . import addon
from . import prefs


def register():
    bpy.utils.register_class(addon.OverdriveProps)
    bpy.utils.register_class(prefs.OverdrivePrefs)

    bpy.types.WindowManager.overdrive = bpy.props.PointerProperty(type=addon.OverdriveProps)


def unregister():
    del bpy.types.WindowManager.overdrive

    bpy.utils.unregister_class(prefs.OverdrivePrefs)
    bpy.utils.unregister_class(addon.OverdriveProps)
