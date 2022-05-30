import bpy

from bpy.props import (StringProperty,
						BoolProperty,
						IntProperty,
						FloatProperty,
						FloatVectorProperty,
						EnumProperty,
						PointerProperty,
						)

from bpy.types import (Panel, Operator, Menu, UIList)

from . projectsettings_props import *

# Panel for project settings panel
class VIEW3D_PT_projectsettings_panel(Panel):
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"
	bl_label = "Database settings"
	bl_idname = "VIEW3D_PT_projectsettings_panel"
	bl_category = "Archeology PRO"
	#bl_options = {'DEFAULT_CLOSED'}

	def draw_header(self, _):
		layout = self.layout

		from . import preview_collections
		pcoll = preview_collections["main"]
		icon_settings = pcoll["icon_settings"]

		layout.label(text="", icon_value=icon_settings.icon_id)

	def draw(self, context):
		layout = self.layout
		scn = context.scene
# check if necessary !
		# unit = context.scene.unit_settings
		# prefs = context.preferences
		# view = prefs.view
		# edit = prefs.edit

		from . import preview_collections
		pcoll = preview_collections["main"]
		icon_world = pcoll["icon_world"]

		# col = layout.column(align=True)
		# row = col.row(align=True)
		# row.label(text="Geographic Information System:", icon_value=icon_world.icon_id)
		# row.operator("wm.gishelp", text="", icon="QUESTION")
		# row.operator("wm.gishelp", text="", icon="PRESET")
		# col = layout.column(align=True)
		# row = col.row(align=True)
		# #row.prop(unit, "length_unit", text="")
		# row.prop(unit, "scale_length", text="Scale")
		# row.prop(unit, "use_separate", icon='HIDE_OFF', text="")
		# col = layout.column(align=True)
		# row = col.row(align=True)
		# row.prop(scn.projectsettings_props, 'x_offset_value', text='Longitude Offset (X)')
		# row = col.row(align=True)
		# row.prop(scn.projectsettings_props, 'y_offset_value', text='Latitude Offset (Y)')
		# row = col.row(align=True)
		# row.prop(scn.projectsettings_props, 'z_offset_value', text='Altitude Offset (Z)')

		# col = layout.column(align=True)
		# row = col.row(align=True)
		# row.label(text="Chronological Time References:")
		# row.operator("wm.timehelp", text="", icon="QUESTION")
		# row.operator("wm.gishelp", text="", icon="PRESET")

		# col = layout.column(align=True)
		# row = col.row(align=True)
		# row.prop(scn, 'frame_current', text='Current Year')
		# row = col.row(align=True)
		# row.prop(edit, "use_negative_frames", text="Use B.C Years (Gregorian)", icon="PROP_OFF")
		# row.prop(scn, 'lock_frame_selection_to_range', text='', icon='HIDE_OFF')
		# row = col.row(align=True)
		# row.prop(scn, 'frame_start', text='Start Year')
		# row.prop(scn, 'frame_end', text='End Year') 


		col = layout.column(align=True)
		row = col.row(align=True)
		row.label(text="Database Column Settings:")
		row.operator("wm.dbhelp", text="", icon="QUESTION")
		row.operator("wm.gishelp", text="", icon="PRESET")

		col = layout.column(align=True)
		box = col.box()
		colbox = box.column(align=True)
		splitcolbox = colbox.split(factor=0.5, align=True)
		col_scb = splitcolbox.column(align=True)
		col_scb.label(text="Data")
		col_scb = splitcolbox.column(align=True)
		col_scb.label(text="Column")
		col_scb = splitcolbox.column(align=True)
		col_scb.label(text="Import")
		col_scb = splitcolbox.column(align=True)
		col_scb.label(text="Export")

		col = layout.column(align=True)
		splitcol = col.split(factor=0.5, align=True)
		col_l = splitcol.column(align=True)
		col_l.alignment="RIGHT"
		col_l.label(text="ID")
		col_l.label(text="Longitude (X)")
		col_l.label(text="Latitude (Y)")
		col_l.label(text="Elevation (Z)")
		col_l.label(text="Object Name")
		col_l.label(text="Type")
		col_l.label(text="Material")
		col_l.label(text="Shape")
		col_l.label(text="Start Year")
		col_l.label(text="End Year")

		col_l = splitcol.column(align=True)
		col_l.prop(scn.projectsettings_props, "col_id", text="")
		col_l.prop(scn.projectsettings_props, "col_x", text="")
		col_l.prop(scn.projectsettings_props, "col_y", text="")
		col_l.prop(scn.projectsettings_props, "col_z", text="")
		col_l.prop(scn.projectsettings_props, "col_name", text="")
		col_l.prop(scn.projectsettings_props, "col_type", text="")
		col_l.prop(scn.projectsettings_props, "col_mat", text="")
		col_l.prop(scn.projectsettings_props, "col_shape", text="")
		col_l.prop(scn.projectsettings_props, "col_fs", text="")
		col_l.prop(scn.projectsettings_props, "col_fe", text="")

		col_l = splitcol.column(align=True)

		if scn.projectsettings_props.active_id_import:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_id_import", text="", icon=active_icon,toggle=True)
		if scn.projectsettings_props.active_long_import:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_long_import", text="", icon=active_icon,toggle=True)
		if scn.projectsettings_props.active_lat_import:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_lat_import", text="", icon=active_icon,toggle=True)
		if scn.projectsettings_props.active_elev_import:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_elev_import", text="", icon=active_icon,toggle=True)
		if scn.projectsettings_props.active_name_import:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_name_import", text="", icon=active_icon,toggle=True)

		if scn.projectsettings_props.active_type_import:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_type_import", text="", icon=active_icon,toggle=True)
		if scn.projectsettings_props.active_material_import:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_material_import", text="", icon=active_icon,toggle=True)
		if scn.projectsettings_props.active_shape_import:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_shape_import", text="", icon=active_icon,toggle=True)

		if scn.projectsettings_props.active_sf_import:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_sf_import", text="", icon=active_icon,toggle=True)
		if scn.projectsettings_props.active_ef_import:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_ef_import", text="", icon=active_icon,toggle=True)

# column of data to EXPORT
		col_l = splitcol.column(align=True)


		if scn.projectsettings_props.active_id_export:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_id_export", text="", icon=active_icon,toggle=True)
		if scn.projectsettings_props.active_long_export:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_long_export", text="", icon=active_icon,toggle=True)
		if scn.projectsettings_props.active_lat_export:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_lat_export", text="", icon=active_icon,toggle=True)
		if scn.projectsettings_props.active_elev_export:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_elev_export", text="", icon=active_icon,toggle=True)
		if scn.projectsettings_props.active_name_export:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_name_export", text="", icon=active_icon,toggle=True)

		if scn.projectsettings_props.active_type_export:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_type_export", text="", icon=active_icon,toggle=True)
		if scn.projectsettings_props.active_material_export:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_material_export", text="", icon=active_icon,toggle=True)
		if scn.projectsettings_props.active_shape_export:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_shape_export", text="", icon=active_icon,toggle=True)

		if scn.projectsettings_props.active_sf_export:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_sf_export", text="", icon=active_icon,toggle=True)
		if scn.projectsettings_props.active_ef_export:
			active_icon = "LINKED"
		else:
			active_icon = "UNLINKED"
		col_l.prop(scn.projectsettings_props, "active_ef_export", text="", icon=active_icon,toggle=True)

# Table config setup
		# col = layout.column(align=True)
		# row = col.row(align=True)
		# row.operator("infowin.open", text="Reset table configuration")
		# row.operator("infowin.open", text="Apply table configuration")





