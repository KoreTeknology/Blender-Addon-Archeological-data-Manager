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
class OrthocamProperties(PropertyGroup):

	orthocam_name : bpy.props.StringProperty(  
		name = "Orthocam Name",
		description = "Orthocam Name",
		default = "Orthocam"
		)