#---------------------------------------------
# Title: chronodesign_op.py
# Author: Uriel Deveaud @2019
#---------------------------------------------

# ########################### 
# IMPORT MODULES  
# ########################### 
import bpy, os, sys, struct
from bpy.types import Operator
from bpy.types import Sequences

from . chronodesign_props import *

# ########################### 
# OPERATORS
# ########################### 

class SEQWIN_OT_open(bpy.types.Operator):
	"""Open the sequence window"""
	bl_idname = "seqwin.open"
	bl_label = "Open Sequencer"
	bl_options = {'INTERNAL'}

	def execute(self, context):
		bpy.ops.screen.userpref_show('INVOKE_DEFAULT') 
		area = bpy.context.window_manager.windows[-1].screen.areas[0] 
		area.type = 'SEQUENCE_EDITOR' 

		return {'FINISHED'}

# TEST
class SEQWIN_OT_Create_chrono(bpy.types.Operator):
	"""Create chronology sequences"""
	bl_idname = "seqwin.createchrono"
	bl_label = "Create chronology"
	#bl_options = {'INTERNAL'}

	def execute(self, context):
		p1_name = "Phase 1"
		p1_start = 10
		p1_end = 100
		p1_channel = 1
		p1_color = (1, 0, 0)
		scene = bpy.context.scene
		scene.timeline_markers.new("Phase 1", frame=p1_start)

		context = bpy.context
		scene = context.scene
		sed = scene.sequence_editor
		sequences = sed.sequences

		phase1 = sequences.new_effect("Color", 'COLOR', p1_channel,frame_start=p1_start, frame_end=p1_end)
		phase1.color = p1_color
		phase1.name = p1_name

		p2_name = "Phase 2"
		p2_start = 100
		p2_end = 200
		p2_channel = 2
		scene.timeline_markers.new("Phase 2", frame=p2_start)
		phase1 = sequences.new_effect("Color", 'COLOR', p2_channel,frame_start=p2_start, frame_end=p2_end)
		phase1.color = (0, 1, 0)
		phase1.name = p2_name

		p3_name = "Phase 3"
		p3_start = 120
		p3_end = 280
		p3_channel = 3
		scene.timeline_markers.new("Phase 3", frame=p3_start)
		phase3 = sequences.new_effect("Color", 'COLOR', p3_channel,frame_start=p3_start, frame_end=p3_end)
		phase3.color = (0, 0, 1)
		phase3.name = p3_name

		bpy.ops.markerlist.refresh()

		return {'FINISHED'}

# refresh marker list button
class Markerlist_refresh(bpy.types.Operator):
    bl_idname = "markerlist.refresh"
    bl_label = "Refresh Markers"
    bl_description = "Refresh Markers and Apply Names to Timeline"
        
    def execute(self, context):
        scene=bpy.context.scene
        mlist=scene.markerlist
        framelist=[]
        Oframelist=[]
        Ocommentlist=[]
        for nm in mlist:
            for m in scene.timeline_markers:
                if nm.frame==m.frame:
                    m.name=nm.name
                elif nm.name==m.name:
                    nm.frame=m.frame
            Oframelist.append(nm.frame)
            Ocommentlist.append(nm.comment)
        for i in range(len(mlist)-1,-1,-1):
                mlist.remove(i)
        for m in scene.timeline_markers:
            framelist.append(m.frame)
        framelist.sort()
        for fm in framelist:
            newmarker=mlist.add()
            newmarker.frame=fm
        for nm in mlist:
            for m in scene.timeline_markers:
                if nm.frame==m.frame:
                    nm.name=m.name
            for of in Oframelist:
                if nm.frame==of:
                    indx=Oframelist.index(of)
                    nm.comment=Ocommentlist[indx]
        info = 'Markers List refreshed'
        self.report({'INFO'}, info)
        
        return {'FINISHED'} 

# add marker button
class Markerlist_add(bpy.types.Operator):
	bl_idname = "markerlist.add_marker"
	bl_label = "Add Marker"
	bl_description = "Add Marker for Current Frame"

	def execute(self, context):
		scene=bpy.context.scene
		mlist=scene.markerlist
		framelist=[]
		check=0

		for nm in scene.timeline_markers:
			nm.select=False
			if nm.frame==scene.frame_current:
				info = 'Markers already exists'
				self.report({'ERROR'}, info)
				check=1
		if check==0:
			Ocontext=bpy.context.area.type
			bpy.context.area.type='SEQUENCE_EDITOR'
			bpy.ops.marker.add()
			bpy.context.area.type=Ocontext
			bpy.ops.markerlist.refresh()
			for nm in scene.timeline_markers:
				if nm.select==True:
					Nmarker=nm
			for m in mlist:
				framelist.append(m.frame)
			for f in framelist:
				if f==Nmarker.frame:
					scene.marker_index=framelist.index(f)

			bpy.ops.markerlist.refresh()

			info = 'Marker created'
			self.report({'INFO'}, info)

		return {'FINISHED'} 

# delete marker button
class Markerlist_delete(bpy.types.Operator):
	bl_idname = "markerlist.delete_marker"
	bl_label = "Delete Marker"
	bl_description = "Delete selected Marker"
        
	def execute(self, context):
		scene=bpy.context.scene
		idx=scene.marker_index
		mlist = scene.markerlist
		tlmlist = scene.timeline_markers
		if (idx+1) > len(mlist):
			info = 'Please select a marker'
			self.report({'ERROR'}, info)
		else :
			of = mlist[bpy.context.scene.marker_index].frame
			bpy.ops.markerlist.refresh()
			if (idx+1) > len(mlist):
				info = 'Marker no longer exists'
				self.report({'ERROR'}, info)
			else:
				nf = mlist[bpy.context.scene.marker_index].frame
				if of==nf:
					if len(bpy.context.scene.timeline_markers) > 0:
						for m in bpy.context.scene.timeline_markers:
							m.select=False
						for m in bpy.context.scene.timeline_markers:
							if m.frame==bpy.context.scene.markerlist[bpy.context.scene.marker_index].frame:
								m.select=True
						info = 'Marker removed'
						Ocontext=bpy.context.area.type
						bpy.context.area.type='SEQUENCE_EDITOR'
						Nmarker=bpy.ops.marker.delete()
						bpy.context.area.type=Ocontext
						self.report({'INFO'}, info)
						bpy.ops.markerlist.refresh()
				else:
					info = 'Marker no longer exists'
					self.report({'ERROR'}, info)

		bpy.ops.markerlist.refresh()

		return {'FINISHED'} 


# select button
class Markerlist_select(bpy.types.Operator):
	bl_idname = "markerlist.select_marker"
	bl_label = "Select Marker"
	bl_description = "Select Marker on Timeline"

	def execute(self, context):
		scene=bpy.context.scene
		idx=scene.marker_index
		mlist = scene.markerlist
		tlmlist = scene.timeline_markers
		if (idx+1) > len(mlist):
			info = 'Please select a marker'
			self.report({'ERROR'}, info)
		else :
			of = mlist[bpy.context.scene.marker_index].frame
			bpy.ops.markerlist.refresh()
			if (idx+1) > len(mlist):
				info = 'Marker no longer exists'
				self.report({'ERROR'}, info)
			else:
				nf = mlist[bpy.context.scene.marker_index].frame
				if of==nf:
					for m in bpy.context.scene.timeline_markers:
						m.select=False
					lmarker = bpy.context.scene.markerlist[bpy.context.scene.marker_index]
					for m in bpy.context.scene.timeline_markers:
						if m.frame==lmarker.frame:
							m.select=True
				else:
					info = 'Marker no longer exists'
					self.report({'ERROR'}, info)

		return {'FINISHED'} 


# jumpto button
class Markerlist_jumpto(bpy.types.Operator):
	bl_idname = "markerlist.jump_to"
	bl_label = "Jump to Marker"
	bl_description = "Jump to selected Marker"

	def execute(self, context):
		scene=bpy.context.scene
		idx=scene.marker_index
		mlist = scene.markerlist
		tlmlist = scene.timeline_markers
		if (idx+1) > len(mlist):
			info = 'Please select a marker'
			self.report({'ERROR'}, info)
		else :
			of = mlist[bpy.context.scene.marker_index].frame
			bpy.ops.markerlist.refresh()
			if (idx+1) > len(mlist):
				info = 'Marker no longer exists'
				self.report({'ERROR'}, info)
			else:
				nf = mlist[bpy.context.scene.marker_index].frame
				if of==nf:
					newF = mlist[bpy.context.scene.marker_index].frame
					scene.frame_current=newF
					for m in tlmlist :
						m.select=False
						if m.frame==newF:
							m.select=True
				else:
					info = 'Marker no longer exists'
					self.report({'ERROR'}, info)

		return{'FINISHED'}

# Go to previous marker
class Markerlist_Gotoprevious(bpy.types.Operator):
	bl_idname = "markerlist.goto_previous"
	bl_label = "Go to Previous Marker"
	bl_description = "Go to Previous Marker"

	def execute(self, context):
		scene=bpy.context.scene
		tlmlist=scene.timeline_markers
		mlist=scene.markerlist
		cframe=scene.frame_current
		framelist=[]
		lowerframelist=[]
		bpy.ops.markerlist.refresh()
		for m in tlmlist:
			m.select=False
		for m in mlist:
			framelist.append(m.frame)
			if m.frame < cframe:
				lowerframelist.append(m.frame)
		lowerframelist.sort(reverse=True)
		if len(lowerframelist)==0:
			ncframe=cframe
		else:
			scene.frame_current=lowerframelist[0]
			ncframe=scene.frame_current
		for m in tlmlist:
			if m.frame==ncframe:
				m.select=True
		for f in framelist:
			if f==ncframe:
				scene.marker_index=framelist.index(f)

		return {'FINISHED'}

# Go to next marker
class Markerlist_Gotonext(bpy.types.Operator):
	bl_idname = "markerlist.goto_next"
	bl_label = "Go to Next Marker"
	bl_description = "Go to Next Marker"

	def execute(self, context):
		scene=bpy.context.scene
		tlmlist=scene.timeline_markers
		mlist=scene.markerlist
		cframe=scene.frame_current
		framelist=[]
		upperframelist=[]
		bpy.ops.markerlist.refresh()
		for m in tlmlist:
			m.select=False
		for m in mlist:
			framelist.append(m.frame)
			if m.frame > cframe:
				upperframelist.append(m.frame)
		if len(upperframelist)==0:
			ncframe=cframe
		else:
			scene.frame_current=upperframelist[0]
			ncframe=scene.frame_current
		for m in tlmlist:
			if m.frame==ncframe:
				m.select=True
		for f in framelist:
			if f==ncframe:
				scene.marker_index=framelist.index(f)

		return {'FINISHED'} 


class AddChronologyOperator(bpy.types.Operator):
	"""Add chronology sequences"""
	bl_idname = "seq.addchrono"
	bl_label = "Add chronology"
	#bl_options = {'INTERNAL'}

	def execute(self, context):

		context = bpy.context
		scn = context.scene

		p1_name = scn.chronodesign_props.chrono_name
		p1_start = scn.chronodesign_props.chrono_start
		p1_end = scn.chronodesign_props.chrono_end
		p1_channel = scn.chronodesign_props.chrono_channel
		p1_color = scn.chronodesign_props.chrono_color
		#scene = bpy.context.scene
		scn.timeline_markers.new("Phase", frame=scn.chronodesign_props.chrono_start)

		seq = bpy.context.scene.sequence_editor_create()
		cstrip = seq.sequences.new_effect("Color", 'COLOR', p1_channel,frame_start=p1_start, frame_end=p1_end)
		cstrip.color = scn.chronodesign_props.chrono_color
		cstrip.name = scn.chronodesign_props.chrono_name

		return {'FINISHED'}

