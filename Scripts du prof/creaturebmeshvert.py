import bpy
import bmesh
from mathutils import Vector
from random import randint, uniform

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False, confirm=False)

lengthpair=1
originallengthpair=lengthpair
pairnumber=1
lengthneck=1
lengthhead=1

# Quelques raccourcis
context = bpy.context
scene = context.scene

# On crée un Objet de type Mesh
me = bpy.data.meshes.new("Thing")
ob = bpy.data.objects.new("Thing", me)

# On crée un Bmesh
bm = bmesh.new()
root = bm.verts.new()

print(root)

#----------------------------------------------------------
#fonction pour faire une jambe
def newleg (depvert,lengthpair):
    newvert1 = bm.verts.new((lengthpair, 0, 0))
    newedge = bm.edges.new([depvert, newvert1])

    vertleg1 = bm.verts.new((lengthpair,1,2))
    newedge = bm.edges.new([newvert1, vertleg1])
    vertleg2 = bm.verts.new((lengthpair,1,-3))
    newedge = bm.edges.new([vertleg1, vertleg2])
    lengthpair+=1
    
    lastvert = bm.verts.new((lengthpair, 0, 0))
    newedge = bm.edges.new([newvert1, lastvert])
    lengthpair+=1
    
    return lengthpair, lastvert

#----------------------------------------------------------
#jambe initiale
newvert1 = bm.verts.new((lengthpair, 0, 0))
newedge = bm.edges.new([root, newvert1])

vertleg1 = bm.verts.new((1,1,2))
newedge = bm.edges.new([newvert1, vertleg1])
vertleg2 = bm.verts.new((1,1,-3))
newedge = bm.edges.new([vertleg1, vertleg2])
lengthpair+=1

lastvert = bm.verts.new((lengthpair, 0, 0))
newedge = bm.edges.new([newvert1, lastvert])
lengthpair+=1

lengthpair, lastvert = newleg(lastvert, lengthpair)
#----------------------------------------------------------
#tete
vertneck= bm.verts.new((lengthpair+lengthneck, 0,-1)) 
newedge = bm.edges.new([lastvert, vertneck])
lengthpair+=lengthneck
verthead =bm.verts.new((lengthpair+lengthhead, 0,2)) 
newedge = bm.edges.new([vertneck, verthead])

#----------------------------------------------------------
'''
newvert2 = bm.verts.new((5, 2, 2))
newedge = bm.edges.new([newvert1, newvert2])

v = root
for l in range(randint(1, 4)):
    ret = bmesh.ops.extrude_vert_indiv(bm, verts=[v])
    for v in ret['verts']:
        v.co += Vector([uniform(-1, 1) for axis in "xyz"])
'''

#----------------------------------------------------------        
bm.to_mesh(me)

# placement de l'objet
ob.location = (0, 0, 0)
# Modifier Skin
skin = ob.modifiers.new(name="Skin", type='SKIN')
sub = ob.modifiers.new(name="Sub", type='SUBSURF')
sub.levels = 1

# Ajout de l'objet dans la scène
scene.collection.objects.link(ob)

#----------------------------------------------------------
'''
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.modifier_add(type='MIRROR')
bpy.context.object.modifiers["Mirror"].use_axis[1] = True
'''