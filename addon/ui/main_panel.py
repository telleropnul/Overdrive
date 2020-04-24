import bpy
from .. import utils


class OverdrivePanel(bpy.types.Panel):
    bl_idname = 'OD_PT_OverdrivePanel'
    bl_category = 'Overdrive'
    bl_label = f'Overdrive {utils.common.version()}'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'


    def draw(self, context):
        prefs = utils.common.prefs()

        layout = self.layout

        if self.is_popover:
            layout.ui_units_x = 8

        col = layout.column()

        box = col.box().column()
        box.operator('overdrive.overdrive')
        box.prop(prefs, 'od_interval')
        box.prop(prefs, 'od_show_face_orientation')
        box.prop(prefs, 'od_show_wireframes')

		
def popover(self, context):
    layout = self.layout
    panel = OverdrivePanel.bl_idname
    icon = utils.ui.get_icon()
    layout.popover(panel, text='', icon_value=icon)
