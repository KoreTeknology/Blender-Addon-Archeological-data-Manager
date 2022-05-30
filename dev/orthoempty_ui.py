import bpy, os, sys, csv, struct, datetime

from bpy.props import (StringProperty,
						BoolProperty,
						IntProperty,
						FloatProperty,
						FloatVectorProperty,
						EnumProperty,
						PointerProperty,
						)

from bpy.types import (Panel,
						Operator,
						Menu,
						UIList,
						AddonPreferences,
						PropertyGroup,
						)

from . orthoempty_props import *


# Panel for Orthocam
class VIEW3D_PT_orthoempty_panel(Panel):
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"
	bl_label = "Orthographic Empty"
	bl_idname = "VIEW3D_PT_orthoempty_panel"
	bl_category = "Archeology PRO"
	#bl_options= {'DEFAULT_CLOSED'}

	def draw_header(self, _):
		layout = self.layout

		from . import preview_collections
		pcoll = preview_collections["main"]
		icon_coord = pcoll["icon_coord"]

		layout.label(text="", icon_value=icon_coord.icon_id)

	def draw(self, context):
		layout = self.layout

		scn = bpy.context.scene
		# col = layout.column(align=True)
		# row = col.row(align=True)
		# row.label(text="dede")
		# row.prop(scn.orthoempty_props, 'fake_x_value', text="")


		if bpy.data.objects.get("Empty Fake center") is not None:
			emptyobj = bpy.data.objects["Empty Fake center"]
			#scn.orthoempty_props.fake_x_value = scn.orthoempty_props.fake_x_value + Vector((5.0,2.0,0.0))
			#scn.orthoempty_props.fake_x_value = 5.1


			col = layout.column(align=True)
			row = col.row(align=True)
			row.label(text="World location (Global):")
			row = col.row(align=True)
			row.prop(emptyobj,"location", text="")
			row = col.row(align=True)
			row.label(text="Offset (X,Y,Z):")
			row = col.row(align=True)
			row.prop(scn.orthoempty_props, "x_offset_value", text="")
			row.prop(scn.orthoempty_props, "y_offset_value", text="")
			row.prop(scn.orthoempty_props, "z_offset_value", text="")
			row = col.row(align=True)
			row.label(text="Fake coord (X,Y,Z):")
			row = col.row(align=True)
			row.prop(scn.orthoempty_props, "fake_x_value", text="")
			row.prop(scn.orthoempty_props, "fake_y_value", text="")
			row.prop(scn.orthoempty_props, "fake_z_value", text="")
			col = layout.column(align=True)
			row = col.row(align=True)
			row.operator('scene.fake_coord_calculate',text="Calculate", icon='EMPTY_AXIS')

		else:
			col = layout.column(align=True)
			row = col.row(align=True)
			row.operator('scene.add_orthoempty',text="Create Empty", icon='EMPTY_AXIS')


		

		# obj = bpy.data.objects[oe]
		# row = col.row(align=True)
		# row.prop(obj, 'location', text = "")
		# row = col.row(align=True)
		# row.prop(obj,"name", icon='OBJECT_DATA', text="")

