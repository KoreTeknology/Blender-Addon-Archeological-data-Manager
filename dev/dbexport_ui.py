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

from . dbexport_props import *

# Panel of db exporter > Main
class VIEW3D_PT_export_db_Panel(Panel):
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"
	bl_label = "Database & Library Exporter"
	bl_idname = "VIEW3D_PT_export_db_Panel"
	bl_category = "Archeology PRO"
	bl_options = {'DEFAULT_CLOSED'}

	def draw_header(self, _):
		layout = self.layout

		from . import preview_collections
		pcoll = preview_collections["main"]
		icon_csvexport = pcoll["icon_csvexport"]

		layout.label(text="", icon_value=icon_csvexport.icon_id)

	def draw(self, context):
		layout = self.layout
		scn = context.scene

		# import db sequences
		col = layout.column(align=True)
		colbox = col.box()
		colboxrow = colbox.row(align=True)
		colboxrow.label(text="Settings:")
		colboxrow.operator("wm.timehelp", text="", icon="QUESTION")

		col = layout.column(align=True)
		splitcol = col.split(factor=0.5, align=True)
		col_scb = splitcol.column(align=False)
		col_scb.alignment="RIGHT"
		col_scb.label(text="Path to .csv file")
		col_scb.label(text="Path to .blend file")
		col_scb.label(text="Option")
		col_scb = splitcol.column(align=False)
		col_scb.prop(scn.dbexport_props, "path_csv", text="")
		col_scb.prop(scn.dbexport_props, "path_blend", text="")

		if scn.dbexport_props.link_switch:
			link_text = "Selected Objects"
			link_icon = "APPEND_BLEND"
		else:
			link_text = "All Scene"
			link_icon = "LINK_BLEND"

		col_scb.prop(scn.dbexport_props,'link_switch', text=link_text, toggle=True, icon=link_icon)
		col_scb.alert = True
		col_scb.operator("render.render", icon="COLLECTION_NEW", text="Export")

		# col = layout.column(align=True)
		# row = col.row(align=True)
		# row.scale_y = 1.5
		# row.operator("render.render", icon="COLLECTION_NEW", text="Export Library")
		# row = col.row(align=True)
		# row.label(text="Help: If you notice an error, check the report!", icon='QUESTION')