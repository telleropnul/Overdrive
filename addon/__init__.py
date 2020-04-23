from . import props
from . import icons
from . import ops
from . import ui


def register():
    props.register()
    icons.register()
    ops.register()
    ui.register()


def unregister():
    ui.unregister()
    ops.unregister()
    icons.unregister()
    props.unregister()
