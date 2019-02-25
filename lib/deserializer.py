# -*- coding: utf-8 -*-
import os
import platform
from lib import *
if 'java' in platform.system().lower():
    import java.io as io
    from com.thoughtworks.xstream import XStream


class Deserializer(object):

    def __init__(self, input_):
        """
        :param input: Binary data that must be deserialized
        """
        self.input  = input_
        self.output = []


    def execute(self):
        """
        Scan input (file) for Java Serialized data to deserialize

        :return: List of tuples (type, data) where:
            - type can be:
                - object: for deserialized Java object
                - block: raw data corresponding to primitive types (boolean, byte, char...)
            - data is the deserialized data (in XML form) when type = object, otherwise the raw data
        """

        # Java Serialized stream begins with:
        # AC ED: STREAM_MAGIC
        # 00 05: STREAM_VERSION
        header = self.input.find('\xAC\xED\x00\x05')
        if header >= 0:
            PrintUtils.print_success('Java Serialized data header found at offset 0x{0:x}'.format(header))
            print
            self.deserializeStream()
            self.printDeserializedData()
        else:
            PrintUtils.print_error('Unable to find Java Serialized data into input, assuming it is only raw data')
            self.output.append(('block', self.input))
        return self.output


    def deserializeStream(self):
        """
        Deserialize stream, put the result inside self.output
        """
        bis = io.ByteArrayInputStream(self.input)
        ois = io.ObjectInputStream(bis)
        i = 0

        while True:
            # Block raw data ?
            block_data = []
            try:
                while True:
                    byte = BinaryUtils.tohex(ois.readByte())
                    #raw_byte = chr(int(byte, 16))
                    #block_data.append(raw_byte)
                    block_data.append(byte)
            except:
                if len(block_data) > 0:
                    #print 'Block data detected - length = {0}:'.format(len(block_data))
                    self.output.append(('block', block_data))
                    i += 1
                    print

            # Object ?
            try:
                obj = ois.readObject()

                # converting Java object to XML structure
                xs = XStream()
                xml = xs.toXML(obj)
                #self.output += xml + '\n'
                self.output.append(('object', xml))
                i += 1
                continue                
            except:
                pass

            # if we arrive here, it means there is nothing more
            break


    def printDeserializedData(self):
        """
        Print deserialized data nicely in the terminal
        """
        if len(self.output) == 0:
            PrintUtils.print_error('No deserialized data to print')
            return

        PrintUtils.print_delimiter()
        i = 0
        for type_,data in self.output:
            if type_ == 'block':
                PrintUtils.print_info('[0x{i:02x}] Block raw data - length = {length} (0x{length:02x}) bytes:'.format(i=i, length=len(data)))
                PrintUtils.hexdump(''.join(list(map(lambda x: chr(int(x, 16)), data))))
                #print self.output[i][1]
            elif type_ == 'object':
                PrintUtils.print_info('[0x{i:02x}] Java Object (converted into XML):'.format(i=i))
                PrintUtils.print_xml_highlighted(data)
            i += 1
            PrintUtils.print_delimiter()

        return



