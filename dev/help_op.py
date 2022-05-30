import bpy

from bpy.types import Operator

# ########################################
# HELP SECTIONS
# ########################################

# ########################################
# Geo Inf Sys help
class WM_OT_gishelp(bpy.types.Operator):
	bl_idname = "wm.gishelp"
	bl_label = "Gis Help"
	bl_description = "Help - click to read basic information"

	def draw(self, context):
		layout = self.layout
		layout.label(text="Description:")
		layout.label(text="- GIS Settings to relative mapping")
		layout.label(text="Set the central reference point")
		layout.label(text="as exact coordinates")

	def execute(self, context):
		return {"FINISHED"}

	def invoke(self, context, event):
		return context.window_manager.invoke_popup(self, width=220)

# ########################################
# database help
class WM_OT_dbhelp(bpy.types.Operator):
	bl_idname = "wm.dbhelp"
	bl_label = "Database Help"
	bl_description = "Help - click to read basic information"

	def draw(self, context):
		layout = self.layout
		layout.label(text="Description:")
		layout.label(text="- GIS Settings to relative mapping")
		layout.label(text="Set the central reference point")
		layout.label(text="as exact coordinates")

	def execute(self, context):
		return {"FINISHED"}

	def invoke(self, context, event):
		return context.window_manager.invoke_popup(self, width=220)


# ########################################
# database help
class WM_OT_timehelp(bpy.types.Operator):
	bl_idname = "wm.timehelp"
	bl_label = "time Help"
	bl_description = "Help - click to read basic information"

	def draw(self, context):
		layout = self.layout
		layout.label(text="Description:")
		layout.label(text="- time Settings to relative mapping")
		layout.label(text="Set the central reference point")
		layout.label(text="as exact coordinates")

	def execute(self, context):
		return {"FINISHED"}

	def invoke(self, context, event):
		return context.window_manager.invoke_popup(self, width=220)


