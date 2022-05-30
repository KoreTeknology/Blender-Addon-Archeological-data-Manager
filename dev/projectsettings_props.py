import bpy

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

from bpy.types import PropertyGroup


# CLASS group of settings for preferences panel
class Projectsettings_Properties(PropertyGroup):

	x_offset_value : bpy.props.FloatProperty(  
		name="x_offset_value",
		#subtype='FACTOR',
		#default=0.0,
		#min=0.0, max=1000.0,
		precision= 10,
		description="Offset Map along X axis"
		)

	y_offset_value : bpy.props.FloatProperty(  
		name="y_offset_value",
		#subtype='FACTOR',
		#default=0.0,
		#min=0.0, max=1000.0,
		precision= 10,
		description="Offset Map along X axis"
		)

	z_offset_value : bpy.props.FloatProperty(  
		name="z_offset_value",
		#subtype='FACTOR',
		#default=0.0,
		#min=0.0, max=1000.0,
		precision= 10,
		description="Offset Map along X axis"
		)

# assign column number to db for import and export
	col_id : bpy.props.IntProperty(
		name = "Column ID",
		description = "Assign column ID for RegID",
		default = 0
		)

	col_x : bpy.props.IntProperty(
		name = "Column X",
		description = "Assign column X for COL_X",
		default = 1
		)

	col_y : bpy.props.IntProperty(
		name = "Column Y",
		description = "Assign column Y for COL_Y",
		default = 2
		)

	col_z : bpy.props.IntProperty(
		name = "Column Z",
		description = "Assign column Z for COL_Z",
		default = 3
		)

	col_name : bpy.props.IntProperty(
	name = "Column Name",
		description = "Assign column Name for COL_NAME",
		default = 4
		)

	col_fs : bpy.props.IntProperty(
		name = "Column Frame Start",
		description = "Assign column Name for COL_FS",
		default = 5
		)

	col_fe : bpy.props.IntProperty(
		name = "Column Frame end",
		description = "Assign column Name for COL_FE",
		default = 6
		)

	col_mat : bpy.props.IntProperty(
		name = "Column Material ID",
		description = "Assign column Material for COL_MAT",
		default = 7
		)

	col_type : bpy.props.IntProperty(
		name = "Column Type",
		description = "Assign column Type for COL_TYPE",
		default = 8
		)

	col_shape : bpy.props.IntProperty(
		name = "Column Shape",
		description = "Assign column Shape for COL_SHP",
		default = 9
		)


# set options to column selection to import and export
	active_item : bpy.props.BoolProperty(
		name = "actitem",
		description = "active item in DB manipulation",
		default = True
		)

	active_id_import : bpy.props.BoolProperty(
		name = "Activate Import ID data",
		description = "Active item in DB manipulation: Import ID",
		default = True
		)

	active_id_export : bpy.props.BoolProperty(
		name = "Activate Export ID data",
		description = "Active item in DB manipulation: Export ID",
		default = True
		)

	active_long_import : bpy.props.BoolProperty(
		name = "Activate Import Longitude data",
		description = "Active item in DB manipulation: Import Longitude",
		default = True
		)

	active_long_export : bpy.props.BoolProperty(
		name = "Activate Export Longitude data",
		description = "Active item in DB manipulation: Export Longitude",
		default = True
		)

	active_lat_import : bpy.props.BoolProperty(
		name = "Activate Import Latitude data",
		description = "Active item in DB manipulation: Import Latitude",
		default = True
		)

	active_lat_export : bpy.props.BoolProperty(
		name = "Activate Export Latitude data",
		description = "Active item in DB manipulation: Export Latitude",
		default = True
		)

	active_elev_import : bpy.props.BoolProperty(
		name = "Activate Import Elevation data",
		description = "Active item in DB manipulation: Import Elevation",
		default = True
		)

	active_elev_export : bpy.props.BoolProperty(
		name = "Activate Export Elevation data",
		description = "Active item in DB manipulation: Export Elevation",
		default = True
		)

	active_name_import : bpy.props.BoolProperty(
		name = "Activate Import Name data",
		description = "Active item in DB manipulation: Import Name",
		default = True
		)

	active_name_export : bpy.props.BoolProperty(
		name = "Activate Export Name data",
		description = "Active item in DB manipulation: Export Name",
		default = True
		)

	active_type_import : bpy.props.BoolProperty(
		name = "Activate Import Type data",
		description = "Active item in DB manipulation: Import Type",
		default = False
		)

	active_type_export : bpy.props.BoolProperty(
		name = "Activate Export Type data",
		description = "Active item in DB manipulation: Export Type",
		default = False
		)

	active_material_import : bpy.props.BoolProperty(
		name = "Activate Import Material data",
		description = "Active item in DB manipulation: Import Material",
		default = False
		)

	active_material_export : bpy.props.BoolProperty(
		name = "Activate Export Material data",
		description = "Active item in DB manipulation: Export Material",
		default = False
		)

	active_shape_import : bpy.props.BoolProperty(
		name = "Activate Import Shape data",
		description = "Active item in DB manipulation: Import Shape",
		default = False
		)

	active_shape_export : bpy.props.BoolProperty(
		name = "Activate Export Shape data",
		description = "Active item in DB manipulation: Export Shape",
		default = False
		)

	active_sf_import : bpy.props.BoolProperty(
		name = "Activate Import Startframe data",
		description = "Active item in DB manipulation: Import Startframe",
		default = False
		)

	active_sf_export : bpy.props.BoolProperty(
		name = "Activate Export Startframe data",
		description = "Active item in DB manipulation: Export Startframe",
		default = False
		)

	active_ef_import : bpy.props.BoolProperty(
		name = "Activate Import Endframe data",
		description = "Active item in DB manipulation: Import Endframe",
		default = False
		)

	active_ef_export : bpy.props.BoolProperty(
		name = "Activate Export Endframe data",
		description = "Active item in DB manipulation: Export Endframe",
		default = False
		)

