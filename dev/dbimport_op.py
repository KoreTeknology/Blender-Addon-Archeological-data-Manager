#---------------------------
# Title: File db_importer_ops.py
#---------------------------

import bpy, csv, struct
import datetime

from bpy.props import (StringProperty,
						BoolProperty,
						IntProperty,
						FloatProperty,
						FloatVectorProperty,
						EnumProperty,
						PointerProperty,
						)

from bpy.types import (Panel,
						Operator,
						Menu,
						UIList,
						AddonPreferences,
						PropertyGroup,
						)

from . dbimport_props import *

############################ 
# CLASS OPERATORS
############################ 

# OPERATOR to open csv file and import data
class SCENE_OT_Import_db(bpy.types.Operator):
	bl_idname = "scene.import_db"
	bl_label = "Import csv data from files"
	bl_description = "Import CSV database"

	def execute(self, context):
		scene = bpy.context.scene

		# create new collection "import"
		newcol = bpy.data.collections.new("Project Import")
		bpy.context.scene.collection.children.link(newcol)


		# Create groups if no exist >>> replace for collection
		# group = bpy.data.groups.new("Database Group")
		# group
		# group_empties = bpy.data.groups.new("Empty Group")
		# group_empties
		# group_texts = bpy.data.groups.new("Text Group")
		# group_texts

		# import data from db file
		with open( scene.dbimport_props.path_csv ) as csvfile:
			rdr = csv.reader( csvfile )
			for i, row in enumerate( rdr ):
				if i == 0: continue
				name, lon, lat, elev, type, shape, fs, fe = row[1:9] # columns data

				# check if object exist with same name
				if bpy.data.objects.get(name) is not None:
					self.report({'ERROR'}, "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
					self.report({'ERROR'}, "The object "+ name+" exist !!! Stop Loading...")
					continue
				else:
					self.report({'INFO'}, "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
					self.report({'INFO'}, "### The object "+ name+" don't exist, Start Loading...")
					#self.report({'INFO'}, "Initialize import for "+ name)

				# generate Empty object at x = lon and y = lat and z = elev 
				bpy.ops.object.empty_add( type='ARROWS', location = ( float(lon), float(lat), float(elev) ) )

				# select and customize new created empty object
				new_target = bpy.context.selected_objects[0]
				new_target.name = "" + name + ""
				bpy.ops.transform.resize(value=(0.3, 0.3, 0.3), constraint_axis=(False, False, False), orient_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1)

				#new_target.show_bounds = True
				#new_target.show_axis = True
				self.report({'INFO'}, "# New Empty added on DB location for: "+new_target.name)

				# assign to group
				#empty_grp = bpy.data.groups.get('Empty Group')
				#empty_grp.objects.link(new_target)    
				#empty_grp.name = "Empty Group"
				#self.report({'INFO'}, "# Empty "+new_target.name+" have been added to "+empty_grp.name)

				empty_object = new_target
				Row = row

				# add other data to empty
				OBlocation = new_target.location
				bpy.ops.object.text_add(location=OBlocation)

				bpy.ops.transform.translate(value=(0, 0, 0.7), constraint_axis=(False, False, False), orient_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1)
				bpy.ops.transform.resize(value=(0.05, 0.05, 0.05), constraint_axis=(False, False, False), orient_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1)
				bpy.context.active_object.rotation_mode = 'XYZ'
				bpy.context.active_object.rotation_euler = (1.5708,0,1.5708)
				bpy.context.active_object.rotation_euler[1] = 0
				#bpy.context.active_object.draw_type = 'WIRE'
				bpy.context.active_object.display_type = 'WIRE'


				bpy.ops.object.editmode_toggle()
				bpy.ops.font.delete()
				bpy.ops.font.text_insert(text="Object: "+Row[1])
				bpy.ops.transform.resize(value=(0.451466, 0.451466, 0.451466), constraint_axis=(False, False, False), orient_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1)
				bpy.ops.font.line_break()
				bpy.ops.font.text_insert(text="- Type: " + Row[5])
				bpy.ops.font.line_break()
				bpy.ops.font.text_insert(text="- Shape: " + Row[6])
				bpy.ops.font.line_break()
				bpy.ops.font.text_insert(text="- from: " + Row[7]+" to "+ Row[8]+" AD")
				bpy.ops.object.editmode_toggle()

				txt_target = bpy.context.selected_objects[0]

				txt_target.show_in_front = True
				#txt_target.show_x_ray = True
				#txt_target.show_bounds = True

				#text_grp = bpy.data.groups.get('Text Group')
				#text_grp.objects.link(txt_target) 

				# new variable : name of new created empty object
				tn = new_target.name
				#text_grp.name = "Text Group"

				#self.report({'INFO'}, "# New Text Object added on DB location for "+tn)
				#self.report({'INFO'}, "# Text Object "+new_target.name+" have been added to "+text_grp.name)

				link = False

				if scene.dbimport_props.link_switch:
					link = False
				else:
					link = True

				# load objects from library selected with db name column               
				with bpy.data.libraries.load(scene.dbimport_props.path_blend, link=link) as (data_from, data_to):
					data_to.objects = [name for name in data_from.objects if name.startswith(tn)]

				# load imported objects to the scene at empties location      
				for obj in data_to.objects:
					if obj is not None:
						newcol.objects.link(obj)
						#scene.objects.link(obj)

					obj.location = new_target.location 
					#obj.show_name = True  
					obj.show_axis = True  
					obj.show_texture_space = True
					obj.name =  "" + name + "-OBJ"

					# print imported object name
					on = obj.name

					self.report({'INFO'}, "# Object imported from library: "+ on)





					# # insert keyframes at data position frame/year
					# frm_start = int(fs)
					# frm_end = int(fe)
					# frm_pre = int(fs)-1
					# scn = bpy.context.scene

					# scn.frame_set(frm_pre)
					# obj.hide_viewport = True
					# obj.keyframe_insert(data_path="hide")
					# empty_object.keyframe_insert(data_path="hide")

					# scn.frame_set(frm_start)
					# obj.hide = False
					# obj.keyframe_insert(data_path="hide")
					# empty_object.keyframe_insert(data_path="hide")

					# scn.timeline_markers.new(obj.name, frame=frm_start)

					# scn.frame_set(frm_end)
					# obj.hide = True
					# obj.keyframe_insert(data_path="hide")
					# empty_object.keyframe_insert(data_path="hide")

					# self.report({'INFO'}, "# Object is added on frame "+ str(frm_start)+" and removed on frame "+ str(frm_end))

					# scn.frame_set(frm_start)

					# # add to group
					# # !!! works ONLY if group is created, a group is created within this loop
					# #grp = bpy.data.groups.get('Database Group')
					# #grp.objects.link(obj)                 

					# # deselect objects
					# #bpy.ops.object.select_all(action='TOGGLE')                   
					# bpy.ops.object.select_all(action='DESELECT') #deselect all object
					# obj.select = True
					# txt_target.select = True
					# new_target.select = True
					# bpy.context.scene.objects.active = new_target    #the active object will be the parent of all selected object
					# bpy.ops.object.parent_set()

					# bpy.ops.object.select_all(action='DESELECT')

					# #self.report({'INFO'}, "# Object is assign to group: "+grp.name)
					# self.report({'INFO'}, "### "+name+" loaded with success !")

		return {'FINISHED'}
