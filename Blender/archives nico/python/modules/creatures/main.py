import bpy
import bmesh
from mathutils import Vector, Matrix
from random import randint, uniform

BODY_SCALE_RANGE = (5, 5, 5)
HEAD_SCALE_RANGE = (2, 2, 2)
NUMBER_LEGS_RANGE = 4

USE_LEGS = False
USE_SUBDIV = False

number_iterations = 4

EPSILON_SCALE = 1

# Quelques raccourcis
context = bpy.context
scene = context.scene


def create_mesh():
    # On crée un Objet de type Mesh
    mesh = bpy.data.meshes.new("Thing")
    creature = bpy.data.objects.new("Thing", mesh)

    # On crée un Bmesh
    blenderMesh = bmesh.new()

    farthestCubeHeadVerts = None
    longestHeadYScale = 0

    for i in range(number_iterations):
        # Body Creation

        scaleBody = (uniform(EPSILON_SCALE, BODY_SCALE_RANGE[0]), uniform(EPSILON_SCALE, BODY_SCALE_RANGE[1]),
                     uniform(EPSILON_SCALE, BODY_SCALE_RANGE[2]))

        bodyMatrix = Matrix.Scale(scaleBody[0], 4, (1, 0, 0)) @ Matrix.Scale(scaleBody[1], 4, (0, 1, 0)) @ Matrix.Scale(
            scaleBody[2], 4, (0, 0, 1))

        bodyVerts = bmesh.ops.create_cube(blenderMesh, size=1, matrix=bodyMatrix, calc_uvs=False)

    for i in range(number_iterations):
        # Head creation
        scaleHead = (uniform(EPSILON_SCALE, HEAD_SCALE_RANGE[0]), uniform(EPSILON_SCALE, HEAD_SCALE_RANGE[1]),
                     uniform(EPSILON_SCALE, HEAD_SCALE_RANGE[2]))

        headMatrix = Matrix.Scale(scaleHead[0], 4, (1, 0, 0)) @ Matrix.Scale(scaleHead[1], 4, (0, 1, 0)) @ Matrix.Scale(
            scaleHead[2], 4, (0, 0, 1))

        y = (scaleBody[1] + scaleHead[1]) / 4
        headMatrix = headMatrix @ Matrix.Translation((0, y, 0))

        headVerts = bmesh.ops.create_cube(blenderMesh, size=1, matrix=headMatrix, calc_uvs=False)

        if y > longestHeadYScale :
            farthestCubeHeadVerts = headVerts
            longestHeadYScale = y

    # Legs
    if USE_LEGS:
        numberLegs = randint(2, NUMBER_LEGS_RANGE)
        distanceBetweenLegs = scaleBody[1] / (numberLegs - 1)

        for i in range(numberLegs):
            x, y, z = -scaleBody[0] / 2 - 0.25, distanceBetweenLegs * i - scaleBody[1] / 2, 0
            print(x, y, z)
            legMatrix = Matrix.Translation((x, y, z))
            legVerts = bmesh.ops.create_cube(blenderMesh, size=1, matrix=legMatrix, calc_uvs=False)

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

    print(list(map(lambda x : x.co, farthestCubeHeadVerts["verts"])))

    bmesh.ops.subdivide_edges(blenderMesh, blenderMesh.edges.get())

    blenderMesh.to_mesh(mesh)

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.loopcut_slide(
        MESH_OT_loopcut={"number_cuts": 3, "smoothness": 0, "falloff": 'INVERSE_SQUARE', "object_index": 0,
                         "edge_index": 76, "mesh_select_mode_init": (False, False, True)},
        TRANSFORM_OT_edge_slide={"value": 0, "single_side": False, "use_even": False, "flipped": False,
                                 "use_clamp": True, "mirror": False, "snap": False, "snap_target": 'CLOSEST',
                                 "snap_point": (0, 0, 0), "snap_align": False, "snap_normal": (0, 0, 0),
                                 "correct_uv": True, "release_confirm": False, "use_accurate": False})

    # placement de l'objet
    creature.location = (0, 0, 0)

    mirror = creature.modifiers.new(name="Symetry", type='MIRROR')
    mirror.use_axis = (True, False, False)

    # Modifier Skin
    # skin = creature.modifiers.new(name="Skin", type='SKIN')

    if USE_SUBDIV :
        sub = creature.modifiers.new(name="Sub", type='SUBSURF')
        sub.levels = 2
    # Ajout de l'objet dans la scène
    scene.collection.objects.link(creature)


create_mesh()