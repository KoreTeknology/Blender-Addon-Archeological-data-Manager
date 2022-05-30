import bpy

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

# CLASS group of settings for preferences panel
class ToolbarProperties(PropertyGroup):

	offset : bpy.props.FloatProperty(
		name = 'Offset', 
		default = 0.0
		)

	new_coord : bpy.props.FloatVectorProperty(
		name = "New coordinates", 
		subtype = 'XYZ',
		default = (0.0,0.0,0.0),
		precision=4
		)