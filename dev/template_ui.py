import bpy, os

from bpy.props import (StringProperty,
						BoolProperty,
						IntProperty,
						FloatProperty,
						FloatVectorProperty,
						EnumProperty,
						PointerProperty,
						)

from bpy.types import (Panel, Operator, Menu, UIList)

# import for preset add/remove functions
from bl_operators.presets import AddPresetBase

# import properties
from . template_props import *

class ARCHEO_MT_presets(Menu):
	bl_label = "Template Presets"
	preset_subdir = "archeology_pro/template" # you might wanna change this
	preset_operator = "script.execute_preset" # but not this
	draw = Menu.draw_preset # or that


# Panel for project settings panel
class VIEW3D_PT_template_panel(Panel):
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"
	bl_label = "Labels & UI Elements"
	bl_idname      = "VIEW3D_PT_template_panel"
	bl_category = "Templates"
	#bl_options     = {'DEFAULT_CLOSED'}

	def draw(self, context):
		layout = self.layout
		scn = context.scene

		from . import preview_collections
		pcoll = preview_collections["main"]
		icon_blogo = pcoll["icon_blogo"]
		icon_archeo = pcoll["icon_archeo"]


		col = layout.column(align=True)
		row = col.row(align=True)
		row.label(text="Simple Label Left aligned with Help button", icon_value=icon_archeo.icon_id)
		row.operator("wm.templatehelp", text="", icon="QUESTION")

		col = layout.column(align=True)
		row = col.row(align=True)
		row.alignment = 'RIGHT'
		row.alert = True
		row.label(text="Simple Alert Label Right aligned", icon="ERROR")

		col = layout.column(align=True)
		box = col.box()
		rowbox = box.row(align=True)
		rowbox.alignment = 'CENTER'
		rowbox.alert = True
		rowbox.label(text="Alert Label centered in Box", icon="ERROR")

		col = layout.column(align=True)
		row = col.row(align=True)
		row.label(text="Custom icon", icon_value=icon_archeo.icon_id)




# Panel for project settings panel 2
class VIEW3D_PT_template2_panel(Panel):
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"
	bl_label = "UI Properties and Presets Menu"
	bl_idname      = "VIEW3D_PT_template2_panel"
	bl_category = "Templates"
	#bl_options     = {'DEFAULT_CLOSED'}

	def draw(self, context):
		layout = self.layout
		scn = context.scene

# test preset bar menu in
		col = layout.column(align=True)
		row = col.row(align=True)
		row.label(text="Presets:")
		row = col.row(align=True)
		row.menu("ARCHEO_MT_presets", text=bpy.types.ARCHEO_MT_presets.bl_label)
		row.operator("scene.preset_add", text="", icon='ADD')
		row.operator("scene.preset_add", text="", icon='REMOVE').remove_active = True
# properties
		col = layout.column(align=True)
		row = col.row(align=True)
		row.label(text="String property:")
		row.prop(scn.template_props, "prop1", text="")

		col = layout.column(align=True)
		row = col.row(align=True)
		row.label(text="FloatVector property:")
		row.prop(scn.template_props, "prop2", text="")

		col = layout.column(align=True)
		row = col.row(align=True)
		row.label(text="Boolean property:")
		row.prop(scn.template_props, "prop3", text="Toggle", toggle=True)

		col = layout.column(align=True)
		row = col.row(align=True)
		row.label(text="Integer property:")
		row.prop(scn.template_props, "prop4", text="")

		col = layout.column(align=True)
		row = col.row(align=True)
		row.label(text="Float property:")
		row.prop(scn.template_props, "prop5", text="")



