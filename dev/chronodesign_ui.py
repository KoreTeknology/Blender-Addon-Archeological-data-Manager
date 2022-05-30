#---------------------------------------------
# Title: chronodesign_ui.py
# Author: Uriel Deveaud @2019
#---------------------------------------------

# ########################### 
# IMPORT MODULES  
# ########################### 
import bpy, os, sys, csv, struct, datetime

from bpy.types import (
	AddonPreferences,
	Operator,
	Panel,
	Menu,
	UIList,
	PropertyGroup,
	Sequences,
	WorkSpaceTool,
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

from . chronodesign_props import *
from bpy.utils.toolsystem import ToolDef

# custom list UI
class MARKERLIST_UL_Items(UIList):
	def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
		col1_size = 0.3
		col2_size = 0.3
		col3_size = 0.2
		col4_size = 0.2

		col = layout.column()
		row = col.split(factor=col1_size)
		row.prop(item, "name", text="", icon='KEYTYPE_MOVING_HOLD_VEC',  emboss=False, translate=False)
		row = row.split(factor=col1_size)
		row.label(text=str(item.frame), icon='TRACKING_FORWARDS_SINGLE')
		row.prop(item, "comment", icon="ERROR", text="",  emboss=False, translate=False)

	def invoke(self, context, event):
		pass   


# Panel of Chronology Designer > Main
class VIEW3D_PT_chronodesign_Panel(Panel):
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"
	bl_label = "Chronology Designer"
	bl_idname      = "VIEW3D_PT_chronodesign_Panel"
	bl_category = "Archeology PRO"
	bl_options     = {'DEFAULT_CLOSED'}


	def draw_header(self, _):
		layout = self.layout

		from . import preview_collections
		pcoll = preview_collections["main"]
		icon_chrono = pcoll["icon_chrono"]

		layout.label(text="", icon_value=icon_chrono.icon_id)


	def draw(self, context):
		layout = self.layout
		scn = bpy.context.scene
# check if necessary !
		unit = context.scene.unit_settings
		prefs = context.preferences
		view = prefs.view
		edit = prefs.edit


		ts = bpy.context.tool_settings
		mlist = scn.markerlist
		tlmlist = scn.timeline_markers
		idx = scn.marker_index

		# time refs
		col = layout.column(align=True)
		colbox = col.box()
		colboxrow = colbox.row(align=True)
		colboxrow.label(text="Time References:")
		colboxrow.operator("wm.timehelp", text="", icon="QUESTION")
		# ----------------------------
		col = layout.column(align=True)
		splitcol = col.split(factor=0.5, align=True)
		col_scb = splitcol.column(align=False)
		col_scb.alignment="RIGHT"
		col_scb.label(text="Current Year")
		col_scb.label(text="Start Year")
		col_scb.label(text="End Year")
		col_scb = splitcol.column(align=False)
		col_scb.prop(scn, 'frame_current', text='')
		col_scb.prop(scn, 'frame_start', text='')
		col_scb.prop(scn, 'frame_end', text='') 
		colrow_scb = col_scb.row(align=True)
		colrow_scb.operator("screen.frame_jump", text="", icon='REW').end = False
		colrow_scb.operator("screen.animation_play", text="Run", icon='PLAY')
		colrow_scb.operator("screen.frame_jump", text="", icon='FF').end = True

		# col = layout.column(align=True)
		# row = col.row(align=True)
		# row.label(text="Current Year:")
		# row.prop(scn, 'frame_current', text='')
		# row.operator("screen.animation_play", text="", icon='PLAY')
		# # row = col.row(align=True)
		# # row.prop(edit, "use_negative_frames", text="Use B.C Years (Gregorian)", icon="PROP_OFF")
		# # row.prop(scn, 'lock_frame_selection_to_range', text='', icon='HIDE_OFF')
		# row = col.row(align=True)
		# row.label(text="Start Year:")
		# row.prop(scn, 'frame_start', text='')
		# row.operator("screen.frame_jump", text="", icon='REW').end = False
		# row = col.row(align=True)
		# row.label(text="End Year:")
		# row.prop(scn, 'frame_end', text='') 
		# row.operator("screen.frame_jump", text="", icon='FF').end = True


		# import db sequences
		col = layout.column(align=True)
		colbox = col.box()
		colboxrow = colbox.row(align=True)
		colboxrow.label(text="Import from database:")
		colboxrow.operator("wm.timehelp", text="", icon="QUESTION")
		# ----------------------------
		col = layout.column(align=True)
		splitcol = col.split(factor=0.5, align=False)
		col_scb = splitcol.column(align=True)
		col_scb.alignment="RIGHT"
		col_scb.label(text="Path to Database")
		col_scb.label(text="")
		col_scb = splitcol.column(align=False)
		col_scb.prop(scn.chronodesign_props, 'path_chrono', text='') 
		col_scb.operator("seq.addchrono", text="Import")

		# manual creation for sequence
		col = layout.column(align=True)
		colbox = col.box()
		colboxrow = colbox.row(align=True)
		colboxrow.label(text="Create Phase Sequence:")
		colboxrow.operator("wm.timehelp", text="", icon="QUESTION")
		# ----------------------------
		col = layout.column(align=True)
		splitcol = col.split(factor=0.5, align=True)
		col_scb = splitcol.column(align=False)
		col_scb.alignment="RIGHT"
		col_scb.label(text="Name")
		col_scb.label(text="Color")
		col_scb.label(text="Start Year")
		col_scb.label(text="End Year")
		col_scb.label(text="Channel")
		col_scb.label(text="Option")
		col_scb.label(text="")
		col_scb.separator()
		col_scb.alert = True
		col_scb.operator("seqwin.createchrono", text="TEST !", icon='ERROR')
		col_scb = splitcol.column(align=False)
		col_scb.prop(scn.chronodesign_props, 'chrono_name', text="")
		col_scb.prop(scn.chronodesign_props, 'chrono_color', text="")
		col_scb.prop(scn.chronodesign_props, 'chrono_start', text="")
		col_scb.prop(scn.chronodesign_props, 'chrono_end', text="")
		col_scb.prop(scn.chronodesign_props, 'chrono_channel', text="")
		col_scb.prop(scn.chronodesign_props, 'chrono_marker', text="Add Marker", icon="MARKER_HLT") #, toggle=False
		col_scb.operator("seq.addchrono", text="Create")
		col_scb.separator()
		col_scb.operator("seqwin.open", text="Open Chronology", icon="WINDOW")



		# list markers
		col = layout.column(align=True)
		colbox = col.box()
		colboxrow = colbox.row(align=True)
		colboxrow.label(text="Markers Collection:")
		colboxrow.operator("wm.timehelp", text="", icon="QUESTION")
		# ----------------------------
		col = layout.column(align=True)
		row = col.row(align=False)
		rows = 8
		row.template_list("MARKERLIST_UL_Items", "", scn, "markerlist", scn, "marker_index", rows=rows)
		col3 = row.column(align=True)
		col3.operator("markerlist.add_marker", icon="ADD", text="")
		col3.operator("markerlist.delete_marker", icon="REMOVE", text="")
		col3.separator()
		col3.operator("markerlist.refresh", icon="FILE_REFRESH", text="")
		col3.separator()
		col3.operator("markerlist.select_marker", icon="MARKER_HLT", text="")
		col3.separator()
		col3.operator("markerlist.jump_to", icon="NLA_PUSHDOWN", text="")
		col3.separator()
		col3.operator("markerlist.goto_previous", icon="TRIA_LEFT_BAR", text="")
		col3.operator("markerlist.goto_next", icon="TRIA_RIGHT_BAR", text="")

		if scn.marker_index >= 0 and scn.markerlist: 
			item = scn.markerlist[scn.marker_index]
			col = layout.column(align=True)
			row = col.row(align=True)
			row.prop(item, "name", text="", icon="KEYTYPE_MOVING_HOLD_VEC")
			# row.prop(item, "frame", text="", icon="TRACKING_FORWARDS_SINGLE")
			#row.prop(item, "comment", text="", icon="ERROR")


# add toolbar icon
class MyTool(WorkSpaceTool):
	bl_space_type='VIEW_3D'
	bl_context_mode='OBJECT'

	# The prefix of the idname should be your add-on name.
	bl_idname = "my_template.my_circle_select"
	bl_label = "Custom Button"
	bl_description = (
		"This is a tooltip\n"
		"with multiple lines"
	)
	#bl_icon = "NLA"
	bl_widget = None
	bl_keymap = (
		("view3d.select_circle", {"type": 'LEFTMOUSE', "value": 'PRESS'},
			{"properties": [("wait_for_input", False)]}),
		("view3d.select_circle", {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},
			{"properties": [("mode", 'SUB'), ("wait_for_input", False)]}),
	)

	def draw_settings(context, layout, tool):
		props = tool.operator_properties("view3d.select_circle")
		layout.prop(props, "mode")
		layout.prop(props, "radius")
