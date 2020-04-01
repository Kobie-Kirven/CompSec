"""A class to get the concensus"""


class Concensus():

	def __init__(self, list_of_sequences):
		self.list_of_sequences = list_of_sequences

	def counts(self):
		concensus_seq = ''
		for z in range(len(self.list_of_sequences[1])):
			c = 0
			e = 0
			h = 0
			ele_list = []
			for i in range(len(self.list_of_sequences)):
				if self.list_of_sequences[i][z] == 'C':
					c += 1
				elif self.list_of_sequences[i][z] == 'E':
					e += 1
				elif self.list_of_sequences[i][z] == 'H':
					h += 1
			ele_list.append(c)
			ele_list.append(e)
			ele_list.append(h)
			major = [0,0]
			for m in range(len(ele_list)):
				if ele_list[m] > major[1]:
					major[1] = ele_list[m]
					major[0] = m
			if major[0] == 0:
				concensus_seq = concensus_seq + 'C'
			elif major[0] == 1:
				concensus_seq = concensus_seq + 'E'
			elif major[0] == 2:
				concensus_seq = concensus_seq + 'H'
		return concensus_seq


