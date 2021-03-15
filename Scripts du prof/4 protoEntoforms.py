import bpy
import bmesh
from mathutils import Vector
from random import randint, uniform


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


newvert1 = bm.verts.new((2, 2, 2))
newedge = bm.edges.new([root, newvert1])
newvert2 = bm.verts.new((5, 2, 2))
newedge = bm.edges.new([newvert1, newvert2])

for i in range(5): # tree branches
    v = root
    for l in range(randint(1, 4)):
        ret = bmesh.ops.extrude_vert_indiv(bm, verts=[v])
        for v in ret['verts']:
            v.co += Vector([uniform(-1, 1) for axis in "xyz"])
        bm.to_mesh(me)

# placement de l'objet
ob.location = (0, 0, 0)
# Modifier Skin
skin = ob.modifiers.new(name="Skin", type='SKIN')
sub = ob.modifiers.new(name="Sub", type='SUBSURF')
sub.levels = 2
# Ajout de l'objet dans la scène
scene.collection.objects.link(ob)
