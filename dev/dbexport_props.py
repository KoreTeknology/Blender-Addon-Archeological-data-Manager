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
class DbexportProperties(PropertyGroup):

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

	link_switch : bpy.props.BoolProperty(
		name = "Link",
		description = "linkswitch",
		default = True
		)