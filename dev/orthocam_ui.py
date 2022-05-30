import bpy

from bpy.props import (StringProperty,
						BoolProperty,
						IntProperty,
						FloatProperty,
						FloatVectorProperty,
						EnumProperty,
						PointerProperty,
						)

from bpy.types import (Panel, Operator, Menu, UIList)

from . orthocam_props import *

# Panel for Orthocam
class VIEW3D_PT_orthocam_panel(Panel):
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"
	bl_label = "Orthographic Camera"
	bl_idname      = "VIEW3D_PT_orthocam_panel"
	bl_category = "Archeology PRO"
	bl_options     = {'DEFAULT_CLOSED'}

	def draw_header(self, _):
		layout = self.layout

		from . import preview_collections
		pcoll = preview_collections["main"]
		icon_camera = pcoll["icon_camera"]

		layout.label(text="", icon_value=icon_camera.icon_id)

	def draw(self, context):
		layout = self.layout
		col = layout.column(align=True)
		scn = context.scene
		oc = bpy.context.scene.orthocam_props.orthocam_name 

		if bpy.data.objects.get(oc) is not None:
			cam = bpy.data.cameras[oc]
			rd = scn.render
			rdis = rd.image_settings

			col = layout.column(align=True)
			row = col.row(align=True)
			row.scale_y = 1.5
			row.operator("render.render", text="Take Picture")
			row = col.row(align=True)
			row.prop(rd, "filepath", text="")

			col = layout.column(align=True)
			row = col.row(align=False)
			row.label(text="Color Mode:")
			row.prop(rdis, "color_mode", text="") # , expand=True
			row = col.row(align=False)
			row.label(text="Resolution:")
			row.prop(rd, "resolution_percentage", text="")
			col = layout.column(align=True)
			row = col.row(align=True)
			row.prop(rd, "resolution_x", text="Width")
			row.prop(rd, "resolution_y", text="Height")


			col = layout.column(align=True)
			row = col.row(align=True)
			row.label(text="Camera settings:")
			row = col.row(align=True)
			#row.prop(cam, "sensor_width", text="f")
			row.prop(cam, 'ortho_scale', text = "Zoom")

			obj = bpy.data.objects[oc]
			row = col.row(align=True)
			row.prop(obj, 'location', text = "")
			row = col.row(align=True)
			row.prop(obj,"name", icon='OBJECT_DATA', text="")

			cam = bpy.data.cameras[oc]
			row = col.row(align=True)
			row.label(text="Passepartout:")
			row = col.row(align=True)
			row.prop(cam, "show_passepartout", icon = "RESTRICT_VIEW_OFF", text="",toggle=True)
			row.prop(cam, "passepartout_alpha", text="Set Alpha", slider=True)

		else:
			#col = layout.column(align=True)
			box = col.box()
			colbox = box.column(align=True)
			rowcolbox = colbox.row(align=True)
			rowcolbox.alignment = 'CENTER'
			rowcolbox.alert = True
			rowcolbox.label(text="'OrthoCam does not exist !", icon = "ERROR")


			col = layout.column(align=True)
			splitcol = col.split(factor=0.5, align=True)
			col_scb = splitcol.column(align=False)
			col_scb.alignment="RIGHT"
			col_scb.label(text="Name")
			col_scb = splitcol.column(align=False)
			col_scb.prop(scn.orthocam_props, "orthocam_name", text="")
			col_scb.operator('scene.add_orthocam',text="Create Camera", icon='CAMERA_DATA')




