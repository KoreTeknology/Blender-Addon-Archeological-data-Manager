import bpy, os, sys, csv, struct, datetime


from bpy.types import (
	AddonPreferences,
	Operator,
	Panel,
	Menu,
	UIList,
	PropertyGroup,
	Sequences,
	)

from bpy.props import(
	StringProperty,
	BoolProperty,
	IntProperty,
	FloatProperty,
	FloatVectorProperty,
	EnumProperty,
	PointerProperty,
	CollectionProperty,
	)

from . toolbar_props import *

class VIEW3D_PT_toolbar_Panel(Panel):
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"
	bl_label = "Toolbar"
	bl_category = "Archeology PRO"
	bl_idname      = "VIEW3D_PT_toolbar_Panel"
	#bl_options     = {'DEFAULT_CLOSED'}
	bl_options     = {'HIDE_HEADER'}


	def draw(self, context):
		layout = self.layout

		scn = bpy.context.scene
		obj = bpy.context.object

		from . import preview_collections
		pcoll = preview_collections["main"]
		icon_blogo = pcoll["icon_blogo"]
		icon_archeo = pcoll["icon_archeo"]
		icon_north = pcoll["icon_north"]
		icon_south = pcoll["icon_south"]
		icon_east = pcoll["icon_east"]
		icon_west = pcoll["icon_west"]
		icon_ruler = pcoll["icon_ruler"]
		icon_camera32 = pcoll["icon_camera32"]

		box = layout.box()
		col = box.column(align=True)

		info = "http://www.urieldeveaud.com"
		info2 = "https://github.com/KoreTeknology/Blender-Addon-Archeological-data-Manager"

		row = col.row(align=True)
		row.scale_y = 1.5
		row.operator("wm.url_open", text="Open Database Settings", icon_value=icon_ruler.icon_id).url = info
		col = box.column(align=True)
		row    = col.row(align=True)
		row.scale_y = 1.5
		#row.alignment = 'LEFT'
		row.operator("wm.url_open", text="Open Chronology Panel", icon_value=icon_camera32.icon_id).url = info2
		col = box.column(align=True)
		row    = col.row(align=True)
		row.scale_y = 1.5
		row.operator("wm.url_open", text="Open Object Properties Panel", icon_value=icon_archeo.icon_id).url = info
		#row.separator()
		# col = box.column(align=True)
		# row    = col.row(align=True)
		# row.scale_y = 1.5
		# row.operator("wm.url_open", text="Open ...", icon_value=icon_archeo.icon_id).url = info2
		# col = box.column(align=True)
		# row    = col.row(align=True)
		# row.scale_y = 1.5
		# row.operator("wm.url_open", text="Open ...").url = info

		box = layout.box()
		col = box.column(align=True)
		row = col.row(align=True)
		row.operator("view3d.localview", text="", icon="SCENE_DATA")
		row.operator("view3d.view_persportho", text="", icon='VIEW_PERSPECTIVE')
		row.separator()
		row.operator("view3d.view_axis", text="",icon_value=icon_west.icon_id).type = 'RIGHT'
		row.operator("view3d.view_axis", text="",icon_value=icon_east.icon_id).type = 'LEFT'
		row.operator("view3d.view_axis", text="",icon_value=icon_north.icon_id).type = 'FRONT'
		row.operator("view3d.view_axis", text="",icon_value=icon_south.icon_id).type = 'BACK'
		row.operator("view3d.view_axis", text="", icon='TRACKER').type = 'TOP'

		# box = layout.box()
		# col = box.column(align=True)
		# row = col.row(align=True)
		# row.label(text="New coordinate system:")
		# row = col.row(align=True)
		# row.prop(scn.toolbar_props, 'offset', icon="MATFLUID", text="Offset value")
		# # row = col.row(align=False)
		# # row.prop(scn.toolbar_props, 'new_coord', icon="MATFLUID", text="new coordonates ")

		# row = col.row(align=False)
		# row.prop(scn.toolbar_props, 'new_coord', text="")
		# #row.prop(scn.toolbar_props, 'new_coord[1]', icon="MATFLUID", text="Y:")





