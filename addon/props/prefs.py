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

    show_face_orientation: bpy.props.BoolProperty(
        name='Force Show Normals',
        description='Whether to use Show Face Orientation overlay',
        default=True,
    )


    show_wireframes: bpy.props.BoolProperty(
        name='Force Show Edges',
        description='Whether to use Show Wireframes overlay',
        default=True,
    )


    high_contrast_icons: bpy.props.BoolProperty(
        name='Overdrive High Contrast Icons',
        description='Whether to use the high contrast set of icons',
        default=False,
    )


    is_running: bpy.props.BoolProperty(
        name='Overdrive Is Running',
        description='Indicates whether or not Overdrive is currently active',
        default=False,
    )

    def draw(self, context):
        layout = self.layout
        utils.ui.draw_prop(layout, 'Overdrive Auto Show/Hide Last Bevel Modifier Interval', self, 'overdrive_interval')
        utils.ui.draw_prop(layout, 'Force Show Normals', self, 'show_face_orientation')
        utils.ui.draw_prop(layout, 'Force Show Edges', self, 'show_wireframes')
        utils.ui.draw_prop(layout, 'Overdrive High Contrast Icons', self, 'high_contrast_icons')
        utils.ui.draw_prop(layout, 'Overdrive Is Running', self, 'is_running')