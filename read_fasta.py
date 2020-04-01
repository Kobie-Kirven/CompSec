def fasta(read_file):
	id_sequence = ''
	list_of_ids = []
	un_joined_sequences = []
	joined_sequence = ''
	joined_sequence_list = []

	for sequence in read_file:
		sequence = sequence.strip('\n')
		if sequence.startswith('>'):
			if id_sequence:
				id_sequence = sequence 
				list_of_ids.append(id_sequence)
				for un_joined_sequence in un_joined_sequences:
					joined_sequence = joined_sequence + un_joined_sequence 
				joined_sequence_list.append(joined_sequence)
				joined_sequence = ''
				un_joined_sequences = []

			else:
				id_sequence = sequence 
				list_of_ids.append(id_sequence)
		else:
			un_joined_sequences.append(sequence)

	if id_sequence:
		for un_joined_sequence in un_joined_sequences:
			joined_sequence = joined_sequence + un_joined_sequence 
		joined_sequence_list.append(joined_sequence)
	return joined_sequence_list