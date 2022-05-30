#---------------------------------------------
# Title: chronodesign_props.py
# Author: Uriel Deveaud @2019
#---------------------------------------------

# ########################### 
# IMPORT MODULES  
# ########################### 
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

# Create custom property group
class MarkerList(bpy.types.PropertyGroup):
	'''name = StringProperty() '''
	frame : IntProperty()
	comment : StringProperty(default = "No Comment")
	markerid : IntProperty()




# CLASS group of settings for chronology create
class ChronodesignProperties(PropertyGroup):

	chrono_start : IntProperty(
		name = "Start chronology strip",
		description = "Chronology strip start frame",
		default = 10
		)

	chrono_end : IntProperty(
		name = "End chronology strip",
		description = "Chronology strip end frame",
		default = 100
		)

	chrono_channel : IntProperty(
		name = "Channel chronology strip",
		description = "Chronology strip channel",
		default = 2
		)

	chrono_color : FloatVectorProperty(  
		name="strip_color",
		subtype='COLOR',
		default=(1, 0.87, 0.34),
		min=0.0, max=1.0,
		description="Strip Color"
		)

	chrono_name : StringProperty(
		name = "Strip Name",
		description = "Strip name",
		default = "New Phase name"
		)

	chrono_marker : BoolProperty(
		name = "Add marker ",
		description = "Add marker to timeline",
		default = True
		)

	path_chrono : bpy.props.StringProperty(
		name="Path to db",
		description="Choose a name for the category of the panel",
		default="//(.csv)"
		)