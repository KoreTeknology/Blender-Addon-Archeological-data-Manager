#---------------------------
# Title: File objectedit_op.py
#---------------------------


############################ 
# IMPORT MODULES  
############################ 
import bpy
from bpy.types import Operator
from bpy.props import IntProperty, BoolProperty, StringProperty, PointerProperty


##############################
# OPERATORS
##############################

# if object doesnt have properties, check and create any
class OBJECT_OT_edit_properties(Operator):
	"""Edit Object Properties"""
	bl_idname = "object.edit_properties"
	bl_label = "Edit Object properties"

	def execute(self, context): 
		obj = bpy.context.object
		dim = obj.dimensions

		obj["ID"] = 120
		obj["Loc x"] = obj.location[0]
		obj["Loc y"] = obj.location[1]
		obj["Loc z"] = obj.location[2]

		obj["name"] = obj.name
		obj["material"] = obj.active_material.name

		obj["group"] = "Element"
		obj["collection"] = "Collection A"
		obj["notes"] = "any notes..."
		obj["project"] = "MyProject"
		obj["ref"] = "ABC_e00_o000"
		obj["folder"] = "Folder Path"
		obj["industry"] = "industry name"

		obj["type"] = "Deposit"
		obj["category"] = "Artefact"

		obj["shape"] = "shape"
		obj["length"] = str(round(dim[0], 3))
		obj["width"] = str(round(dim[1], 3))
		obj["height"] = str(round(dim[2], 3))

		obj["startyear"] = "1"
		obj["endyear"] = "2"

		return {'FINISHED'}    

# if object doesnt have properties, check and create any
class OBJECT_OT_modif_properties(Operator):
	"""Modif Object Properties"""
	bl_idname = "object.modif_properties"
	bl_label = "Modify Object properties"

	def execute(self, context): 
		obj = bpy.context.object
		dim = obj.dimensions

		obj["ID"]
		obj["Loc x"] = obj.location[0]
		obj["Loc y"] = obj.location[1]
		obj["Loc z"] = obj.location[2]
        
		obj["name"] = obj.name
		obj["material"] = obj.active_material.name


		obj["group"]
		obj["collection"]
		obj["notes"]
		obj["project"]
		obj["ref"]
		obj["folder"]
		obj["industry"]

		obj["type"]
		obj["category"]
		obj["shape"]
		obj["length"] = str(round(dim[0], 3))
		obj["width"] = str(round(dim[1], 3))
		obj["height"] = str(round(dim[2], 3))
		obj["startyear"]
		obj["endyear"]

		return {'FINISHED'}       



# Delete all properties from selected object
class OBJECT_OT_delete_properties(Operator):
	"""Delete Object Properties"""
	bl_idname = "object.del_properties"
	bl_label = "Delete Object properties"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context): 
		obj = bpy.context.object

		del obj["ID"]
		del obj["name"]
		del obj["material"]

		del obj["Loc x"]
		del obj["Loc y"]
		del obj["Loc z"]

		del obj["type"]

		del obj["group"]
		del obj["collection"]
		del obj["notes"]
		del obj["project"]
		del obj["ref"]
		del obj["folder"]
		del obj["industry"]

		del obj["category"]
		del obj["shape"]
        
		del obj["length"]
		del obj["width"]
		del obj["height"]
		del obj["startyear"]
		del obj["endyear"]

		return {'FINISHED'}    
 

class OBJECT_OT_add_material(Operator):
	"""Delete Object Properties"""
	bl_idname = "object.add_material"
	bl_label = "Add Object material"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context): 
		obj = bpy.context.object.data

		mat_temp = bpy.data.materials.new("Tempmat")
		mat_temp.diffuse_color = (1,0,0,1)
		obj.materials.append(mat_temp)
		bpy.ops.material.new()

		return {'FINISHED'} 


class OBJECT_OT_open_dialog(bpy.types.Operator):
	"""Really?"""
	bl_idname = "object.open_dialog"
	bl_label = "Object Custom Properties Editor"
	bl_options = {'REGISTER', 'INTERNAL'}

	# prop1 = bpy.props.BoolProperty()
	# prop2 = bpy.props.BoolProperty()



	@classmethod
	def poll(cls, context):
		return True


	def execute(self, context):
		self.report({'INFO'}, "Active Object Properties Updated !")
		return {'FINISHED'}

	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self)

	def draw(self, context):

		scn = context.scene
		obj = bpy.context.object

		layout = self.layout
		col = layout.column(align=True)
		row = col.row(align=True)

		# IF object has property ID (means that has been edited earlier)
		if "ID" in obj:
			col = layout.column(align=True)
			row = col.row(align=True)
			row.label(text="Database Table:")
			row = col.row(align=True)
			row.label(text="ID:", icon="KEY_HLT")
			row.prop(obj,'["ID"]')
			row = col.row(align=True)
			row.label(text="Ref:", icon="KEYINGSET")
			row.prop(obj,'["ref"]', text="")


			col = layout.column(align=True)
			row = col.row(align=True)
			row.label(text="Longitude:", icon="WORLD")
			row.prop(obj,'["Loc x"]', text="X")
			row = col.row(align=True)
			row.label(text="Latitude:", icon="WORLD")
			row.prop(obj,'["Loc y"]', text="Y")
			row = col.row(align=True)
			row.label(text="Elevation:", icon="WORLD")
			row.prop(obj,'["Loc z"]', text="Z")


			col = layout.column(align=True)
			row = col.row(align=True)
			row.label(text="Name:", icon="OBJECT_DATAMODE")
			# remplace direct value by bpy object name, easy to update
			#row.prop(obj,'["name"]', text="")
			row.prop(obj, "name", text="")
			row = col.row(align=True)
			row.label(text="Category:", icon="OBJECT_DATAMODE")
			row.prop(obj,'["category"]', text="")
			row = col.row(align=True)
			row.label(text="Type:", icon="OBJECT_DATAMODE")
			row.prop(obj,'["type"]', text="")
			row = col.row(align=True)
			row.label(text="Shape:", icon="OBJECT_DATAMODE")
			row.prop(obj,'["shape"]', text="")


			col = layout.column(align=True)
			row = col.row(align=True)
			row.label(text="Group:", icon="ZOOM_SELECTED")
			row.prop(obj,'["group"]', text="")
			row = col.row(align=True)
			row.label(text="Collection:", icon="ZOOM_SELECTED")
			row.prop(obj,'["collection"]', text="")
			row = col.row(align=True)
			row.label(text="Notes:", icon="ZOOM_SELECTED")
			row.prop(obj,'["notes"]', text="")
			row = col.row(align=True)
			row.label(text="Project:", icon="ZOOM_SELECTED")
			row.prop(obj,'["project"]', text="")
			row = col.row(align=True)
			row.label(text="Folder:", icon="ZOOM_SELECTED")
			row.prop(obj,'["folder"]', text="")
			row = col.row(align=True)
			row.label(text="Industry:", icon="ZOOM_SELECTED")
			row.prop(obj,'["industry"]', text="")

			col = layout.column(align=True)
			row = col.row(align=True)
			row.label(text="Material:", icon="MATERIAL_DATA")
			row.prop(obj,'["material"]', text="")

			col = layout.column(align=True)
			row = col.row(align=True)
			row.label(text="Length:", icon="MESH_CUBE")
			row.prop(obj,'["length"]', text="")
			row = col.row(align=True)
			row.label(text="Width:", icon="MESH_CUBE")
			row.prop(obj,'["width"]', text="")
			row = col.row(align=True)
			row.label(text="Height:", icon="MESH_CUBE")
			row.prop(obj,'["height"]', text="")

			col = layout.column(align=True)
			row = col.row(align=True)
			row.label(text="Start Year:", icon="TIME")
			row.prop(obj,'["startyear"]', text="")
			row = col.row(align=True)
			row.label(text="End Year:", icon="TIME")
			row.prop(obj,'["endyear"]', text="")

			col = layout.column(align=True)
			row = col.row(align=True)
			row.operator('object.modif_properties', text = "Update Properties", icon="FILE_REFRESH")
			row = col.row(align=True)
			row.operator('object.del_properties', text = "Delete all Properties", icon="X")

			# check if object location is different from loc x var
			if obj.location[0] != obj["Loc x"]:
				col = layout.column(align=True)
				row = col.row(align=True)
				row.alert = True
				row.label(text="Location has changed, Update!", icon="ERROR")

			# check if object name is different from name var
			if obj.name != obj["name"]:
				col = layout.column(align=True)
				row = col.row(align=True)
				row.alert = True
				row.label(text="Name has changed, Update!", icon="ERROR")

			# check if object material is different from material var
			if obj.active_material.name != obj["material"]:
				col = layout.column(align=True)
				row = col.row(align=True)
				row.alert = True
				row.label(text="Material has changed, Update!", icon="ERROR")


		else:
			col = layout.column(align=True)
			box = col.box()
			colbox = box.column(align=True)
			rowcolbox = colbox.row(align=True)
			rowcolbox.alignment = 'CENTER'
			rowcolbox.alert = True
			rowcolbox.label(text="'Object has no properties", icon = "ERROR")
			col = layout.column(align=True)
			row = col.row(align=True)
			row.operator('object.edit_properties', text = "Add Properties")









