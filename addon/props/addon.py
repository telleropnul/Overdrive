import bpy


name = __name__.partition('.')[0]


class OverdriveProps(bpy.types.PropertyGroup):
    addon: bpy.props.StringProperty(
        name='Addon',
        description='The Overdrive module',
        default=name,
    )
