"""A set of classes for visually comparing secondary structure prediction"""
from fpdf import FPDF
class Colors():
	'''A class for dealing with selected colors'''
	global color_table
	def __init__(self, helix, coil, strand):
		self.h = helix
		self.c = coil
		self.e = strand

	def color_table(self):
		'''Reads the HTML color table and outputs list of lists'''
		fn = open('html_colors.txt')
		self.lines = fn.readlines()
		fn.close()

		self.lines = [line.split() for line in self.lines[1:]]
		return self.lines

	def get_colors(self):
		'''Gets the speficied colors from color_table'''
		list_of_colors, output = color_table(self), []
		for comp in [self.h, self.c, self.e]:
			for ele in list_of_colors:
				if comp == ele[3]:
					output.append(ele[:3])
					break
		return(output)


class Chart(Colors):
	'''A class for generating chart'''
	def __init__(self, struct_sequences, hct):
		self.struct_sequences = struct_sequences #the list of sequences
		self.hct = hct #output from get_colors or colors of helix, chain,turn

	global protein_seq
	global square_fill
	
	def protein_seq(self):
		'''returns the sequence of the protein'''
		return self.struct_sequences[0]

	def square_fill(self):
		'''determines what color each square should be and returns
			list of lists'''
		self.fill, mini = [],[]
		for struct_seq in self.struct_sequences[1:]:
			for seq in struct_seq:
				if seq == 'H':
					mini.append(self.hct[0])
				elif seq == 'C':
					mini.append(self.hct[1])
				elif seq == 'E':
					mini.append(self.hct[2])
			self.fill.append(mini)
			mini = []
		return self.fill

	def get_bits(self):
		length = len(protein_seq(self)) 
		if length > 150:
			fills = square_fill(self)
			self.bits, mini_fill = [], []

			while len(fills[-1]) > 150:
				k = 0
				while k < len(fills):
					mini_fill.append(fills[k][:150])
					fills[k] = fills[k][150:]
					k += 1
				k = 0
				self.bits.append(mini_fill)
				mini_fill= []

			mini_fill = []
			for element in fills:
				mini_fill.append(element)
			self.bits.append(mini_fill)
			
			return self.bits
	global get_chunks

	def get_chunks(self):
		target = self.struct_sequences[0]
		if len(target)>150:
			list_of_chunks = []
			while len(target) > 150:
				list_of_chunks.append(target[:150])
				target = target[150:]
			list_of_chunks.append(target)
		return list_of_chunks




	def build_chart(self, output_name, mins):
		length = len(protein_seq(self))
		chunks = Chart.get_bits(self)

		pdf = FPDF('L')
		pdf.add_page()


		height = (125/len(self.struct_sequences[1:]))/len(chunks[0][0][0])
		mult = height - 1
		for i in range(len(chunks)):
			for m in range(len(chunks[i])):
				for z in range(len(chunks[i][m])):
					r,g,b = float(chunks[i][m][z][0]), float(chunks[i][m][z][1]), float(chunks[i][m][z][2])
					pdf.set_fill_color(r,g,b)
					pdf.rect((z + (z*.9))+2,((m+(mult*m) +(i*60)+5)),1.9,height,style='F')
			pdf.line((0 + (0*.9))+2,(m+(mult*m) +(i*60)+5),(z + (z*.9))+3.9,(m+(mult*m) +(i*60)+5))
		pdf.set_font("Arial", style = 'B', size = 5.5)

		pieces = get_chunks(self)
		for Y in range(len(chunks)):
			for B in range(len(pieces[Y])):
				pdf.text((B + (B*.9))+2.2,((Y*60)+4.5),pieces[Y][B])

		option_list = ['Helix','Coil', 'Strand']
		for q in range(3):
			red = float(mins[q][0])
			green = float(mins[q][1])
			blue = float(mins[q][2])

			pdf.set_font("Arial", style = 'B', size = 18)
			
			pdf.set_fill_color(red, green, blue)
			pdf.rect(230,(q*7)+q+185, 15,7 , style = 'F')
			pdf.text(247,(q*7)+q+190,option_list[q])


		pdf.output(output_name)