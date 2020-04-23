import bpy
import time

class OD_OT_timer(bpy.types.Operator):
    """Operator which runs its self from a timer"""
    bl_idname = "overdrive.overdrive"
    bl_label = "Overdrive"
    bl_description = '\n Auto hide/show last bevel modifier in 3D viewport based on mouse activity'
 
    _timer = None
    _moves = None
    _time = None
    _middle_mouse_lock = None
    
 
    def modal(self, context, event):
        if event.type in {'RIGHTMOUSE', 'ESC'}:
            self.cancel(context)
            return {'CANCELLED'}

        print(f"{event.type} / {event.value} / {(time.perf_counter() - self._time):.0f} / {self._moves}")
        
        if bpy.context.space_data.shading.type == 'SOLID':
        
            if event.type == 'MIDDLEMOUSE' and event.value == 'PRESS':
                self._middle_mouse_lock= True
                print ('\n=\n==\n===\nMIDDLE MOUSE PRESS ACTIVE\n===\n==\n=\n')
            
            if event.type == 'MOUSEMOVE' and event.value == 'RELEASE':
                self._middle_mouse_lock= False
            
            if event.type == 'MOUSEMOVE':
                # show last bevel mod (mouse movement delayed)
                if self._moves > 25:               
                    for obj in bpy.context.scene.objects:
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
                and time.perf_counter() - self._time > 1 \
                and not self._middle_mouse_lock:

                # reset 'number of mouse moves' counter 
                self._moves = 0            

                # edit mode exclude
                if bpy.context.active_object:
                    if bpy.context.active_object.mode == 'EDIT':
                        return {'PASS_THROUGH'}

                # hide last bevel mod
                for obj in bpy.context.scene.objects:
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
        

        wm = context.window_manager
        self._timer = wm.event_timer_add(1, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}
 
    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)