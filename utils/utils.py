from configurations.configurations import Configurations
from datetime import date

class Utils():
		def __init__(self):
				self.__configurations = Configurations()

		def read_file(self):
				with open(self.__configurations.file_output, 'r') as file:
						return list(map(lambda x: x.replace('\n', '') , file.readlines()))

		def write_file(self, _type, value, description):
				with open(self.__configurations.file_output, 'a+') as file:
						return file.write(
								f'\n{date.today()} - {_type} - R$ {value} - {description}'
						)