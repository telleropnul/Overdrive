import bpy
from .. import utils


class OverdrivePrefs(bpy.types.AddonPreferences):
    bl_idname = utils.common.module()

    od_interval: bpy.props.IntProperty(
        name='Overdrive Interval',
        description='The amount of seconds for overdrive to show the last bevel modifier',
        default=1,
        min=1,
        max=5,
    )

    od_show_face_orientation: bpy.props.BoolProperty(
        name='Force Show Normals',
        description='Whether to use Show Face Orientation overlay',
        default=True,
    )


    od_show_wireframes: bpy.props.BoolProperty(
        name='Force Show Edges',
        description='Whether to use Show Wireframes overlay',
        default=True,
    )


    od_high_contrast_icons: bpy.props.BoolProperty(
        name='Overdrive High Contrast Icons',
        description='Whether to use the high contrast set of icons',
        default=False,
    )


    od_is_running: bpy.props.BoolProperty(
        name='Overdrive Is Running',
        description='Indicates whether or not Overdrive is currently active',
        default=False,
    )

    def draw(self, context):
        layout = self.layout
        utils.ui.draw_prop(layout, 'Overdrive Auto Show/Hide Last Bevel Modifier Interval', self, 'od_interval')
        utils.ui.draw_prop(layout, 'Force Show Normals', self, 'od_show_face_orientation')
        utils.ui.draw_prop(layout, 'Force Show Edges', self, 'od_show_wireframes')
        utils.ui.draw_prop(layout, 'Overdrive High Contrast Icons', self, 'od_high_contrast_icons')
        utils.ui.draw_prop(layout, 'Overdrive Is Running', self, 'od_is_running')