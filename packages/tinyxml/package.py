from spack.pkg.builtin.tinyxml import Tinyxml as BuiltinTinyxml

class Tinyxml(BuiltinTinyxml):
    """Simple, small, efficient, C++ XML parser"""

    variant('stl', default=False, description='Use STL with TIXML')

    def cmake_args(self):
        args = super(BuiltinTinyxml, self).cmake_args()
        spec = self.spec
        args.append('-DTIXML_USE_STL=%s' % ('YES' if '+stl' in spec else 'NO'))
        return args
