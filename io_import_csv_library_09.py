# -*- coding: utf-8 -*-

'''
***** BEGIN BSD LICENSE BLOCK *****

--------------------------------------------------------------------------
CSV Library Importer v0.9 
--------------------------------------------------------------------------

Copyright (c) 2018 Uriel Deveaud All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
4. Neither the name of Uriel Deveaud nor the names of its contributors
   may be used to endorse or promote products derived from this software
   without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY URIEL DEVEAUD ``AS IS'' AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL HANS.P.G. BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
SUCH DAMAGE.

***** END BSD LICENCE BLOCK *****
'''


bl_info = {
    "name": "CSV Library Database Importer",
    "author": "Uriel Deveaud - Project B-HGIS-ADB3",
    "version": (0, 9, 1),
    "blender": (2, 7, 9),
    "location": "Properties space > Scene tab > CSV Library Database Importer",
    "description": "Append/Link library objects based on csv database",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Import-Export"}


############################ 
# IMPORT MODULES  
############################ 

import bpy, csv
 
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
                       UserPreferences,
                       )
                       
                             
    
############################ 
# GENERAL VARIABLES 
############################     
           
#def scene
#context = bpy.context
#scene = context.scene

# append, set to true to keep the link to the original file 
# or false to copy and create new object
# TODO toggle button ui
link = False


def link_switch(self, context):
    if self.link_switch:
        print("Import MODE as Append")
        link = False
    else:
        print("Import MODE as Link")
        link = True


############################ 
# OPERATORS 
############################ 

# OPERATOR to open csv file and import data
class SCENE_OT_ImportDataFromCSV(bpy.types.Operator):
    bl_idname = "scene.csv_data_import"
    bl_label = "Import csv data from files"
    bl_description = "Import CSV database"
       
    def execute(self, context):
        
        scene = bpy.context.scene
        
        group = bpy.data.groups.new("Database Group")
        group
        
        group_empties = bpy.data.groups.new("Empty Group")
        group_empties
        
        group_texts = bpy.data.groups.new("Text Group")
        group_texts
        
        
        # import data from db file
        with open( scene.my_tool.path ) as csvfile:
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
                bpy.ops.transform.resize(value=(0.3, 0.3, 0.3), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
                #new_target.show_bounds = True
                #new_target.show_axis = True
                self.report({'INFO'}, "# New Empty added on DB location for: "+new_target.name)
                
                
                empty_grp = bpy.data.groups.get('Empty Group')
                empty_grp.objects.link(new_target)    
                empty_grp.name = "Empty Group"
                self.report({'INFO'}, "# Empty "+new_target.name+" have been added to "+empty_grp.name)
                
                empty_object = new_target
                
                Row = row
                
                # add other data to empty
                OBlocation = new_target.location
                
                bpy.ops.object.text_add(location=OBlocation)
                
                bpy.ops.transform.translate(value=(0, 0, 0.7), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
                bpy.ops.transform.resize(value=(0.05, 0.05, 0.05), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
                bpy.context.active_object.rotation_mode = 'XYZ'
                bpy.context.active_object.rotation_euler = (1.5708,0,1.5708)
                bpy.context.active_object.rotation_euler[1] = 0
                bpy.context.active_object.draw_type = 'WIRE'

                
                bpy.ops.object.editmode_toggle()
                bpy.ops.font.delete()
                bpy.ops.font.text_insert(text="Object: "+Row[1])
                bpy.ops.transform.resize(value=(0.451466, 0.451466, 0.451466), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
                bpy.ops.font.line_break()
                bpy.ops.font.text_insert(text="- Type: " + Row[5])
                bpy.ops.font.line_break()
                bpy.ops.font.text_insert(text="- Shape: " + Row[6])
                bpy.ops.font.line_break()
                bpy.ops.font.text_insert(text="- from: " + Row[7]+" to "+ Row[8]+" AD")
                bpy.ops.object.editmode_toggle()
                
                txt_target = bpy.context.selected_objects[0]
                txt_target.show_x_ray = True
                txt_target.show_bounds = True

                text_grp = bpy.data.groups.get('Text Group')
                text_grp.objects.link(txt_target) 
                
                
                
                # new variable : name of new created empty object
                tn = new_target.name
                
                self.report({'INFO'}, "# New Text Object added on DB location for "+tn)
                
                
                text_grp.name = "Text Group"
                self.report({'INFO'}, "# Text Object "+new_target.name+" have been added to "+text_grp.name)
                
                
                # load objects from library selected with db name column               
                with bpy.data.libraries.load(scene.my_tool.path2, link=link) as (data_from, data_to):
                    data_to.objects = [name for name in data_from.objects if name.startswith(tn)]
                    

                # load imported objects to the scene at empties location      
                for obj in data_to.objects:
                    if obj is not None:
                        scene.objects.link(obj)
                    obj.location = new_target.location 
                    #obj.show_name = True  
                    obj.show_axis = True  
                    obj.show_texture_space = True
                    obj.name =  "" + name + "-OBJ"
                    
                    # print imported object name
                    on = obj.name
                    
                    self.report({'INFO'}, "# Object imported from library: "+ on)
                    
                    # insert keyframes at data position frame/year
                    frm_start = int(fs)
                    frm_end = int(fe)
                    frm_pre = int(fs)-1
                    scn = bpy.context.scene
                    
                    scn.frame_set(frm_pre)
                    obj.hide = True
                    obj.keyframe_insert(data_path="hide")
                    empty_object.keyframe_insert(data_path="hide")

                    scn.frame_set(frm_start)
                    obj.hide = False
                    obj.keyframe_insert(data_path="hide")
                    empty_object.keyframe_insert(data_path="hide")

                    scn.timeline_markers.new(obj.name, frame=frm_start)

                    scn.frame_set(frm_end)
                    obj.hide = True
                    obj.keyframe_insert(data_path="hide")
                    empty_object.keyframe_insert(data_path="hide")
                    
                    self.report({'INFO'}, "# Object is added on frame "+ str(frm_start)+" and removed on frame "+ str(frm_end))
                    
                    scn.frame_set(frm_start)
                    
                    # add to group
                    # !!! works ONLY if group is created, a group is created within this loop
                    grp = bpy.data.groups.get('Database Group')
                    grp.objects.link(obj)                 
                    
                    # deselect objects
                    #bpy.ops.object.select_all(action='TOGGLE')                   
                    bpy.ops.object.select_all(action='DESELECT') #deselect all object
                    obj.select = True
                    txt_target.select = True
                    new_target.select = True
                    bpy.context.scene.objects.active = new_target    #the active object will be the parent of all selected object
                    bpy.ops.object.parent_set()

                    bpy.ops.object.select_all(action='DESELECT')
                    
                    self.report({'INFO'}, "# Object is assign to group: "+grp.name)
                    self.report({'INFO'}, "### "+name+" loaded with success !")
                    #self.report({'INFO'}, "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    
        return {'FINISHED'}
 
# OPERATOR to print paths and scene name
class SCENE_OT_PrintFilePath(bpy.types.Operator):
    bl_idname = "scene.file_path_print"
    bl_label = "Print Paths Operator"
    bl_description = "Print in console"
        
    def execute(self, context):
        
        scene = bpy.context.scene
        #bpy.ops.wm.console_toggle()
        print ("-"*0)
        print ("SYS.CHECK Filepaths ...")
        print ("> CSV file Path: "+scene.my_tool.path)
        print ("> BLEND file Path: "+scene.my_tool.path2)
        print ("."*3)
        
        return {'FINISHED'}

# OPERATOR to print scene name and group name
class SCENE_OT_PrintSceneInfos(bpy.types.Operator):
    bl_idname = "scene.scene_infos_print"
    bl_label = "Print Scene infos Operator"
    bl_description = "Print in console"
    
    def execute(self, context):
        scene = bpy.context.scene
        
        group = bpy.data.groups.new("Database Group")
        group
        
        print ("-"*0)
        print ("SYS.CHECK Scene Infos ...")
        print ("> Scene name: "+scene.name)
        print ("> Group name: "+bpy.data.groups[0].name)
        print ("-"*3)
        #print (link)
        
        return {'FINISHED'}
    
    
# OPERATOR to open terminal
class SCENE_OT_OpenTerminal(bpy.types.Operator):
    bl_idname = "scene.console_open"
    bl_label = "Open Terminal Operator"
    bl_description = "open Terminal"
    
    def execute(self, context):
        bpy.ops.wm.console_toggle()
        print ("-"*50)
        print ("Terminal opened")

        return {'FINISHED'}
        

############################ 
# UI  
############################  
 
class SCENE_MT_units_length_presets(Menu):
    """Unit of measure for properties that use length values"""
    bl_label = "Unit Presets"
    preset_subdir = "units_length"
    preset_operator = "script.execute_preset"
    draw = Menu.draw_preset 


class MySettings(PropertyGroup):

    path = StringProperty(
        name="",
        description="Path to Directory",
        default="",
        maxlen=1024,
        subtype='FILE_PATH')
        
    path2 = StringProperty(
        name="",
        description="Path to Directory",
        default="",
        maxlen=1024,
        subtype='FILE_PATH')

 
class SCENE_PT_FilePathPrinter(bpy.types.Panel):

    bl_label = "CSV Library Importer 0.9"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "scene"    
    
    def draw(self, context):
        
        scene = bpy.context.scene
        lay = self.layout
        col1 = lay.column()
        
        ob_cols = []
        db_cols = []
        objects = bpy.data.objects
        
        
        # Buttons action
        lay = self.layout
        col = lay.column(align=True)
        #col.label(text="Importer") 

        row2 = col.row(align=True)
        row2.scale_y = 1.5
        row2.operator("scene.csv_data_import", icon="LOAD_FACTORY", text="Import Library")
               
        # add switch toggle for Append or link file
        link_text = ""

        if context.scene.link_switch:
            link_text = "Link from"
            link_icon = "LINK_BLEND"
            #link=True
        else:
            link_text = "Append from"
            link_icon = "APPEND_BLEND"
            #link=False
						
        row2.prop(context.scene, "link_switch", text=link_text, toggle=True, icon=link_icon)
        
        box = lay.box()
        col = box.column(align=True)
        col.label(text="Set Options before loading your data!", icon='QUESTION')
        
      
        
        # Directories
        lay = self.layout
        col1 = lay.column(align=True)
        row2 = col1.row(align=True)
        row2.label("Directories:")

        box = lay.box()
        col = box.column(align=True)
        col.label("Database Path (.csv):",icon='RNA_ADD')
        col.prop(scene.my_tool, "path", text="")
        col.label("Objects Library Path (.blend):",icon='LINK_BLEND')
        col.prop(scene.my_tool, "path2", text="")
        col.label(text="Help: Works always with absolute path!", icon='QUESTION')
        


        # Setup section
        lay = self.layout
        col = lay.column(align=True)
        col.label(text="Preferences and Setup:") 
        
        lay = self.layout
        #optional settings
        box = lay.box()
        col1 = box.column(align=True)
        row2 = col1.row(align=True)
        
        if scene.show_options_timeline:
            row2.prop(scene, "show_options_timeline", icon="DOWNARROW_HLT", text="", emboss=False)
        else:
            row2.prop(scene, "show_options_timeline", icon="RIGHTARROW", text="", emboss=False)

        row2.label('Timeline Options', icon="PREVIEW_RANGE")
        
        if scene.show_options_timeline:
            row2 = col1.row(align=True)
            row2.label('Time range', icon="ACTION_TWEAK")
            row2 = col1.row(align=True)
            split = col1.split(percentage=0.5)
            split.prop(scene, 'frame_start', text='Start Year')
            split.prop(scene, 'frame_end', text='End Year')
            
            userpref = context.user_preferences
            edit = userpref.edit
            
            col1.separator()
            row2 = col1.row(align=True)
            row2.prop(edit, "use_negative_frames", text="Use Negative values")

        '''
        # optional geo
        lay = self.layout
        box = lay.box()
        col1 = box.column(align=True)
        row2 = col1.row(align=True)
        
        if scene.show_options_geo:
            row2.prop(scene, "show_options_geo", icon="DOWNARROW_HLT", text="", emboss=False)
            # icon can be TRIA_DOWN
        else:
            row2.prop(scene, "show_options_geo", icon="RIGHTARROW", text="", emboss=False)

        row2.label('Geo Options', icon="LINK_BLEND")
        
        if scene.show_options_geo:
            col1 = box.column(align=True)
            row2 = col1.row(align=True)
            row2.label(text="Length:", icon='SNAP_GRID')
            row2.menu("SCENE_MT_units_length_presets", text=SCENE_MT_units_length_presets.bl_label)
            
            #SNAP_INCREMENT
            unit = context.scene.unit_settings
            scenename = bpy.data.scenes

            split = box.split(percentage=0.5)
            split.label("Unit system:")
            split.prop(unit, "system", text="")

            col1 = box.column()
            col1.enabled = unit.system != 'NONE'
            split = col1.split(percentage=0.5)
            split.label("Scale Adjust:", icon='SNAP_INCREMENT')
            split.prop(unit, "scale_length", text="")
            split = col1.split(percentage=0.5)
            split.row()
            split.prop(unit, "use_separate")
        '''
            

        '''
        #optional import
        lay = self.layout
        box = lay.box()
        col1 = box.column(align=True)
        row2 = col1.row(align=True)
        
        if scene.show_options_import:
            row2.prop(scene, "show_options_import", icon="DOWNARROW_HLT", text="", emboss=False)
        else:
            row2.prop(scene, "show_options_import", icon="RIGHTARROW", text="", emboss=False)

        row2.label('Import Options', icon="IMPORT")
        unit = context.scene.unit_settings
        scenename = bpy.data.scenes
        
        if scene.show_options_import:
            row2 = col1.row(align=True)
            col1 = row2.column(align=True)
            split = col1.split(percentage=0.5)
            split.prop(unit, "use_separate", text="Import Objects")
            split.prop(unit, "use_separate", text="Import Text")
            split = col1.split(percentage=0.5)
            split.prop(unit, "use_separate", text="Import Material")
            split.prop(unit, "use_separate", text="Import Group")     
            #col.separator()
            split = col1.split(percentage=0.5)
            split.prop(unit, "use_separate", text="Add Axis")
            split.prop(unit, "use_separate", text="Add BoundBox")
        '''
        
        lay = self.layout
        #optional settings
        box = lay.box()
        col1 = box.column(align=True)
        row2 = col1.row(align=True)
        
        if scene.show_options_terminal:
            row2.prop(scene, "show_options_terminal", icon="DOWNARROW_HLT", text="", emboss=False)
        else:
            row2.prop(scene, "show_options_terminal", icon="RIGHTARROW", text="", emboss=False)

        row2.label('Console Log', icon="CONSOLE")
        
        if scene.show_options_terminal:
            row2 = col1.row(align=True)
            row2.operator("scene.console_open", text="Open Terminal")
            row2 = col1.row(align=True)
            row2.scale_y = 1
            row2.operator("scene.file_path_print", text="Path Infos")
            row2.operator("scene.scene_infos_print", text="Scene Infos")
            
            row3 = col1.row(align=True)
            row3.enabled = False
            row3.operator("scene.csv_data_import", text="DB Infos")
           

        #optional infos
        lay = self.layout
        box = lay.box()
        col1 = box.column(align=True)
        row2 = col1.row(align=True)
        
        if scene.show_options_infos:
            row2.prop(scene, "show_options_infos", icon="DOWNARROW_HLT", text="", emboss=False)
        else:
            row2.prop(scene, "show_options_infos", icon="RIGHTARROW", text="", emboss=False)

        row2.label('Infos Options', icon="INFO")
        
        if scene.show_options_infos:
            col1.label(text="Select Append/Link, and load your dataset!", icon='HELP')
 
            
############################ 
# REGISTER 
############################ 
                      
def register():
    bpy.utils.register_module(__name__)
    bpy.types.Scene.my_tool = PointerProperty(type=MySettings)
    
    bpy.types.Scene.show_options_geo = bpy.props.BoolProperty(name='Show Geo panel', default=False)
    bpy.types.Scene.show_options_terminal = bpy.props.BoolProperty(name='Show Terminal panel', default=False)
    bpy.types.Scene.show_options_import = bpy.props.BoolProperty(name='Show Import panel', default=False)
    bpy.types.Scene.show_options_timeline = bpy.props.BoolProperty(name='Show Timeline panel', default=False)
    bpy.types.Scene.show_options_infos = bpy.props.BoolProperty(name='Show Infos panel', default=False)
    bpy.types.Scene.link_switch = bpy.props.BoolProperty(update = link_switch, default = False)
    #bpy.types.Scene.theChosenObject = bpy.props.StringProperty()
        
def unregister():
    bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.my_tool
    del bpy.types.Scene.show_options_geo
    del bpy.types.Scene.show_options_terminal
    del bpy.types.Scene.show_options_import
    del bpy.types.Scene.show_options_timeline
    del bpy.types.Scene.show_options_infos
    #del bpy.types.Object.theChosenObject

if __name__ == '__main__':
    register()
    
   