import os
import platform
from lib import *
if 'java' in platform.system().lower():
	import java.io as io
	from com.thoughtworks.xstream import XStream


class Deserializer(object):

	def __init__(self, filename, begin_offset=0):
		self.filename = filename.strip()
		self.length = os.stat(filename).st_size
		self.begin_offset = begin_offset
		self.input  = open(self.filename, 'r').read()[self.begin_offset:]
		self.output = {}


	def execute(self):
		"""
		Scan input (file) for Java Serialized data to deserialize.
		"""
		# Java Serialized stream begins with:
		# AC ED: STREAM_MAGIC
		# 00 05: STREAM_VERSION
		header = self.input.find('\xAC\xED\x00\x05')
		if header >= 0:
			PrintUtils.print_success('Java Serialized data header found at offset 0x{0:x}'.format(header))
			print
			self.deserializeStream(self.input)
			self.printDeserializedData()
			return self.output
		else:
			PrintUtils.print_error('Unable to find Java Serialized data into input')
			return False


	def deserializeStream(self, data):
		"""
		Deserialize stream.
		@Args 	data: 	The Java serialized data
		"""
		bis = io.ByteArrayInputStream(data)
		ois = io.ObjectInputStream(bis)
		i = 0

		while True:
			# Block raw data ?
			block_data = []
			try:
				while True:
					byte = BinaryUtils.tohex(ois.readByte())
					raw_byte = chr(int(byte, 16))
					block_data.append(raw_byte)
			except:
				if len(block_data) > 0:
					#print 'Block data detected - length = {0}:'.format(len(block_data))
					self.output[i] = ('block', ''.join(block_data))
					i += 1
					print

			# Object ?
			try:
				obj = ois.readObject()

				# converting Java object to XML structure
				xs = XStream()
				xml = xs.toXML(obj)
				#self.output += xml + '\n'
				self.output[i] = ('object', xml)
				i += 1
				continue				
			except:
				pass

			# if we arrive here, it means there is nothing more
			break


	def printDeserializedData(self):
		"""
		Print deserialized data in the terminal
		"""
		if len(self.output) == 0:
			PrintUtils.print_error('No deserialized data to print')
			return

		PrintUtils.print_delimiter()
		for i in range(len(self.output)):
			if self.output[i][0] == 'block':
				length = len(self.output[i][1])
				PrintUtils.print_info('[0x{0:02x}] Block raw data - length = {1} (0x{2:02x}) bytes:'.format(i, length, length))
				PrintUtils.hexdump(self.output[i][1])
				#print self.output[i][1]
			elif self.output[i][0] == 'object':
				PrintUtils.print_info('[0x{0:02x}] Java Object (converted into XML):'.format(i))
				PrintUtils.print_xml_highlighted(self.output[i][1])
			else:
				continue
			PrintUtils.print_delimiter()

		return



