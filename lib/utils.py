from colorama import *
import os
import os.path
import shutil
import pprint
import json
try:
    import pygments
    from pygments.lexers import *
    from pygments.formatters import *
    pygments_import = True
except ImportError:
    print 'Pygments not found, no XML syntax highlighting available'
    pygments_import = False



class PrintUtils(object):

	@staticmethod
	def hexdump(src, length=16):
		FILTER = ''.join([(len(repr(chr(x))) == 3) and chr(x) or '.' for x in range(256)])
		lines = []
		for c in xrange(0, len(src), length):
			chars = src[c:c+length]
			hex = ' '.join(["%02x" % ord(x) for x in str(chars)])
			printable = ''.join(["%s" % ((ord(x) <= 127 and FILTER[ord(x)]) or '.') for x in str(chars)])
			lines.append("%04x  %-*s  %s\n" % (c, length*3, hex, printable))
		print ''.join(lines)

	@staticmethod
	def print_xml_highlighted(xml):
		if pygments_import:
			print pygments.highlight(xml, 
				                     pygments.lexers.get_lexer_by_name('XML'), 
				                     pygments.formatters.get_formatter_by_name('terminal'))
		else:
			print xml

	@staticmethod
	def print_title(title):
		print Style.BRIGHT + Fore.YELLOW + title + Style.RESET_ALL

	@staticmethod
	def print_error(reason):
		print Style.BRIGHT + Fore.RED + '[!] ' + reason.strip() + Style.RESET_ALL

	@staticmethod
	def print_warning(reason):
		print Style.BRIGHT + Fore.YELLOX + '[!] ' + Style.RESET_ALL + reason.strip()

	@staticmethod
	def print_success(reason):
		print Style.BRIGHT + Fore.GREEN + '[+] ' + Style.NORMAL + reason.strip() + Style.RESET_ALL

	@staticmethod
	def print_info(info):
		print Style.BRIGHT + "[~] " + Style.RESET_ALL + info.strip() 

	@staticmethod
	def print_delimiter():
		print '-'*80



class FileUtils(object):

	@staticmethod
	def write_to_file(filename, data):
		try:
			f = open(filename, 'w')
			f.write(data)
			return True
		except Exception:
			return False

	@staticmethod
	def write_pprint_to_file(filename, data):
		try:
			f = open(filename, 'w')
			pprint.pprint(data, f)
			return True
		except Exception:
			return False

	@staticmethod
	def write_json_to_file(filename, data):
		#try:
		f = open(filename, 'w')
		json.dump(data, f)
		return True
		#except Exception:
		#	return False


class BinaryUtils(object):

	@staticmethod
	def tohex(val, nbits=8):
  		return hex((val + (1 << nbits)) % (1 << nbits))

