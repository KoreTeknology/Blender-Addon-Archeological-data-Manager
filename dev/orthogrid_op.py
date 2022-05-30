#---------------------------
# Title: File orthogrid_op.py
#---------------------------

############################ 
# IMPORT MODULES  
############################ 
import bpy

from bpy.types import (
        Panel,
        Operator,
        )

from bpy.props import IntProperty, BoolProperty, StringProperty, PointerProperty

from . orthogrid_props import *

##############################
# OPERATORS
##############################

def add_orthogrid(self, context):
	context = bpy.context
	scn = context.scene
	pos = scn.cursor.location
	#gsx = scn.orthogrid_props.gridsize_x
	
	mesh = bpy.ops.mesh.primitive_grid_add(
		size= 10,
		x_subdivisions=scn.orthogrid_props.gridsubdiv_x, 
		y_subdivisions=scn.orthogrid_props.gridsubdiv_y, 
		#view_align=False, 
		enter_editmode=False, 
		location=pos)


class SCENE_OT_add_orthogrid(Operator):
	"""Create a new Mesh Object"""
	bl_idname = "scene.add_orthogrid"
	bl_label = "Add Grid Object"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		add_orthogrid(self, context)
		context = bpy.context
		scn = context.scene

		# move en edit mode than the center is the corner LeftBottom
		bpy.ops.object.editmode_toggle()
		bpy.ops.transform.translate(value=(0.5, 0, 0), proportional_size=1)
		bpy.ops.transform.translate(value=(0, 0.5, 0), proportional_size=1)

		bpy.ops.mesh.delete(type='ONLY_FACE')
		bpy.ops.object.editmode_toggle()

		# Add object options
		obj = context.active_object
		obj.show_axis = scn.orthogrid_props.show_axis
		obj.show_texture_space = scn.orthogrid_props.show_space
		obj.show_name = scn.orthogrid_props.show_name

		obj.name = scn.orthogrid_props.grid_name

		# array duplicate over x
		bpy.ops.object.modifier_add(type='ARRAY')
		obj.modifiers["Array"].name = "multi4x"
		obj.modifiers["multi4x"].count = scn.orthogrid_props.gridsize_x
		obj.modifiers["multi4x"].use_merge_vertices = True
		obj.modifiers["multi4x"].show_on_cage = True
		obj.modifiers["multi4x"].show_expanded = False
		# array duplicate over y
		bpy.ops.object.modifier_add(type='ARRAY')
		obj.modifiers["Array"].name = "multi4y"
		obj.modifiers["multi4y"].relative_offset_displace[0] = 0
		obj.modifiers["multi4y"].relative_offset_displace[1] = 1
		obj.modifiers["multi4y"].count = scn.orthogrid_props.gridsize_y
		obj.modifiers["multi4y"].use_merge_vertices = True
		obj.modifiers["multi4y"].show_on_cage = True
		obj.modifiers["multi4y"].show_expanded = False
		# apply modifiers
		bpy.ops.object.modifier_apply(apply_as='DATA', modifier="multi4x")
		bpy.ops.object.modifier_apply(apply_as='DATA', modifier="multi4y")


		return {'FINISHED'}

