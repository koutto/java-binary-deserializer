# -*- coding: utf-8 -*-
import os
import sys
import traceback
import signal
import platform
import argparse
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from lib import *



class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def signal_handler(signal, frame):
    PrintUtils.print_info('Exiting...')
    print
    sys.exit(0)


try:
    SCRIPTNAME = os.path.dirname(os.path.abspath(__file__))
except NameError:
    SCRIPTNAME = os.path.dirname(os.path.abspath(sys.argv[0]))
    
BANNER = """
===============================================================================
                -- Java Serializer/Deserializer --
===============================================================================
"""


def show_help_and_exit(parser):
    print 
    parser.print_help()
    print
    print 'Examples:'
    print '---------'
    print
    print '- Deserialize Java Serialized Binary data:'
    print 'CLASSPATH=./jar/*:./APP_JAR_DIRECTORY/* ~/jython2.7.0/bin/jython java_deserializer.py --deserialize -f data_serialized.raw -o data_deserialized.txt'
    print
    print '- Serialize into Java binary data:'
    print 'CLASSPATH=./jar/*:./APP_JAR_DIRECTORY/* ~/jython2.7.0/bin/jython java_deserializer.py --serialize -f data_deserialized.txt -o data_serialized.raw'
    print
    sys.exit(0)


# -----------------------------------------------------------------------------
# --- Command parsing ---------------------------------------------------------
# -----------------------------------------------------------------------------
print Style.BRIGHT + BANNER + Style.RESET_ALL
print

# Check Jython
if not 'java' in platform.system().lower():
    PrintUtils.print_error('This tool can only be used with Jython')
    PrintUtils.print_info('Command syntax:')
    PrintUtils.print_info('CLASSPATH=./jar/*:./APP_JAR_DIRECTORY/* ~/jython2.7.0/bin/jython java_deserializer.py [options]')
    print
    sys.exit(0)


# Command-line parsing
parser = argparse.ArgumentParser()

io = parser.add_argument_group('Input/Output')
io.add_argument('-f', help='Input file', action='store', type=str, dest='input_file', default=None)
io.add_argument('-o', help='Output file', action='store', type=str, dest='output_file', default=None)
io.add_argument('--offset', help='Force offset (in binary data)', action='store', type=int, dest='offset', default=0)

mode = parser.add_argument_group('Mode')
mode.add_argument('--deserialize', help='Java Serialized Binary to XML', action='store_true', dest='deserialize', default=False)
mode.add_argument('--serialize', help='XML to Java Serialized Binary', action='store_true', dest='serialize', default=False)

rpc = parser.add_argument_group('RPC Server - Serialize/Deserialize Java on-the-fly')
rpc.add_argument('--rpcserver', help='Start RPC Server', action='store_true', dest='rpcserver', default=False)
rpc.add_argument('-p', '--port', help='Listening port', action='store', type=int, dest='port', default=8000)

args = parser.parse_args()


# Check input/output
if not args.rpcserver:
    if not args.input_file:
        PrintUtils.print_error('An input file must be provided')
        show_help_and_exit(parser)
    else:
        if not os.access(args.input_file.strip(), os.F_OK):
            PrintUtils.print_error('Input file ({}) does not exist'.format(args.input_file))
            sys.exit(0)

    if args.serialize and args.offset:
        PrintUtils.print_error('Cannot specify offset when serializing data')
        sys.exit(0)

    input_data = open(args.input_file, 'r').read()[args.offset:]

    if args.output_file is not None:
        filename = args.output_file.strip()
        if os.access(filename, os.F_OK):
            PrintUtils.print_error('Output file ({}) already exists, choose a new file'.format(args.output_file))
            sys.exit(0)

    # Check mode
    if (not args.deserialize and not args.serialize):
        PrintUtils.print_error('A mode (serialize or deserialize) must be selected')
        show_help_and_exit(parser)

    if (args.deserialize and args.serialize):
        PrintUtils.print_error('Choose one mode only')
        show_help_and_exit(parser)


# -----------------------------------------------------------------------------
# --- Processing --------------------------------------------------------------
# -----------------------------------------------------------------------------
output = None

if args.deserialize:
    PrintUtils.print_title('Java Deserialization')
    print 
    deserializer = Deserializer(input_data)

    PrintUtils.print_info('Input file length: {length} (0x{length:x}) bytes'.format(length=len(input_data)))
    print
    PrintUtils.hexdump(deserializer.input)

    PrintUtils.print_info('Scanning input for Java Serialized data and try to deserialize it...')
    output = deserializer.execute()

    # Output into file
    if args.output_file and output:
        if FileUtils.write_to_file(args.output_file.strip(), str(output)):
            PrintUtils.print_success('Output written into file "{file}"'.format(file=args.output_file))
        else:
            PrintUtils.print_error('An error occured when writing to file. Check permissions')

    
elif args.serialize:
    PrintUtils.print_title('Java Serialization')
    print 

    if input_data:
        PrintUtils.print_error('Empty input data')

    # Convert input_data from str to list of tuples
    try:
        input_data = ast.literal_eval(input_data)
    except Exception:
        PrintUtils.print_error('Input data is malformed')
        sys.exit(1)

    serializer = Serializer(input_data)

    PrintUtils.print_info('Input file length: {length} (0x{length:x}) bytes'.format(length=len(input_data)))
    output = serializer.execute()

    # Output into file
    if args.output_file and output:
        if FileUtils.write_to_file(args.output_file.strip(), output):
            PrintUtils.print_success('Output written into file "{file}"'.format(file=args.output_file))
        else:
            PrintUtils.print_error('An error occured when writing to file. Check permissions')


if args.rpcserver:
    try:
        server = SimpleXMLRPCServer(("", args.port), requestHandler=RequestHandler)
        server.register_introspection_functions()
        server.register_instance(RPCServer())
    except:
        PrintUtils.print_error('Error occured when trying to start RPC server. Check if port already used.')
        sys.exit(0)

    PrintUtils.print_title('RPC Server: ON - Waiting for calls...')
    print
    signal.signal(signal.SIGINT, signal_handler)
    PrintUtils.print_info('Press Ctrl+C to stop the server')
    print
    server.serve_forever()


print