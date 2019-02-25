# -*- coding: utf-8 -*-
from lib import *
import time
import os
import base64
import pickle


class RPCServer(object):

    def deserialize(self, b64encoded_data):
        """
        Deserialize Java serialized
        :param b64encoded_data: Java serialized data, encoded in Base64
        :return: Base64(PythonSerialized(   list of tuples (type, data)  ))

        In order to recover the list of tuples from the caller (on client-side):
        pickle.loads(base64.b64decode(result))
        """
        input_data = base64.b64decode(b64encoded_data)
        print
        PrintUtils.print_title('Receive RPC Call deserialize')
        print
        PrintUtils.hexdump(input_data)
        print

        deserializer = Deserializer(input_data)
        output = deserializer.execute()

        return base64.b64encode(pickle.dumps(output))


    def serialize(self, b64encoded_data):
        """
        Serialize data
        :param b64encoded_data: Data to serialize, at the format: Base64(PythonSerialized(   list of tuples (type, data)  ))
            where:
            - type can be:
                - object: for deserialized Java object
                - block: raw data corresponding to primitive types (boolean, byte, char...)
            - data is XML structure of Java Object when type = object, otherwise the raw data
        
        :return: Base64 encoded raw bytes of serialized data
        """
        input_data = pickle.loads(base64.b64decode(b64encoded_data))
        print
        PrintUtils.print_title('Receive RPC Call serialize')
        print
        print input_data
        print

        serializer = Serializer(input_data)
        output = serializer.execute()

        # ser = Serializer(input_data)
        # output = ser.execute()

        return base64.b64encode(output)
