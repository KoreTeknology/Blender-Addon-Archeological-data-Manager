
bl_info = {
	"name": "Archeology PRO",
	"author": "Uriel Deveaud",
	"version": (1, 7, 2),
	"blender": (2, 80, 0),
	"location": "3D View > Tools > N panel",
	"description": "Addon for blender 2.8",
	"warning": "This Addon is in constant progress! Please, report any bugs, thx",
	"wiki_url": "http://www.urieldeveaud.com/blender/scripts",
	"tracker_url": "http://www.urieldeveaud.com/blender/scripts",
	"support": "COMMUNITY",
	"category": "ARCHEOLOGY ADDONS"}

# ########################################
# IMPORT SECTION
# ########################################

# Extra files IMPORT
if "bpy" in locals():
	import imp

	imp.reload(prefs_op)
	imp.reload(prefs_ui)

	imp.reload(toolbar_props)
	imp.reload(toolbar_ui)

	imp.reload(help_op)

	imp.reload(template_op)
	imp.reload(template_ui)
	imp.reload(template_props)

	imp.reload(orthocam_op)
	imp.reload(orthocam_ui)
	imp.reload(orthocam_props)

	imp.reload(orthogrid_op)
	imp.reload(orthogrid_ui)
	imp.reload(orthogrid_props)

	imp.reload(orthoempty_props)
	imp.reload(orthoempty_op)
	imp.reload(orthoempty_ui)

	imp.reload(objectedit_op)
	imp.reload(objectedit_ui)
	#imp.reload(objectedit_props)

	imp.reload(dbimport_op)
	imp.reload(dbimport_ui)
	imp.reload(dbimport_props)

	#imp.reload(dbexport_op)
	imp.reload(dbexport_ui)
	imp.reload(dbexport_props)

	imp.reload(chronodesign_op)
	imp.reload(chronodesign_ui)
	imp.reload(chronodesign_props)

	imp.reload(projectsettings_op)
	imp.reload(projectsettings_ui)
	imp.reload(projectsettings_props)

else:
	from . import prefs_op
	from . import prefs_ui

	from . import toolbar_props
	from . import toolbar_ui

	from . import help_op

	from . import template_op
	from . import template_ui
	from . import template_props

	from . import orthocam_op
	from . import orthocam_ui
	from . import orthocam_props

	from . import orthogrid_op
	from . import orthogrid_ui
	from . import orthogrid_props

	from . import orthoempty_props
	from . import orthoempty_op
	from . import orthoempty_ui

	from . import objectedit_op
	from . import objectedit_ui
	#from . import objectedit_props

	from . import dbimport_op
	from . import dbimport_ui
	from . import dbimport_props

	#from . import dbexport_op
	from . import dbexport_ui
	from . import dbexport_props

	from . import chronodesign_op
	from . import chronodesign_ui
	from . import chronodesign_props

	from . import projectsettings_op
	from . import projectsettings_ui
	from . import projectsettings_props


# Main IMPORT MODULES
import bpy, sys, csv, struct, datetime
import os, shutil

from os import path
icon_dir = path.join(path.dirname(__file__), "icons")
preview_collections = {}

import bpy.utils.previews

from bpy.types import (
	AddonPreferences,
	Operator,
	Panel,
	Menu,
	UIList,
	PropertyGroup,
	Sequences,
	WorkSpaceTool,
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


# ########################################
# REGISTER SECTION
# ########################################

classes = (
		prefs_ui.AddonPreferences,

		toolbar_props.ToolbarProperties,
		toolbar_ui.VIEW3D_PT_toolbar_Panel,
# HELP SECTION
		help_op.WM_OT_gishelp,
		help_op.WM_OT_dbhelp,
		help_op.WM_OT_timehelp,

		projectsettings_ui.VIEW3D_PT_projectsettings_panel,
		projectsettings_props.Projectsettings_Properties,

		orthocam_ui.VIEW3D_PT_orthocam_panel,
		orthocam_op.SCENE_OT_add_orthocam,
		orthocam_props.OrthocamProperties,

		orthogrid_ui.VIEW3D_PT_orthogrid_panel,
		orthogrid_op.SCENE_OT_add_orthogrid,
		orthogrid_props.OrthogridProperties,

		orthoempty_ui.VIEW3D_PT_orthoempty_panel,
		orthoempty_op.SCENE_OT_add_orthoempty,
		orthoempty_props.OrthoemptyProperties,
		orthoempty_op.SCENE_OT_fake_coord_orthoempty,

		objectedit_ui.VIEW3D_PT_objectedit_Panel,
		objectedit_op.OBJECT_OT_edit_properties,
		objectedit_op.OBJECT_OT_modif_properties,
		objectedit_op.OBJECT_OT_delete_properties,
		objectedit_op.OBJECT_OT_add_material,
# test open messagebox
		objectedit_op.OBJECT_OT_open_dialog,

		dbimport_ui.VIEW3D_PT_import_db_Panel,
		dbimport_op.SCENE_OT_Import_db,
		dbimport_props.DbimportProperties,

		dbexport_ui.VIEW3D_PT_export_db_Panel,
		#dbexport_op.SCENE_OT_Export_db,
		dbexport_props.DbexportProperties,

		chronodesign_ui.MARKERLIST_UL_Items,
		chronodesign_ui.VIEW3D_PT_chronodesign_Panel,
		chronodesign_op.SEQWIN_OT_open,
		chronodesign_op.SEQWIN_OT_Create_chrono,
		chronodesign_op.Markerlist_refresh,
		chronodesign_op.Markerlist_add,
		chronodesign_op.Markerlist_delete,
		chronodesign_op.Markerlist_select,
		chronodesign_op.Markerlist_jumpto,
		chronodesign_op.Markerlist_Gotoprevious,
		chronodesign_op.Markerlist_Gotonext,
		chronodesign_op.AddChronologyOperator,
		chronodesign_props.ChronodesignProperties,
		chronodesign_props.MarkerList,

		# Template
		template_op.WM_OT_templatehelp,
		template_ui.VIEW3D_PT_template_panel,
		template_ui.VIEW3D_PT_template2_panel,
		template_props.Template_Properties,
		# test presets in template
		template_ui.ARCHEO_MT_presets,
		template_op.AddPresetRender,
		)


# Register
def register():
# Register ToolbarUI (Experimental !)
	bpy.utils.register_tool(chronodesign_ui.MyTool, after={"builtin.scale_cage"}, separator=True, group=True)


# Register icons preview
	pcoll = bpy.utils.previews.new()
	icons = {
		"icon_archeo" : "ARCHEO16.png",
		"icon_blogo" : "BLOGO16.png",
		"icon_calendar" : "CALENDAR16.png",
		"icon_calendarplus" : "CALENDARPLUS16.png",
		"icon_camera" : "CAMERA16b.png",
		"icon_chart" : "CHART16.png",
		"icon_chrono" : "CHRONO16.png",
		"icon_circle" : "CIRCLE16.png",
		"icon_coord" : "COORD16.png",
		"icon_cross" : "CROSS16.png",
		"icon_csvexport" : "CSVEXPORT16.png",
		"icon_csvimport" : "CSVIMPORT16.png",
		"icon_datadetails" : "DATADETAILS16.png",
		"icon_dbcol" : "DBCOL16.png",
		"icon_dbexport" : "DBEXPORT16.png",
		"icon_dbset" : "DBSET16.png",
		"icon_east" : "EAST16.png",
		"icon_eye" : "EYE16.png",
		"icon_filter" : "FILTER16.png",
		"icon_globe" : "GLOBE16.png",
		"icon_grid" : "GRID16.png",
		"icon_info" : "INFO16.png",
		"icon_mapmarker" : "MAPMARKER16.png",
		"icon_north" : "NORTH16.png",
		"icon_northdir" : "NORTHDIR16.png",
		"icon_offset" : "OFFSET16.png",
		"icon_placemarker" : "PLACEMARKER16.png",
		"icon_sat" : "SAT16.png",
		"icon_settings" : "SETTINGS16.png",
		"icon_south" : "SOUTH16.png",
		"icon_spreadsheet" : "SPREADSHEET16.png",
		"icon_square" : "SQUARE16.png",
		"icon_star" : "STAR16.png",
		"icon_streetview" : "STREETVIEW16.png",
		"icon_table" : "TABLE16.png",
		"icon_timeslider" : "TIMESLIDER16.png",
		"icon_timezone" : "TIMEZONE16.png",
		"icon_tool" : "TOOL16.png",
		"icon_triangle" : "TRIANGLE16.png",
		"icon_uriel" : "URIEL16.png",
		"icon_uriel64" : "URIEL64.png",
		"icon_viewdetails" : "VIEWDETAILS16.png",
		"icon_west" : "WEST16.png",
		"icon_world" : "WORLD16.png",
		"icon_zoom" : "ZOOM16.png",
		"icon_ruler" : "RULER32.png",
		"icon_camera32" : "CAMERA32.png",
		}
	for key, f in icons.items():
		pcoll.load(key, path.join(icon_dir, f), 'IMAGE')

	preview_collections["main"] = pcoll


# Register Classes
	from bpy.utils import register_class
	for cls in classes:
		register_class(cls)

# Register propertygroups
	bpy.types.Scene.template_props = bpy.props.PointerProperty(type=template_props.Template_Properties)
	bpy.types.Scene.orthocam_props = bpy.props.PointerProperty(type=orthocam_props.OrthocamProperties)
	bpy.types.Scene.orthogrid_props = bpy.props.PointerProperty(type=orthogrid_props.OrthogridProperties)
	bpy.types.Scene.orthoempty_props = bpy.props.PointerProperty(type=orthoempty_props.OrthoemptyProperties)
	bpy.types.Scene.projectsettings_props = bpy.props.PointerProperty(type=projectsettings_props.Projectsettings_Properties)
	bpy.types.Scene.dbimport_props = bpy.props.PointerProperty(type=dbimport_props.DbimportProperties)
	bpy.types.Scene.dbexport_props = bpy.props.PointerProperty(type=dbexport_props.DbexportProperties)
	bpy.types.Scene.chronodesign_props = bpy.props.PointerProperty(type=chronodesign_props.ChronodesignProperties)
	bpy.types.Scene.toolbar_props = bpy.props.PointerProperty(type=toolbar_props.ToolbarProperties)

	# Register marker list
	bpy.types.Scene.markerlist = bpy.props.CollectionProperty(type=chronodesign_props.MarkerList)
	bpy.types.Scene.marker_index = IntProperty()
	bpy.types.Scene.markerlist_copyall = bpy.props.BoolProperty(
		name="Copy All Markers",
		description="Copy All Markers to selected Scene",
		default = False)



def unregister():
# Unregister ToolbarUI (experiemntal !)
	bpy.utils.unregister_tool(chronodesign_ui.MyTool)

# Unregister propertygroups
	del bpy.types.Scene.template_props
	del bpy.types.Scene.projectsettings_props
	del bpy.types.Scene.orthocam_props
	del bpy.types.Scene.orthogrid_props
	del bpy.types.Scene.orthoempty_props
	del bpy.types.Scene.dbimport_props
	del bpy.types.Scene.dbexport_props
	del bpy.types.Scene.chronodesign_props
	del bpy.types.Scene.toolbar_props

# unregister marker list
	del bpy.types.Scene.markerlist
	del bpy.types.Scene.marker_index
	del bpy.types.Scene.markerlist_copyall

# Unregister classes
	from bpy.utils import unregister_class
	for cls in reversed(classes):
		unregister_class(cls)


# Unregister icons preview
	for pcoll in preview_collections.values():
		bpy.utils.previews.remove(pcoll)
	preview_collections.clear()


if __name__ == "__main__":
	register()








