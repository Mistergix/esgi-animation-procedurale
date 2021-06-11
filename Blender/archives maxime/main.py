import bpy
import bmesh
from mathutils import Vector
import sys
from dataclasses import dataclass
from typing import List
import os


class BestioleDescriptor:
    def __init__(self, encoded_dna: str):
        encoded_dna_list = list(encoded_dna)
        self.leg_height: float = self.read(encoded_dna_list, 4, 0.0, 3.0)
        self.leg_phalanx_count: int = self.read(encoded_dna_list, 1, 2, 3)
        self.body_part_count: int = self.read(encoded_dna_list, 2, 1, 4)
        self.body_width: float = self.read(encoded_dna_list, 3, 0.1, 2.0)

    @staticmethod
    def read(binary: List[chr], bit_count: int, _min, _max):
        return BestioleDescriptor.convert_to_range(BestioleDescriptor.extract_n_bits(binary, bit_count), _min, _max)

    @staticmethod
    def convert_to_range(binary: str, _min, _max):
        assert (type(_min) == type(_max))
        _type: type = type(_min)
        v = int(binary, 2)
        a = 0
        b = pow(2, len(binary)) - 1
        A = _min
        B = _max
        return _type(A + (B - A) * (v - a) / (b - a))

    @staticmethod
    def extract_n_bits(binary: List[chr], n: int) -> str:
        extracted: str = "".join(binary[:n])
        binary[:] = binary[n:]
        return extracted


def grow_leg(bm: bmesh.types.BMesh, root: bmesh.types.BMVert, height: float, phalanx_count: int):
    v = root
    segment_length = height / phalanx_count

    for j in range(phalanx_count):
        res = bmesh.ops.extrude_vert_indiv(bm, verts=[v], use_select_history=False)

        v = res["verts"][0]
        v.co += Vector((1, 0, -segment_length))


def grow_bones(scene):
    armature = bpy.data.armatures.new("Armature")
    obj_amt = bpy.data.objects.new("Armature", armature)
    scene.collection.objects.link(obj_amt)
    bpy.ops.object.mode_set(mode='EDIT', toggle=False)
    edit_bones = obj_amt.data.edit_bones

    b = edit_bones.new('bone1')
    # a new bone will have zero length and not be kept
    # move the head/tail to keep the bone
    b.head = (1.0, 1.0, 0.0)
    b.tail = (1.0, 1.0, 1.0)

    b = edit_bones.new('bone2')
    b.head = (1.0, 2.0, 0.0)
    b.tail = (1.0, 2.0, 1.0)


def sub(l: Vector, r: Vector):
    return Vector((l.x - r.x, l.y - r.y, l.z - r.z))


def add(l: Vector, r: Vector):
    return Vector((l.x + r.x, l.y + r.y, l.z + r.z))


def negate(vec: Vector):
    vec.negate()
    return vec


def generate(encoded_dna: str):
    descriptor: BestioleDescriptor = BestioleDescriptor(encoded_dna)

    # Quelques raccourcis
    context = bpy.context
    scene = context.scene

    # On crée un Objet de type Mesh
    mesh = bpy.data.meshes.new("Thing")
    obj = bpy.data.objects.new("Thing", mesh)

    # placement de l'objet
    obj.location = (0, 0, 0)

    # Ajout de l'objet dans la scène
    scene.collection.objects.link(obj)
    bpy.context.view_layer.objects.active = obj

    # mesh.use_auto_smooth = True

    # On crée un Bmesh
    bm = bmesh.new()

    body_verts = list()
    pos_y = 0
    body_verts.append(bm.verts.new((0, pos_y, 0)))
    for i in range(descriptor.body_part_count):
        pos_y += 2
        body_verts.append(bm.verts.new((0, pos_y, 0)))
        bm.edges.new((body_verts[i], body_verts[i + 1]))

    for vert in body_verts:
        res = bmesh.ops.extrude_vert_indiv(bm, verts=[vert], use_select_history=False)
        v = res["verts"][0]
        v.co += Vector((descriptor.body_width + 0.1, 0, 0))

        grow_leg(bm, v, descriptor.leg_height, descriptor.leg_phalanx_count)

    bm.to_mesh(mesh)

    # Modifiers

    mirror = obj.modifiers.new(name="Mirror", type='MIRROR')

    skin = obj.modifiers.new(name="Skin", type='SKIN')
    skin.use_x_symmetry = False
    skin.use_smooth_shade = True

    for i in range(descriptor.body_part_count + 1):
        mesh.skin_vertices[0].data[i].radius[0] = descriptor.body_width
        mesh.skin_vertices[0].data[i].radius[1] = descriptor.body_width / 2

    sub_surf = obj.modifiers.new(name="SubSurf", type='SUBSURF')
    sub_surf.levels = 2

    bpy.ops.object.modifier_apply(modifier=mirror.name)
    bpy.ops.object.modifier_apply(modifier=skin.name)
    bpy.ops.object.modifier_apply(modifier=sub_surf.name)

    # armature

    blend_file_path = bpy.data.filepath
    directory = os.path.dirname(blend_file_path)
    target_file = os.path.join(directory, "output/" + encoded_dna + '.obj')

    bpy.ops.export_scene.obj(filepath=target_file, use_materials=False, use_triangles=True)


if True:
    bpy.ops.wm.read_factory_settings(use_empty=True)

    argv = sys.argv
    argv = argv[argv.index("--") + 1:]  # get all args after "--"
    generate(argv[0])
else:
    generate("0100001111")
# BestioleDescriptor("0100001111")
