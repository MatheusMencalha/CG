from OpenGL.GL import *
 
def MTL(filename):
	contents = {}
	mtl = None
	for line in open(filename, "r"):
		if line.startswith('#'): continue
		values = line.split()
		if not values: continue
		if values[0] == 'newmtl':
			mtl = contents[values[1]] = {}
		elif mtl is None:
			raise ValueError("mtl file doesn't start with newmtl stmt")
		elif values[0] == 'map_Kd':
			pass
		else:
			mtl[values[0]] = list(map(float, values[1:]))
	return contents
 
class OBJ:
	def __init__(self, filename, swapyz=False):
		"""Loads a Wavefront OBJ file. """
		self.vertices = []
		self.normals = []
		self.texcoords = []
		self.faces = []

		qtd_vertices = 0
		qtd_faces = 0
		contador_vertices = 0 
		contador_faces = 0

		material = None
		for line in open(filename, "r"):
			if line.startswith('ply'): continue
			if line.startswith('format'): continue
			if line.startswith('comment'): continue
			if line.startswith('property'): continue
			if line.startswith('end_header'): continue             
			if line.startswith('element'):       
				 values = line.split()
				 if values[1] == 'vertex':
					 qtd_vertices = values[2]
					 print("QTD VERTICES-----"+ qtd_vertices)
					 continue
				 elif values[1] == 'face':
					 qtd_faces = values[2]
					 print("QTD FACES-----"+ qtd_faces)       
					 continue
			if contador_vertices < int(qtd_vertices):
				values = line.split()
				v = list(map(float, values[0:3]))
				self.vertices.append(v)
				contador_vertices += 1
				#print("VERTICES-----------", self.vertices)
				continue
			
			if contador_faces < int(qtd_faces):
				#print(contador_faces, line)
				values = line.split()
				self.faces.append(list(map(int, values[1:4])))
				#print("FACES-----------", self.faces)
				contador_faces += 1
				continue
				

		print (len(self.faces), len(self.vertices), contador_faces, contador_vertices)
		print (self.faces[0], self.faces[-1], self.vertices[0], self.vertices[-1])
		self.gl_list = glGenLists(1)
		glNewList(self.gl_list, GL_COMPILE)
		glFrontFace(GL_CCW)
		glBegin(GL_TRIANGLES)
		for vertices in self.faces:
			glColor3f(1.0,1.0,1.0)
			for i in range(len(vertices)):
				glVertex3fv(self.vertices[vertices[i]-1])
		glEnd()
		glDisable(GL_TEXTURE_2D)
		glEndList()


		# self.gl_list = glGenLists(1)
		# glNewList(self.gl_list, GL_COMPILE)
		# glFrontFace(GL_CCW)
		# glBegin(GL_POINTS)
		# for vertices in self.vertices:
		# 	glColor3f(1.0,1.0,1.0)
		# 	for i in range(len(self.vertices)):
		# 		glVertex3fv(self.vertices[i])
		# glEnd()
		# glDisable(GL_TEXTURE_2D)
		# glEndList()
