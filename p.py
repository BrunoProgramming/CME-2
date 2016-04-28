import scanf as s
print ", ".join(["sent time", "received time", "delta","aggressor", "type", "SSN", "ISN", "bid depth", "bid quantity", "bid price", "ask depth", "ask quantity", "ask price"])
with open('mdp_book_builder_output_2m.log') as input_file:
	index_line = 0
	formated_str = ""
	for line in input_file:
		#clprint(line)
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
				print ", ".join([sent, recv, str(indx), "None", header, ssn, isn, '']),
			elif num_segments == 7:
				header1, header2, ssn, isn, sent, recv, indx = s.sscanf(line, "%s %s SSN:%s ISN:%s Sent:%s Received:%s (%d)")
				header = header1 + header2
				print ", ".join([sent, recv, str(indx), "None", header, ssn, isn, '']),
			
			elif num_segments == 15:
				header1, header2, header3, header4, ssn, isn, sent, recv, t1, t2, t3, t4, t5, t6, t7 = s.sscanf(line, "%s %s %s %s SSN:%s ISN:%s Sent:%s Received:%s %s %s %s %s %s %s %s")
				#indx = " ".join(line.split()[-7:])
				a = t7[:-1]
				b = t6[1:]
				c = "quantity:" + t3 + " price:" + t5 + " type:" + b + " " + a
				header = header1 + header2 + header3 + header4
				print ", ".join([sent, recv, "-1", c, header, ssn, isn, '']),

			elif num_segments == 13:
				header1, header2, ssn, isn, sent, recv, t1, t2, t3, t4, t5, t6, t7  = s.sscanf(line, "%s %s SSN:%s ISN:%s Sent:%s Received:%s %s %s %s %s %s %s %s")
				#indx = " ".join(line.split()[-7:])
				a = t7[:-1]
				b = t6[1:]
				c = "quantity:" + t3 + " price:" + t5 + " type:" + b + " " + a
				header = header1 + header2
				print ", ".join([sent, recv, "-1", c, header, ssn, isn, '']),			

			elif num_segments == 14:
				header1, header2, header3, header4, ssn, isn, sent, recv, t1, t2, t3, t4, t5, t6 = s.sscanf(line, "%s %s %s %s SSN:%s ISN:%s Sent:%s Received:%s %s %s %s %s %s %s")
				#indx = " ".join(line.split()[-6:])
				a = t6[:-1]
				b = a[1:]
				c = "quantity:" + t3 + " price:" + t5 + " type:" + b
				header = header1 + header2 + header3 + header4
				print ", ".join([sent, recv, "-1", c, header, ssn, isn, '']),

			elif num_segments == 12:
				header1, header2, ssn, isn, sent, recv, t1, t2, t3, t4, t5, t6 = s.sscanf(line, "%s %s SSN:%s ISN:%s Sent:%s Received:%s %s %s %s %s %s %s")
				#indx = " ".join(line.split()[-6:])
				a = t6[:-1]
				b = a[1:]
				c = "quantity:" + t3 + " price:" + t5 + " type:" + b
				header = header1 + header2
				print ", ".join([sent, recv, "-1", c, header, ssn, isn, '']),
			
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

