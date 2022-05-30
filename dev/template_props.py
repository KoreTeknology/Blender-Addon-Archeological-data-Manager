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
class Template_Properties(PropertyGroup):

	prop1 : bpy.props.StringProperty(  
		name = "prop 1 string",
		description = "prop 1 string",
		default = "prop1"
		)

	prop2 : FloatVectorProperty(  
		name="color",
		subtype='COLOR',
		default=(1.0, 0.374, 0.001),
		min=0.0, max=1.0,
		description="Selection Color"
		)

	prop3 : BoolProperty(
		name = "Boolean",
		description = "boolean button",
		default = False
		)

	prop4 : IntProperty(
		name = "prop4",
		description = "integer",
		default = 2
		)

	prop5 : FloatProperty(
		name = "prop5",
		description = "float number",
		default = 6.0
		)