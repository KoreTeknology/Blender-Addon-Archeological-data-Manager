import bpy

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       CollectionProperty,
                       )

# Access UI types       
from bpy.types import PropertyGroup

############################ 
# GRID OBJECT PROPERTIES
############################ 

# CLASS group of settings for grid object
class OrthogridProperties(PropertyGroup):

	gridsize_x : IntProperty(
		name = "Size X",
		description = "Grid Size X, Enter an integer value for COUNT_X",
		default = 1
		)

	gridsize_y : IntProperty(
		name = "Size Y",
		description = "Grid Size Y, Enter an integer value for COUNT_Y",
		default = 1
		)

	gridsubdiv_x : IntProperty(
		name = "Subdiv X",
		description = "Grid Subdivide X, Enter an integer value for COUNT_SUBDIV_X",
		default = 11
		)

	gridsubdiv_y : IntProperty(
		name = "Subdiv Y",
		description = "Grid Subdivide Y, Enter an integer value for COUNT_SUBDIV_Y",
		default = 11
		)

	show_name : BoolProperty(
		name = "Show Name",
		description = "Show Grid Name, True or False?",
		default = True
		)

	show_axis : BoolProperty(
		name = "Show Axis",
		description = "Show Grid Axis, True or False?",
		default = False
		)

	show_space : BoolProperty(
		name = "Show Space",
		description = "Show Grid Space, True or False?",
		default = True
		)

	grid_name : StringProperty(
		name = "Define Grid Name",
		description = "Show Grid Space, True or False?",
		default = "MyGrid"
		)

	grid_orientation : FloatProperty(
		name = "Orientation from North Angle",
		description = "Grid orientation, Enter an float value",
		default = 0.0
		)

	grid_presets: EnumProperty(
		name="Grid Presets",
		default='1x1',
		description="Grid presets",
		items = [
			('1x1', "1m x 1m", "Blender: Basic quadgrid 1m", 0),
			('1x10', "1m x 10m", "Blender: Large 1x10m", 1),
			('10x10', "10m x 10m", "Blender: 100m2", 2)]
		)