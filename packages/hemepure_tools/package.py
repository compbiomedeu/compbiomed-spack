from spack import *

class Hemepuretools(Package):

    homepage = "https://github.com/JonMcCullough/HemePure_tools"
    url      = "https://github.com/JonMcCullough/HemePure_tools"
    git      = "https://github.com/JonMcCullough/HemePure_tools.git"

    version('master',branch='master')

    depends_on('cmake@3.15:',type='build')
    depends_on('python@3:',type='run')

    depends_on('mpi')
    depends_on('zlib')
    depends_on('libtirpc')