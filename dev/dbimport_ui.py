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

from . dbimport_props import *

class VIEW3D_PT_import_db_Panel(Panel):
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"
	bl_label = "Database & Library Importer"
	bl_idname = "VIEW3D_PT_import_db_Panel"
	bl_category = "Archeology PRO"
	bl_options = {'DEFAULT_CLOSED'}

	def draw_header(self, _):
		layout = self.layout

		from . import preview_collections
		pcoll = preview_collections["main"]
		icon_csvimport = pcoll["icon_csvimport"]

		layout.label(text="", icon_value=icon_csvimport.icon_id)

	def draw(self, context):
		layout = self.layout
		scn = bpy.context.scene

		col = layout.column(align=True)
		splitcol = col.split(factor=0.5, align=True)
		col_scb = splitcol.column(align=False)
		col_scb.alignment="RIGHT"
		col_scb.label(text="Path to .csv file")
		col_scb.label(text="Path to .blend file")
		col_scb.label(text="Options")
		col_scb = splitcol.column(align=False)
		col_scb.prop(scn.dbimport_props, "path_csv", text="")
		col_scb.prop(scn.dbimport_props, "path_blend", text="")





		col = layout.column(align=True)
		splitcol = col.split(factor=0.5, align=True)
		col_l = splitcol.column(align=True)
		col_l.label(text='Import Options:')
		col_l.prop(scn.dbimport_props, "imp_empty", text="Add Empty", icon="PROP_ON")
		col_l.prop(scn.dbimport_props, "imp_text", text="Add Text", icon="PROP_ON")
		col_l.prop(scn.dbimport_props, "imp_obj", text="Add Object", icon="PROP_ON")
		col_l.prop(scn.dbimport_props, "imp_obj", text="Add Chronology", icon="PROP_ON")
		col_l = splitcol.column(align=True)
		col_l.label(text='View Options:')
		col_l.prop(scn.dbimport_props, "imp_axis", text="Show Axis", icon="PROP_ON")
		col_l.prop(scn.dbimport_props, "imp_space", text="Show Space", icon="PROP_ON")
		col_l.prop(scn.dbimport_props, "imp_name", text="Show Name", icon="PROP_ON")
		col_l.prop(scn.dbimport_props, "imp_name", text="Show Data", icon="PROP_ON")

		col = layout.column(align=True)
		row = col.row(align=True)

		if scn.dbimport_props.link_switch:
			link_text = "From Append"
			link_icon = "APPEND_BLEND"
		else:
			link_text = "From Link"
			link_icon = "LINK_BLEND"

		row.label(text="Help: If you notice an error, check the report!", icon='QUESTION')

		col = layout.column(align=True)
		row = col.row(align=True)
		row.prop(scn.dbimport_props,'link_switch', text=link_text, toggle=True, icon=link_icon)
		row = col.row(align=True)
		row.scale_y = 1.5
		row.operator("scene.import_db", icon="COLLECTION_NEW", text="Import Library")

