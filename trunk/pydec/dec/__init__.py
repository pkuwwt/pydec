"DEC data structures and algorithms"

from info import __doc__

from rips_complex import *
from cochain import *
from simplicial_complex import *
from regular_cube_complex import *

__all__ = filter(lambda s:not s.startswith('_'),dir())

