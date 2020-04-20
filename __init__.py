# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Overdrive",
    "author" : "c0",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "3D View"
}

import bpy
import time

class OD_OT_timer(bpy.types.Operator):
    """Operator which runs its self from a timer"""
    bl_idname = "overdrive.operator"
    bl_label = "Overdrive"
    bl_description = '\n Auto hide/show Modifiers in 3D viewport based on mouse activity'
 
    _timer = None
    _moves = None
    _time = None
    _middle_mouse_lock = None
    
 
    def modal(self, context, event):
        if event.type in {'RIGHTMOUSE', 'ESC'}:
            self.cancel(context)
            return {'CANCELLED'}

        print(event.type + ' / ' + event.value + ' / ' + str(time.perf_counter() - self._time))
        
        if bpy.context.space_data.shading.type == 'SOLID':
        
            if event.type == 'MIDDLEMOUSE' and event.value == 'PRESS':
                self._middle_mouse_lock= True
                print ('\n=\n==\n===\nMIDDLE MOUSE PRESS ACTIVE\n===\n==\n=\n')
            
            if event.type == 'MOUSEMOVE' and event.value == 'RELEASE':
                self._middle_mouse_lock= False
            
            if event.type == 'MOUSEMOVE':
                self.mouse_xy=(event.mouse_x, event.mouse_y)
                for obj in bpy.context.scene.objects:
                    for mod in reversed(obj.modifiers):
                        if mod.type == "BEVEL":
                            mod.show_viewport = False
                            break

            if event.type == 'MOUSEMOVE':
                # restart 'seconds at rest' counter
                self._time = time.perf_counter()
                # increment 'number of mouse moves' counter
                self._moves += 1

            if event.type == 'TIMER' \
                and time.perf_counter() - self._time > 2 \
                and not self._middle_mouse_lock \
                and self._moves > 10:
                
                if bpy.context.active_object:
                    if bpy.context.active_object.mode == 'EDIT':
                        return {'PASS_THROUGH'}

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
 
def register():
    bpy.utils.register_class(OD_OT_timer)
 
 
def unregister():
    bpy.utils.unregister_class(OD_OT_timer)
 
 
if __name__ == "__main__":
    register()
 
    # test call
    bpy.ops.wm.overdrive.operator()