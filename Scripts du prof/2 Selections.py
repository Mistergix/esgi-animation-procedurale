import bpy

bpy.ops.mesh.primitive_cube_add()

# Sélection d'un vertex
bpy.ops.object.mode_set(mode = 'OBJECT')
obj = bpy.context.active_object
bpy.ops.object.mode_set(mode = 'EDIT') 
bpy.ops.mesh.select_mode(type="VERT")
bpy.ops.mesh.select_all(action = 'DESELECT')
bpy.ops.object.mode_set(mode = 'OBJECT')
obj.data.vertices[0].select = True
bpy.ops.object.mode_set(mode = 'EDIT') 

# Sélection d'un edge
bpy.ops.object.mode_set(mode = 'OBJECT')
obj = bpy.context.active_object
bpy.ops.object.mode_set(mode = 'EDIT') 
bpy.ops.mesh.select_mode(type="EDGE")
bpy.ops.mesh.select_all(action = 'DESELECT')
bpy.ops.object.mode_set(mode = 'OBJECT')
obj.data.edges[0].select = True
bpy.ops.object.mode_set(mode = 'EDIT') 

bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 3),"orient_type":'NORMAL'})


# Sélection d'une face
bpy.ops.object.mode_set(mode = 'OBJECT')
obj = bpy.context.active_object
bpy.ops.object.mode_set(mode = 'EDIT') 
bpy.ops.mesh.select_mode(type="FACE")
bpy.ops.mesh.select_all(action = 'DESELECT')
bpy.ops.object.mode_set(mode = 'OBJECT')
obj.data.polygons[0].select = True
bpy.ops.object.mode_set(mode = 'EDIT') 

bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 2), "orient_type":'NORMAL'})
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(3, 0, 2)})