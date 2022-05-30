import bpy

from bpy.types import Operator

# import for preset add/remove functions
from bl_operators.presets import AddPresetBase



class AddPresetRender(AddPresetBase, Operator):
	"""Add a Render Preset"""
	bl_idname = "scene.preset_add"
	bl_label = "Add Preset"
	preset_menu = "ARCHEO_MT_presets" # your menu's name!

	# IMPORTANT: you need to specify below, what will be serialized to a preset file

	preset_defines = [
		"scene = bpy.context.scene"
	]

	preset_values = [
		"scene.template_props.prop1",
		"scene.template_props.prop2",
		"scene.template_props.prop3",
		"scene.template_props.prop4",
		"scene.template_props.prop5",
	]

	preset_subdir = "archeology_pro/template" # make sure it's the same as in your menu class

# HELP SECTION
class WM_OT_templatehelp(bpy.types.Operator):
	bl_idname = "wm.templatehelp"
	bl_label = "Template Help"
	bl_description = "Help - click to read basic information"

	def draw(self, context):
		layout = self.layout
		layout.label(text="Description:")
		layout.label(text="- Template help")
		layout.label(text="...")
		layout.label(text="...")

	def execute(self, context):
		return {"FINISHED"}

	def invoke(self, context, event):
		return context.window_manager.invoke_popup(self, width=220)