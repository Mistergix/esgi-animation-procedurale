import bpy



# Commandes de base à utiliser
# et à adapter dans votre code



# Création de l'armatures
bpy.ops.object.armature_add(enter_editmode=True, location=(0, 0, 0))
# Faire des extrude sur l'armature pour avoir des bones
bpy.ops.armature.extrude_move(TRANSFORM_OT_translate={​​"value":(-1, -1, 0)}​​)
# Faire des Ik : Inverse Kinematics (Cinématique Inverse)
# Passer ici en Pose Mode
bpy.ops.pose.constraint_add(type='IK')




# Après avoir sélectionner le perso + l'armature, faire le Skin (CTRL P)4
bpy.ops.object.parent_set(type='ARMATURE_AUTO')