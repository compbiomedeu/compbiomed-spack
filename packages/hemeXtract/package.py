

from spack import *

class Hemextract(MakefilePackage):

    homepage = "https://github.com/UCL-CCS/hemeXtract"
    url      = "https://github.com/UCL-CCS/hemeXtract"
    git      = "https://github.com/UCL-CCS/hemeXtract.git"

    version('master', branch='master')

    depends_on('libtirpc')

    # patch the Makefile
    patch('hemeXtract.patch')

    build_targets = ['CC=cc','CXXFLAGS=cxxflags']

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install('hemeXtract', prefix.bin)

#    depends_on('argp-standalone')


"""
class Hemepuretools(Package):
    url = 
    depends_on('python@3:')
"""
