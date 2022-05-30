import bpy

from bpy.types import Operator

class SCENE_OT_add_orthocam(bpy.types.Operator):
	"""Create a new Camera Object"""
	bl_idname = "scene.add_orthocam"
	bl_label = "Add Orthocam to scene"
	bl_options = {'REGISTER', 'UNDO'}
      
	def execute(self, context):

		bpy.ops.object.select_all(action='TOGGLE')

		bpy.ops.object.camera_add(enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0))

		oc = bpy.context.scene.orthocam_props.orthocam_name
		tvc = bpy.context.object
		tvc.name = oc
		tvc.data.name = oc
		tvc.data.type = 'ORTHO'

		bpy.context.view_layer.objects.active = bpy.data.objects[oc]

		bpy.ops.view3d.view_camera()

		bpy.context.scene.render.resolution_y = 2048
		bpy.context.scene.render.resolution_x = 2048
		bpy.context.scene.render.display_mode = 'WINDOW'
		bpy.context.scene.render.resolution_percentage = 100

		bpy.ops.transform.translate(value=(0, 0, 20), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True))
		bpy.ops.object.rotation_clear(clear_delta=False)

		bpy.ops.view3d.object_as_camera()

		self.report({'INFO'}, "> OrthoCam created")

		# selected object
		obj = bpy.context.selected_objects[0]
		# create new collection layer
		newcol = bpy.data.collections.new("Project Cameras")
		# add new collection to scene aka master collection
		bpy.context.scene.collection.children.link(newcol)
		# link object to new collection
		newcol.objects.link(obj)
		# unlink from master collection
		master_collection = bpy.data.collections['Collection']
		master_collection.objects.unlink(obj)

		self.report({'INFO'}, "> Collection created")

		return {'FINISHED'}
