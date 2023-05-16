

from spack import *

class Hemextract(MakefilePackage):

    homepage = "https://github.com/UCL-CCS/hemeXtract"
    url      = "https://github.com/UCL-CCS/hemeXtract"
    git      = "https://github.com/UCL-CCS/hemeXtract.git"

    version('master', branch='master')

    depends_on('libtirpc')
    depends_on('python@2:',type='run')

    # patch the Makefile
    patch('hemeXtract.patch')

    build_targets = ['CC=cc']

    # inject flags as make variables, i.e `make CXXFLAGS=<cxxflags>`
    flag_handler = build_system_flags

    # installation step is missing in the Makefile
    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install('hemeXtract', prefix.bin)

