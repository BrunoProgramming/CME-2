import scanf as s
print ", ".join(["sent time", "received time", "delta or aggressor", "type", "SSN", "ISN", "depth", "volume", "price"])
with open('mdp_book_builder_output_2m.log') as input_file:
	index_line = 0
	formated_str = ""
	for line in input_file:
		if line == "\n":
			index_line = 1
			print ''
			continue

		if index_line == 0:
			pass
		elif index_line == 1: 
			#print(line)
			num_segments = len(line.split(" "))
			#print num_segments
			if num_segments == 9:
				header1, header2, header3, header4, ssn, isn, sent, recv, indx = s.sscanf(line, "%s %s %s %s SSN:%s ISN:%s Sent:%s Received:%s (%d)")
				header = header1 + header2 + header3 + header4
			elif num_segments == 7:
				header1, header2, ssn, isn, sent, recv, indx = s.sscanf(line, "%s %s SSN:%s ISN:%s Sent:%s Received:%s (%d)")
				header = header1 + header2
			elif num_segments == 15:
				header1, header2, header3, header4, ssn, isn, sent, recv, indx = s.sscanf(line, "%s %s %s %s SSN:%s ISN:%s Sent:%s Received:%s %s")
				indx = " ".join(line.split()[-7:])
				header = header1 + header2 + header3 + header4
			elif num_segments == 14:
				header1, header2, header3, header4, ssn, isn, sent, recv, indx = s.sscanf(line, "%s %s %s %s SSN:%s ISN:%s Sent:%s Received:%s %s")
				indx = " ".join(line.split()[-6:])
				header = header1 + header2 + header3 + header4
			elif num_segments == 13:
				header1, header2, ssn, isn, sent, recv, indx = s.sscanf(line, "%s %s SSN:%s ISN:%s Sent:%s Received:%s %s")
				indx = " ".join(line.split()[-7:])
				header = header1 + header2
			elif num_segments == 12:
				header1, header2, ssn, isn, sent, recv, indx = s.sscanf(line, "%s %s SSN:%s ISN:%s Sent:%s Received:%s %s")
				indx = " ".join(line.split()[-6:])
				header = header1 + header2
			print ", ".join([sent, recv, str(indx), header, ssn, isn, '']),
		else:
			#print line.split()
			elements = line.split()
			field1 = elements[1][:-1]
			field2 = elements[2]
			field3, field4 = elements[4].split('|')
			field5 = elements[6]
			field6 = elements[7][1:]
			if field1 != 'None' or field2 != 'None' or field3 != 'None' or field4 != 'None' or field5 != 'None' or field6 != 'None':
				print ", ".join([field1, field2, field3, field6, field5, field4, '']),
		index_line += 1

