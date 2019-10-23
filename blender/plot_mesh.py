import bpy
import math

# Delete cube
#bpy.data.objects["Cube"].select = True
#bpy.ops.object.delete()

# mesh arrays
verts = []
faces = []

# mesh variables
numX = 5
numY = 30

# wave variables
freq = 0.5
amp = 1
a, b= -2, 2
scale = (b-a)/numX
zscale = 0.1*scale

#fill verts array
for i in range (0, numX):
    for j in range(0,numY):

        x = a + i*math.cos(scale * j)
        y = a + i*math.sin(scale * j)
        #z = scale*((amp*math.cos(i*freq))+(amp*math.sin(j*freq)))
        z = j*zscale

        vert = (x,y,z)
        verts.append(vert)

#fill faces array
count = 0
for i in range (0, numY *(numX-1)):
    if count < numY-1:
        A = i
        B = i+1
        C = (i+numY)+1
        D = (i+numY)

        face = (A,B,C,D)
        faces.append(face)
        count = count + 1
    else:
        count = 0

#create mesh and object
mesh = bpy.data.meshes.new("wave")
object = bpy.data.objects.new("wave", mesh)

#set mesh location
object.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(object)

#create mesh from python data
mesh.from_pydata(verts,[],faces)
mesh.update(calc_edges=True)

# create plane
bpy.ops.mesh.primitive_plane_add(location=(0,0,0))
plano = bpy.context.object
plano.dimensions = (20,20,0)

# Asignar un material (color) al plano
color, obj = (0.4,1,0.3),  plano
mat = bpy.data.materials.new("mat_" + str(obj.name))
mat.diffuse_color = color
obj.data.materials.append(mat)

# Asignar un material (color) a la malla
color, obj = (1, 0.2, 0.4), mesh
mat = bpy.data.materials.new("mat_" + str(obj.name))
mat.diffuse_color = color
obj.materials.append(mat)


v3d = bpy.ops.view3d
v3d.camera_to_view_selected()
