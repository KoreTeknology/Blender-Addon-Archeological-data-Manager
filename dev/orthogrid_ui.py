from bpy.props import (StringProperty,
						BoolProperty,
						IntProperty,
						FloatProperty,
						FloatVectorProperty,
						EnumProperty,
						PointerProperty,
						)

from bpy.types import (Panel, Operator, Menu, UIList)

from . orthogrid_props import *

# Panel for Orthocam
class VIEW3D_PT_orthogrid_panel(Panel):
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"
	bl_label = "Orthographic Grid"
	bl_idname      = "VIEW3D_PT_orthogrid_panel"
	bl_category = "Archeology PRO"
	bl_options     = {'DEFAULT_CLOSED'}

	def draw_header(self, _):
		layout = self.layout

		from . import preview_collections
		pcoll = preview_collections["main"]
		icon_grid = pcoll["icon_grid"]

		layout.label(text="", icon_value=icon_grid.icon_id)

	def draw(self, context):
		layout = self.layout
		scn = context.scene

		col = layout.column(align=True)
		row = col.row(align=True)
		row.label(text="Presets")
		row.prop(scn.orthogrid_props, 'grid_presets',text = "")
		col = layout.column(align=True)
		row = col.row(align=True)
		row.prop(scn.orthogrid_props, 'gridsize_x',text = "Size X (m)")
		row.prop(scn.orthogrid_props, 'gridsize_y',text = "Size Y (m)")
		col = layout.column(align=True)
		row = col.row(align=True)
		row.prop(scn.orthogrid_props, 'gridsubdiv_x', text = "Divisions X")
		row.prop(scn.orthogrid_props, 'gridsubdiv_y', text = "Divisions Y")
		col = layout.column(align=True)
		row = col.row(align=True) 
		row.prop(scn.orthogrid_props, 'show_name', toggle=True, text = "Show Name", icon="PROP_OFF")
		row = col.row(align=True)
		row.prop(scn.orthogrid_props, 'show_axis', toggle=True, text = "Show Axis", icon="PROP_OFF")
		row = col.row(align=True)
		row.prop(scn.orthogrid_props, 'show_space', toggle=True, text = "Show space", icon="PROP_OFF")
		col = layout.column(align=True)
		row = col.row(align=True) 
		row.prop(scn.orthogrid_props, 'grid_name', text="")
		row.operator('scene.add_orthogrid',text="Create Grid", icon='GRID')