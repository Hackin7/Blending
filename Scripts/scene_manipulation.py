import bpy
import mathutils

### Scene ######################################################################
# retrieve all scenes
list_of_all_scenes = bpy.data.scenes
print(list_of_all_scenes)
for scene in list_of_all_scenes:
    print(scene.name)

# currently active scene
scene = bpy.context.scene
print(scene.name)

# Change Scene
bpy.context.window.scene = list_of_all_scenes[0]
scene = bpy.context.scene
print(scene.name)

### Objects ####################################################################
for object in scene.objects:
    print(object)

# Create the camera
scene = bpy.context.scene
cam_data = bpy.data.cameras.new('camera')
cam = bpy.data.objects.new('camera', cam_data)
bpy.context.collection.objects.link(cam)
scene.camera = cam

cam.location = mathutils.Vector((6, -3, 5))
cam.rotation_euler = mathutils.Euler((0.9, 0.0, 1.1))

scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = "./image.png"
bpy.ops.render.render(write_still = 1)
