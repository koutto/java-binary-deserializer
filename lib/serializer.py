import os
import platform
import ast
import struct
from lib import *
if 'java' in platform.system().lower():
	import java.io as io
	from com.thoughtworks.xstream import XStream


class Serializer(object):
	
	def __init__(self, filename):
		self.filename 	= filename.strip()
		self.length 	= os.stat(filename).st_size
		self.input  	= open(self.filename, 'r').read()
		self.output 	= ''


	def execute(self):
		"""
		Serialize input data into Java serialized data
		"""
		data = dict()
		try:
			data = ast.literal_eval(self.input)
		except Exception:
			PrintUtils.print_error('Input data is malformed')
			return False

		if not data:
			PrintUtils.print_error('Empty input data')
			return False

		#print data

		self.serializeData(data)
		if self.output:
			PrintUtils.print_success('Data serialized with success - length = {0} (0x{1:x}) bytes'.format(len(self.output), len(self.output)))
			print
			self.printSerializedData()
			return self.output
		else:
			PrintUtils.print_error('No data serialized')
			return ''


	def serializeData(self, data):
		"""
		Serialize data
		@Args 	data: 	The Java serialized data
		"""
		self.output = '\xAC\xED\x00\x05'

		for i in data.keys():
			# Object
			if data[i][0] == 'object':

				# Create XStream object and create Java object from the XML structure
				xs = XStream()
				serialized = xs.fromXML(data[i][1])

				# Serialize created object with ObjectOutputStream
				bos = io.ByteArrayOutputStream()
				oos = io.ObjectOutputStream(bos)
				oos.writeObject(serialized)

				self.output += bos.toByteArray()[4:]

			# TC_BLOCKDATA = (byte)0x77
			elif data[i][0] == 'block' and len(data[i][1]) <= 0xff:
				self.output += '\x77'
				self.output += struct.pack('<B', len(data[i][1])) # length on 1 byte
				self.output += data[i][1]

			# TC_BLOCKDATALONG = (byte)0x7A
			else:
				self.output += '\x7A'
				self.output += struct.pack('>I', len(data[i][1])) # length on 4 bytes (big endian)
				self.output += data[i][1]


	def printSerializedData(self):
		"""
		Print serialized data in the terminal
		"""
		if len(self.output) == 0:
			PrintUtils.print_error('No serialized data to print')
			return

		PrintUtils.print_delimiter()

		PrintUtils.hexdump(self.output)