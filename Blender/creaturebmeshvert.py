import bpy
import bmesh
from mathutils import Vector
from random import randint, uniform
import sys
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

print(argv)  # --> ['example', 'args', '123']


bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False, confirm=False)

lengthpair=float(argv[0])
pairnumber=1
disthead=float(argv[5])
lengthneckx=float(argv[6])
lengthnecky=float(argv[7])
lengthheadx=float(argv[8])
lengthheady=float(argv[9])
lengthlegx=float(argv[3])
lengthlegy=float(argv[4])
lengthkneex=float(argv[1])
lengthkneey=float(argv[2])
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

    vertleg1 = bm.verts.new((lengthpair,lengthkneex,lengthkneey))
    newedge = bm.edges.new([newvert1, vertleg1])
    vertleg2 = bm.verts.new((lengthpair,lengthkneex,lengthkneey))
    newedge = bm.edges.new([vertleg1, vertleg2])
    lengthpair+=lengthpair
    
    lastvert = bm.verts.new((lengthpair, 0, 0))
    newedge = bm.edges.new([newvert1, lastvert])
    lengthpair+=lengthpair
    
    return lengthpair, lastvert

#----------------------------------------------------------
#jambe initiale
newvert1 = bm.verts.new((lengthpair, 0, 0))
newedge = bm.edges.new([root, newvert1])

vertleg1 = bm.verts.new((1,lengthkneex,lengthkneey))
newedge = bm.edges.new([newvert1, vertleg1])
vertleg2 = bm.verts.new((1,lengthlegx,lengthlegy))
newedge = bm.edges.new([vertleg1, vertleg2])
lengthpair+=lengthpair

lastvert = bm.verts.new((lengthpair, 0, 0))
newedge = bm.edges.new([newvert1, lastvert])
lengthpair+=lengthpair

for i in range(pairnumber-1):
    lengthpair, lastvert = newleg(lastvert, lengthpair)
#----------------------------------------------------------
#tete
distneck= bm.verts.new((lengthpair+disthead, 0,-1)) 
newedge = bm.edges.new([lastvert, distneck])
lengthpair+=disthead

vertneck=bm.verts.new((lengthpair+lengthneckx, 0,lengthnecky)) 
newedge = bm.edges.new([distneck, vertneck])
lengthpair=lengthpair+lengthneckx

verthead =bm.verts.new((lengthpair+lengthheadx, 0,lengthheady)) 
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
bpy.data.objects['Thing.005'].select_set(True)
bpy.ops.object.modifier_add(type='MIRROR')
bpy.context.object.modifiers["Mirror"].use_axis[1] = True
'''

bpy.ops.export_scene.obj(filepath=argv[10])