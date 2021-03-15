import bpy
import os

filename = os.path.join(os.path.dirname(bpy.data.filepath), "python/main.py")
exec(compile(open(filename).read(), filename, 'exec'))