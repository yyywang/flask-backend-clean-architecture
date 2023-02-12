# https://github.com/yitter/IdGenerator/tree/master/Python
from .generator import DefaultIdGenerator
from .options import IdGeneratorOptions

__id_generator_options = IdGeneratorOptions()
id_generator = DefaultIdGenerator()
id_generator.set_id_generator(__id_generator_options)
