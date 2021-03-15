import bpy
import bmesh
from mathutils import Vector, Matrix
from random import randint, uniform


BODY_SCALE_RANGE = (5, 5, 5)
HEAD_SCALE_RANGE = (2, 2, 2)
NUMBER_LEGS_RANGE = 4

USE_WINGS = True
NUMBER_WINGS_RANGE = 3

EPSILON_SCALE = 1


# Quelques raccourcis
context = bpy.context
scene = context.scene

# On crée un Objet de type Mesh
mesh = bpy.data.meshes.new("Thing")
creature = bpy.data.objects.new("Thing", mesh)

# On crée un Bmesh
blenderMesh = bmesh.new()

#Body Creation

scaleBody = (uniform(EPSILON_SCALE, BODY_SCALE_RANGE[0]), uniform(EPSILON_SCALE, BODY_SCALE_RANGE[1]), uniform(EPSILON_SCALE, BODY_SCALE_RANGE[2]))

bodyMatrix = Matrix.Scale(scaleBody[0], 4, (1, 0, 0)) @ Matrix.Scale(scaleBody[1], 4, (0, 1, 0)) @ Matrix.Scale(scaleBody[2], 4, (0, 0, 1))

bodyVerts = bmesh.ops.create_cube(blenderMesh, size=1, matrix=bodyMatrix, calc_uvs=False)


# Head creation
scaleHead = (uniform(EPSILON_SCALE, HEAD_SCALE_RANGE[0]), uniform(EPSILON_SCALE, HEAD_SCALE_RANGE[1]), uniform(EPSILON_SCALE, HEAD_SCALE_RANGE[2]))

headMatrix = Matrix.Scale(scaleHead[0], 4, (1, 0, 0)) @ Matrix.Scale(scaleHead[1], 4, (0, 1, 0)) @ Matrix.Scale(scaleHead[2], 4, (0, 0, 1))

y = (scaleBody[1] + scaleHead[1]) / 4
headMatrix = headMatrix @ Matrix.Translation((0, y, 0))

headVerts = bmesh.ops.create_cube(blenderMesh, size=1, matrix=headMatrix, calc_uvs=False)

'''

root = bm.verts.new()

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
            
'''
blenderMesh.to_mesh(mesh)

# placement de l'objet
creature.location = (0, 0, 0)

mirror = creature.modifiers.new(name="Symetry", type='MIRROR')
mirror.use_axis = (False, False, False)

# Modifier Skin
#skin = creature.modifiers.new(name="Skin", type='SKIN')

sub = creature.modifiers.new(name="Sub", type='SUBSURF')
sub.levels = 2
# Ajout de l'objet dans la scène
scene.collection.objects.link(creature)
