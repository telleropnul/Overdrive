import bpy
from .. import utils


class OverdrivePrefs(bpy.types.AddonPreferences):
    bl_idname = utils.common.module()

    overdrive_interval: bpy.props.IntProperty(
        name='Overdrive Interval',
        description='The amount of seconds for overdrive to show the last bevel modifier',
        default=1,
        min=1,
        max=5,
    )


    high_contrast_icons: bpy.props.BoolProperty(
        name='High Contrast Icons',
        description='Whether to use the high contrast set of icons',
        default=False,
    )
	

    def draw(self, context):
        layout = self.layout
        utils.ui.draw_prop(layout, 'Autosave Interval', self, 'overdrive_interval')
        utils.ui.draw_prop(layout, 'High Contrast Icons', self, 'high_contrast_icons')