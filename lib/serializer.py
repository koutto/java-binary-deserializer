# -*- coding: utf-8 -*-
import os
import platform
import struct
from lib import *
if 'java' in platform.system().lower():
    import java.io as io
    from com.thoughtworks.xstream import XStream


class Serializer(object):
    
    def __init__(self, input_):
        """
        :param input_: Data that must be serialized
        Must be a list of tuples (type, data) where:
            - type can be:
                - object: for deserialized Java object
                - block: raw data corresponding to primitive types (boolean, byte, char...)
            - data is XML structure of Java Object when type = object, otherwise the raw data
        """
        self.input = input_
        self.output = ''


    def execute(self):
        """
        Serialize input data into Java serialized data
        :return: Serialized data raw bytes
        """
        print self.input

        self.serializeData()
        if self.output:
            PrintUtils.print_success('Data serialized with success - length = {length} (0x{length:x}) bytes'.format(length=len(self.output)))
            print
            self.printSerializedData()
        else:
            PrintUtils.print_error('No data has been serialized')

        return self.output


    def serializeData(self):
        """
        Serialize data, put the result inside self.output
        """
        self.output = '\xAC\xED\x00\x05'

        for type_,data in self.input:
            print type_
            print data
            print len(data)

            if type_ == 'object':

                # Create XStream object and create Java object from the XML structure
                xs = XStream()
                serialized = xs.fromXML(data)

                # Serialize created object with ObjectOutputStream
                bos = io.ByteArrayOutputStream()
                oos = io.ObjectOutputStream(bos)
                oos.writeObject(serialized)

                self.output += bos.toByteArray()[4:]

            elif type_ == 'block':
                
                # TC_BLOCKDATA = (byte)0x77
                if len(data) <= 0xff:
                    self.output += '\x77'
                    self.output += struct.pack('<B', len(data)) # length on 1 byte

                # TC_BLOCKDATALONG = (byte)0x7A
                else:
                    self.output += '\x7A'
                    self.output += struct.pack('>I', len(data)) # length on 4 bytes (big endian)
                
                self.output += ''.join(list(map(lambda x: chr(int(x, 16)), data)))


    def printSerializedData(self):
        """
        Print serialized data in the terminal
        """
        if len(self.output) == 0:
            PrintUtils.print_error('No serialized data to print')
            return

        PrintUtils.print_delimiter()
        PrintUtils.hexdump(self.output)