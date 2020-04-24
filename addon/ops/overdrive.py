import bpy
import time
from .. import utils


class OD_OT_timer(bpy.types.Operator):
    """Operator which runs its self from a timer"""
    bl_idname = "overdrive.overdrive"
    bl_label = "Overdrive"
    bl_description = '\n Auto hide/show last bevel modifier in 3D viewport based on mouse activity'
 
    _prefs = None
    _timer = None
    _moves = None
    _time = None
    _middle_mouse_lock = None
    
    def modal(self, context, event):
        if event.type in {'RIGHTMOUSE', 'ESC'}:
            self.cancel(context)
            return {'CANCELLED'}

        print(f"{event.type} / {event.value} / {(time.perf_counter() - self._time):.0f} / {self._moves}")
        
        if hasattr(bpy.context.space_data, 'shading'):
            if bpy.context.space_data.shading.type == 'SOLID':
        
                if event.type == 'MIDDLEMOUSE' and event.value == 'PRESS':
                    self._middle_mouse_lock= True
                    print ('\n=\n==\n===\nMIDDLE MOUSE PRESS ACTIVE\n===\n==\n=\n')
                
                if event.type == 'MOUSEMOVE' and event.value == 'RELEASE':
                    self._middle_mouse_lock= False
                
                if event.type == 'MOUSEMOVE':
                    # hide last bevel mod (mouse movement delayed)
                    if self._moves > 25:
                        if self._prefs.od_show_face_orientation:
                            bpy.context.space_data.overlay.show_face_orientation = True
                        if self._prefs.od_show_wireframes:
                            bpy.context.space_data.overlay.show_wireframes = True
                        for obj in bpy.context.scene.objects:
                            if 'Cutters' in bpy.data.collections:
                                if obj.name not in bpy.data.collections['Cutters'].objects:
                                    for mod in reversed(obj.modifiers):
                                        if mod.type == "BEVEL":
                                            mod.show_viewport = False
                                            break
                    
                    # update counters
                    # reset 'seconds at rest' counter
                    self._time = time.perf_counter()
                    # increment 'number of mouse moves' counter
                    self._moves += 1


                if event.type == 'TIMER' \
                    and time.perf_counter() - self._time > self._prefs.od_interval \
                    and not self._middle_mouse_lock:

                    # reset 'number of mouse moves' counter 
                    self._moves = 0            

                    # edit mode exclude
                    if bpy.context.active_object:
                        if bpy.context.active_object.mode == 'EDIT':
                            return {'PASS_THROUGH'}

                    # show last bevel mod
                    bpy.context.space_data.overlay.show_face_orientation = False
                    for obj in bpy.context.scene.objects:
                        if 'Cutters' in bpy.data.collections:
                            if obj.name not in bpy.data.collections['Cutters'].objects:
                                for mod in reversed(obj.modifiers):
                                    if mod.type == "BEVEL":
                                        mod.show_viewport = True
                                        break
                        
        return {'PASS_THROUGH'}
 
    def execute(self, context):
        #initialization
        self._time = time.perf_counter()
        self._moves = 0
        self._middle_mouse_lock = False
        
        # set is_running property
        self._prefs = utils.common.prefs()
        self._prefs.od_is_running = True
        # force screen refresh.  triggers panel's def popover() and refreshes icons.
        #bpy.context.view_layer.update()
        if hasattr(bpy.context.area, 'tag_redraw'):
            bpy.context.area.tag_redraw()

        wm = context.window_manager
        self._timer = wm.event_timer_add(1, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}
 
    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)
        # set is_running property
        self._prefs.od_is_running = False
        # force screen refresh.  triggers panel's def popover() and refreshes icons.
        #bpy.context.view_layer.update()
        if hasattr(bpy.context.area, 'tag_redraw'):
            bpy.context.area.tag_redraw()