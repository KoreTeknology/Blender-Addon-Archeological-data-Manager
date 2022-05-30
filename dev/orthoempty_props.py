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
class OrthoemptyProperties(PropertyGroup):

	orthoempty_name : bpy.props.StringProperty(  
		name = "Orthoempty Name",
		description = "Orthoempty Name",
		default = "Empty Fake center"
		)

	x_offset_value : bpy.props.FloatProperty(  
		name="x_offset_value",
		#subtype='FACTOR',
		#default=0.0,
		#min=0.0, max=1000.0,
		precision= 2,
		description="Offset Map along X axis"
		)

	y_offset_value : bpy.props.FloatProperty(  
		name="y_offset_value",
		#subtype='FACTOR',
		#default=0.0,
		#min=0.0, max=1000.0,
		precision= 2,
		description="Offset Map along X axis"
		)

	z_offset_value : bpy.props.FloatProperty(  
		name="z_offset_value",
		#subtype='FACTOR',
		#default=0.0,
		#min=0.0, max=1000.0,
		precision= 2,
		description="Offset Map along X axis"
		)

	fake_x_value : bpy.props.FloatProperty(  
		name="fake_x_value",
		#subtype='FACTOR',
		#default=100.0,
		#min=0.0, max=1000.0,
		precision= 2,
		description="Offset Map along X axis"
		)

	fake_y_value : bpy.props.FloatProperty(  
		name="fake_y_value",
		#subtype='FACTOR',
		#default=100.0,
		#min=0.0, max=1000.0,
		precision= 2,
		description="Offset Map along X axis"
		)

	fake_z_value : bpy.props.FloatProperty(  
		name="fake_z_value",
		#subtype='FACTOR',
		#default=100.0,
		#min=0.0, max=1000.0,
		precision= 10,
		description="Offset Map along X axis"
		)
