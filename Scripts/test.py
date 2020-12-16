import bpy
from math import radians

# create cube
bpy.ops.mesh.primitive_cube_add() 
so = bpy.context.active_object

# rotate object
so.rotation_euler[0] += radians(45)

# Create modifier
mod_subsurf = so.modifiers.new("My Modifier", "SUBSURF")
#so.modifiers["My Modifier"].levels=3
mod_subsurf.levels = 3

bpy.ops.object.shade_smooth()

# Create displacement modifier
mod_displace = so.modifiers.new("d", "DISPLACE")

# Create new texture
new_tex = bpy.data.textures.new("t", "DISTORTED_NOISE")
new_tex.noise_scale = 2.0
mod_displace.texture = new_tex

# Create material
new_mat = bpy.data.materials.new(name="m")
so.data.materials.append(new_mat)

new_mat.use_nodes = True
nodes = new_mat.node_tree.nodes

material_output = nodes.get("Material Output")
node_emission = nodes.new(type="ShaderNodeEmission")

node_emission.inputs[0].default_value = (0.0, 0.3, 1.0, 1) # colour
node_emission.inputs[1].default_value = 500 # strength

links = new_mat.node_tree.links
new_link = links.new(node_emission.outputs[0], material_output.inputs[0])