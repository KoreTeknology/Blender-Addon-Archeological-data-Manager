import bpy, os, sys, csv, struct, datetime

# from bpy.utils import previews
# from bpy.utils.previews import .

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



preview_collections = {}


# ########################################
# PREFERENCES PANEL SECTION
# ########################################

# Add-ons Preferences Panel
class AddonPreferences(AddonPreferences):
	# this must match the addon name, use '__package__'
	# when defining this in a submodule of a python package.
	#bl_idname = __name__
	bl_idname = __package__


	category : bpy.props.StringProperty(
		name="Tab Category",
		description="Choose a name for the category of the panel",
		default="//myCustomFolder",
		maxlen=1024,
		subtype='FILE_PATH'
		)

# GIS options
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

	object_color : bpy.props.FloatVectorProperty(  
		name="object_color",
		subtype='COLOR',
		default=(0.033, 0.033, 0.033),
		min=0.0, max=1.0,
		description="Background Color"
		)

	show_pref0: bpy.props.BoolProperty(
		name="Show Preference 0",
		description="Expand this box to show various debugging tools",
		default=False
		)

	show_pref1: bpy.props.BoolProperty(
		name="Show Preference 1",
		description="Expand this box to show various debugging tools",
		default=False
		)

	show_pref2: bpy.props.BoolProperty(
		name="Show Preference 2",
		description="Expand this box to show release infos",
		default=True
		)

	show_pref3: bpy.props.BoolProperty(
		name="Show Preference 3",
		description="Expand this box to show release infos",
		default=True
		)

	projection_presets: EnumProperty(
		name="Projection Presets",
		default='utm',
		description="Projection presets",
		items = [
			('webmercator', "Web Mercator", "Projection Mercator 1569", 0),
			('utm', "UTM", "Transverse Universal Mercator", 1),
			('wgs', "WGS84", "Classic map Projection", 2)]
		)

	def draw(self, context):
		layout = self.layout

		from . import preview_collections
		pcoll = preview_collections["main"]
		icon_blogo = pcoll["icon_blogo"]
		icon_archeo = pcoll["icon_archeo"]
		icon_uriel = pcoll["icon_uriel"]
		icon_world = pcoll["icon_world"]

		col = layout.column()
		row = col.row()
		row.label(text="Path to projects folder:", icon_value=icon_archeo.icon_id)
		row.prop(self, "category", text="")

		col = layout.column()
		row = col.row()
		row.label(text="Path to objects libraries folder:", icon_value=icon_archeo.icon_id)
		row.prop(self, "category", text="")

		col = layout.column()
		row = col.row()
		row.label(text="Path to databases folder:", icon_value=icon_archeo.icon_id)
		row.prop(self, "category", text="")

		box = layout.box()
		col = box.column()
		row = col.row(align=True)
		row.alignment = 'LEFT'
		row.prop(self,'show_pref0',text="Console options",emboss=False,icon="TRIA_DOWN" if self.show_pref0 else "TRIA_RIGHT")
		if self.show_pref0:
			col = box.column()
			col.label(text="Custom Console Theme Color Schemes:", icon='COLOR')
			row = col.row(align=True)
			row.prop(self, 'object_color', icon="MATFLUID", text="Background color")
			row = col.row(align=True)
			row.prop(self, 'object_color', icon="MATFLUID", text="Text color")
			row = col.row(align=True)
			row.prop(self, 'object_color', icon="MATFLUID", text="Error Background color")
			row = col.row(align=True)
			row.prop(self, 'object_color', icon="MATFLUID", text="Error Text color")
			col = box.column()
			row = col.row(align=True)
			row.operator("infowin.resetcolors", text="Reset theme")
			row.operator("infowin.changecolors", text="Apply custom theme")

# panel 2 GIS options
		box = layout.box()
		col = box.column()
		row = col.row(align=True)
		row.alignment = 'LEFT'
		row.prop(self,'show_pref1',text="Geographic Information System",emboss=False,icon="TRIA_DOWN" if self.show_pref1 else "TRIA_RIGHT")
		row.operator("wm.gishelp", text="", icon="QUESTION", emboss= False)
		row.operator("wm.gishelp", text="", icon="PRESET", emboss= False)

		if self.show_pref1:
			col = box.column()
			row = col.row(align=True)
			row.alert = True
			row.label(text="World Projection System:", icon='ERROR')
			row.prop(self, 'projection_presets',text = "")
			# row.operator("wm.gishelp", text="", icon="QUESTION")
			# row.operator("wm.gishelp", text="", icon="PRESET")
			# col = box.column()
			# row = col.row(align=True)
			# row.alert = True
			# row.label(text="This feature wil be available in a next release !", icon='ERROR')
			# #row.prop(self, 'projection_presets',text = "")

			# col = box.column(align=True)
			# row = col.row(align=True)
			# row.label(text="Advanced Settings:", icon_value=icon_world.icon_id)
			# row.operator("wm.gishelp", text="", icon="QUESTION")
			# row.operator("wm.gishelp", text="", icon="PRESET")

			# col = box.column(align=True)
			# row = col.row(align=True)
			# row.prop(self, 'x_offset_value', text='Longitude (X)')
			# #row = col.row(align=True)
			# row.prop(self, 'y_offset_value', text='Latitude (Y)')
			# #row = col.row(align=True)
			# row.prop(self, 'z_offset_value', text='Altitude (Z)')

			col = box.column(align=True)
			splitcolbox = col.split(factor=0.5, align=False)
			col_scb = splitcolbox.column(align=True)
			col_scb.alert = True
			col_scb.label(text="Adjust scale:", icon='ERROR')
			col_scb.prop(self, 'x_offset_value', text='None')
			# col_scb.prop(self, 'projection_presets',text = "")
			col_scb = splitcolbox.column(align=True)
			col_scb.label(text="Coordinates Offset (m):", icon_value=icon_world.icon_id)
			col_scb.prop(self, 'x_offset_value', text='Longitude (X)')
			col_scb.prop(self, 'y_offset_value', text='Latitude (Y)')
			col_scb.prop(self, 'z_offset_value', text='Altitude (Z)')



# Panel 3 preferences
		box = layout.box()
		col = box.column()
		row = col.row(align=True)
		row.alignment = 'LEFT'
		row.prop(self,
			'show_pref2',
			text="Release Infos",
			emboss=False,
			icon="TRIA_DOWN" if self.show_pref2 else "TRIA_RIGHT")
		if self.show_pref2:
			col = box.column(align=True)

			info = "http://www.urieldeveaud.com"
			info2 = "https://github.com/KoreTeknology/Blender-Addon-Archeological-data-Manager"
			row    = col.row(align=True)
			row.label(text="Release 1.6.2 'Tlaloc'", icon='SCRIPT')
			row.label(text="Archeology Blender Addon", icon_value=icon_archeo.icon_id)
			row    = col.row(align=True)
			row.label(text="Release Date: 19/07/2019", icon='INFO')
			row.label(text="Author: Uriel Deveaud", icon_value=icon_uriel.icon_id)
			row    = col.row(align=True)
			row.operator("wm.url_open", text="Advanced Documentation").url = info
			row.operator("wm.url_open", text="Github Repository").url = info2

# Panel 3 preferences
		box = layout.box()
		col = box.column()
		row = col.row(align=True)
		row.alignment = 'LEFT'
		row.prop(self,
			'show_pref3',
			text="Database Import/Export Settings",
			emboss=False,
			icon="TRIA_DOWN" if self.show_pref3 else "TRIA_RIGHT")
		if self.show_pref3:
			col = box.column(align=True)
			row = col.row(align=True)
			row.label(text="here'", icon='SCRIPT')