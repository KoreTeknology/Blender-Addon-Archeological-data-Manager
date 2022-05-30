import bpy

from bpy.types import PropertyGroup

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

# CLASS group of settings
class DbimportProperties(PropertyGroup):

	path_csv : bpy.props.StringProperty(
		name="path to csv",
		description="Path to Directory",
		default="//DatabaseFile.csv",
		maxlen=1024,
		subtype='FILE_PATH'
		)

	path_blend : bpy.props.StringProperty(
		name="path to blend",
		description="Path to Directory",
		default="//LibrayFile.blend",
		maxlen=1024,
		subtype='FILE_PATH'
		)

	imp_empty : bpy.props.BoolProperty(
		name = "Import Empty",
		description = "Import Empty at Object Location",
		default = True
		)

	imp_text : bpy.props.BoolProperty(
		name = "Import Text",
		description = "Import Text at Object Location",
		default = True
		)

	imp_obj : bpy.props.BoolProperty(
		name = "Import Object",
		description = "Import Object at DB Location",
		default = True
		)

	imp_axis : bpy.props.BoolProperty(
		name = "Show Axis",
		description = "Import Empty at Object Location",
		default = True
		)

	imp_space : bpy.props.BoolProperty(
		name = "Show Space",
		description = "Import Text at Object Location",
		default = True
		)

	imp_name : bpy.props.BoolProperty(
		name = "Show Name",
		description = "Import Object at DB Location",
		default = True
		)

	link_switch : bpy.props.BoolProperty(
		name = "Link",
		description = "linkswitch",
		default = True
		)