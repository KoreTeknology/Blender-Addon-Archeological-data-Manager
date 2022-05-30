import bpy
import mathutils
from mathutils import Vector

from bpy.types import Operator

from . orthoempty_props import *

class SCENE_OT_add_orthoempty(bpy.types.Operator):
	"""Create a new Camera Object"""
	bl_idname = "scene.add_orthoempty"
	bl_label = "Add Orthoempty to scene"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		bpy.ops.object.empty_add(type='ARROWS', location=(0, 0, 0))

		tve = bpy.context.object
		oe = bpy.context.scene.orthoempty_props.orthoempty_name
		tve.name = oe
		tve.show_name = True
		tve.show_in_front = True

		self.report({'INFO'}, "> Empty created and named : Empty fake center")

		return {'FINISHED'}

class SCENE_OT_fake_coord_orthoempty(bpy.types.Operator):
	"""Create a new Camera Object"""
	bl_idname = "scene.fake_coord_calculate"
	bl_label = "Calculate fake coordinates"
	bl_options = {'REGISTER', 'UNDO'}


	def execute(self, context):

		# real object location
		obj = bpy.data.objects["Empty Fake center"]
		objlx = obj.location[0]
		objly = obj.location[1]
		objlz = obj.location[2]
		# vector format
		objl_all= mathutils.Vector((objlx, objly, objlz))

		# offset values
		offset_x = bpy.context.scene.orthoempty_props.x_offset_value
		offset_y = bpy.context.scene.orthoempty_props.y_offset_value
		offset_z = bpy.context.scene.orthoempty_props.z_offset_value
		# vector format
		offset_all = mathutils.Vector((offset_x, offset_y, offset_z))

		# fake values
		fxv = bpy.context.scene.orthoempty_props.fake_x_value
		fyv = bpy.context.scene.orthoempty_props.fake_y_value
		fzv = bpy.context.scene.orthoempty_props.fake_z_value
		# vector format
		fv_all = mathutils.Vector((fxv, fyv, fzv))

		# Update Fake coords from modif loc and offset
		bpy.context.scene.orthoempty_props.fake_x_value = objlx + offset_x
		bpy.context.scene.orthoempty_props.fake_y_value = objly + offset_y
		bpy.context.scene.orthoempty_props.fake_z_value = objlz + offset_z

		print ("------------------")
		print ("Real location  = " + str(objl_all))
		print ("offset  values = " + str(offset_all))
		print ("Fake location values = " + str(fv_all))

		self.report({'INFO'}, "> Calculated : Empty fake center´s coordinates")
		
	

		return {'FINISHED'}