import bpy

from bpy.types import Panel, Object


# Panel of db Exporter > Sub: check consistency
class VIEW3D_PT_objectedit_Panel(Panel):
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"
	bl_label = "Active Object Data Editor"
	bl_category = "Archeology PRO"
	bl_idname      = "VIEW3D_PT_objectedit_Panel"
	bl_options     = {'DEFAULT_CLOSED'}

	def draw_header(self, _):
		layout = self.layout

		from . import preview_collections
		pcoll = preview_collections["main"]
		icon_viewdetails = pcoll["icon_viewdetails"]

		layout.label(text="", icon_value=icon_viewdetails.icon_id)

	def draw(self, context):
		layout = self.layout
		scn = context.scene
		
		#obj = bpy.context.object
		obj = context.active_object

		# col = layout.column(align=True)
		# row = col.row(align=True)
		# import db sequences
		col = layout.column(align=True)
		colbox = col.box()
		colboxrow = colbox.row(align=True)
		colboxrow.label(text="Object Data basic:")
		colboxrow.operator("wm.timehelp", text="", icon="QUESTION")

		#if obj.type in ['MESH']:
		
		#if obj.type == 'MESH' :
		
		if (obj and obj.type=='MESH'):
		
			#row.label(text="Object "+obj.name+" is selected", icon="INFO")
			#row = col.row(align=True)

			col = layout.column(align=True)
			splitcol = col.split(factor=0.5, align=False)
			col_scb = splitcol.column(align=True)
			col_scb.alignment="RIGHT"
			col_scb.label(text="Name:")
			col_scb.label(text = "Location:")
			col_scb = splitcol.column(align=False)
			col_scb.prop(obj, "name", text="")
			col_scb.prop(obj, 'location', text="")

			col = layout.column(align=True)
			# row = col.row(align=True)
			# row.label(text = "Name:")
			# row.prop(obj, "name", text="")
			#col = layout.column(align=True)
			# row = col.row(align=True)
			# row.label(text = "Location:")
			# col = layout.column(align=True)
			# col.prop(obj, 'location', text="")
			# IF Object has material
			if obj.active_material_index:
				#row = col.row(align=True)
				#row.label(text="object has material", icon="INFO")  
				#row = col.row(align=True)
				#row.prop(obj.active_material_index, "Material", text="") 

				col = layout.column(align=True)
				row = col.row(align=True)
				row.scale_y = 1.5
				row.operator('object.open_dialog', text="Open Object Properties dialog", icon="WINDOW")

				# # IF object has property ID (means that has been edited earlier)
				# if "ID" in obj:
					# col = layout.column(align=True)
					# row = col.row(align=True)
					# row.label(text="Database Table:")
					# row = col.row(align=True)
					# row.label(text="ID:", icon="KEY_HLT")
					# row.prop(obj,'["ID"]')
					# row = col.row(align=True)
					# row.label(text="Ref:", icon="KEYINGSET")
					# row.prop(obj,'["ref"]', text="")

					# col = layout.column(align=True)
					# row = col.row(align=True)
					# row.label(text="Longitude:", icon="WORLD")
					# row.prop(obj,'["Loc x"]', text="X")
					# row = col.row(align=True)
					# row.label(text="Latitude:", icon="WORLD")
					# row.prop(obj,'["Loc y"]', text="Y")
					# row = col.row(align=True)
					# row.label(text="Elevation:", icon="WORLD")
					# row.prop(obj,'["Loc z"]', text="Z")

					# col = layout.column(align=True)
					# row = col.row(align=True)
					# row.label(text="Name:", icon="OBJECT_DATAMODE")
					# # remplace direct value by bpy object name, easy to update
					# #row.prop(obj,'["name"]', text="")
					# row.prop(obj, "name", text="")
					# row = col.row(align=True)
					# row.label(text="Category:", icon="OBJECT_DATAMODE")
					# row.prop(obj,'["category"]', text="")
					# row = col.row(align=True)
					# row.label(text="Type:", icon="OBJECT_DATAMODE")
					# row.prop(obj,'["type"]', text="")
					# row = col.row(align=True)
					# row.label(text="Shape:", icon="OBJECT_DATAMODE")
					# row.prop(obj,'["shape"]', text="")

					# col = layout.column(align=True)
					# row = col.row(align=True)
					# row.label(text="Group:", icon="ZOOM_SELECTED")
					# row.prop(obj,'["group"]', text="")
					# row = col.row(align=True)
					# row.label(text="Collection:", icon="ZOOM_SELECTED")
					# row.prop(obj,'["collection"]', text="")
					# row = col.row(align=True)
					# row.label(text="Notes:", icon="ZOOM_SELECTED")
					# row.prop(obj,'["notes"]', text="")
					# row = col.row(align=True)
					# row.label(text="Project:", icon="ZOOM_SELECTED")
					# row.prop(obj,'["project"]', text="")
					# row = col.row(align=True)
					# row.label(text="Folder:", icon="ZOOM_SELECTED")
					# row.prop(obj,'["folder"]', text="")
					# row = col.row(align=True)
					# row.label(text="Industry:", icon="ZOOM_SELECTED")
					# row.prop(obj,'["industry"]', text="")

					# col = layout.column(align=True)
					# row = col.row(align=True)
					# row.label(text="Material:", icon="MATERIAL_DATA")
					# row.prop(obj,'["material"]', text="")

					# col = layout.column(align=True)
					# row = col.row(align=True)
					# row.label(text="Length:", icon="MESH_CUBE")
					# row.prop(obj,'["length"]', text="")
					# row = col.row(align=True)
					# row.label(text="Width:", icon="MESH_CUBE")
					# row.prop(obj,'["width"]', text="")
					# row = col.row(align=True)
					# row.label(text="Height:", icon="MESH_CUBE")
					# row.prop(obj,'["height"]', text="")

					# col = layout.column(align=True)
					# row = col.row(align=True)
					# row.label(text="Start Year:", icon="TIME")
					# row.prop(obj,'["startyear"]', text="")
					# row = col.row(align=True)
					# row.label(text="End Year:", icon="TIME")
					# row.prop(obj,'["endyear"]', text="")

					# col = layout.column(align=True)
					# row = col.row(align=True)
					# row.operator('object.modif_properties', text = "Update Properties", icon="FILE_REFRESH")
					# row = col.row(align=True)
					# row.operator('object.del_properties', text = "Delete all Properties", icon="X")

					# # check if object location is different from loc x var
					# if obj.location[0] != obj["Loc x"]:
						# col = layout.column(align=True)
						# row = col.row(align=True)
						# row.alert = True
						# row.label(text="Location has changed, Update!", icon="ERROR")

					# # check if object name is different from name var
					# if obj.name != obj["name"]:
						# col = layout.column(align=True)
						# row = col.row(align=True)
						# row.alert = True
						# row.label(text="Name has changed, Update!", icon="ERROR")

					# # check if object material is different from material var
					# if obj.active_material.name != obj["material"]:
						# col = layout.column(align=True)
						# row = col.row(align=True)
						# row.alert = True
						# row.label(text="Material has changed, Update!", icon="ERROR")

				# else:
					# col = layout.column(align=True)
					# box = col.box()
					# colbox = box.column(align=True)
					# rowcolbox = colbox.row(align=True)
					# rowcolbox.alignment = 'CENTER'
					# rowcolbox.alert = True
					# rowcolbox.label(text="'Object has no properties", icon = "ERROR")
					# col = layout.column(align=True)
					# row = col.row(align=True)
					# row.operator('object.edit_properties', text = "Add Properties")

			else:
				col = layout.column(align=True)
				box = col.box()
				colbox = box.column(align=True)
				rowcolbox = colbox.row(align=True)
				rowcolbox.alignment = 'CENTER'
				rowcolbox.alert = True
				rowcolbox.label(text="Object has no material !", icon = "ERROR")
				col = layout.column(align=True)
				row = col.row(align=True)
				row.operator('object.add_material', text="Add material")

		else:
			col = layout.column(align=True)
			box = col.box()
			colbox = box.column(align=True)
			rowcolbox = colbox.row(align=True)
			rowcolbox.alignment = 'CENTER'
			rowcolbox.alert = True
			rowcolbox.label(text="'Select an object MESH first", icon = "ERROR")