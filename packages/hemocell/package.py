import os
import stat

from spack import *


class Hemocell(CMakePackage):
    """HemoCell is a framework for simulating suspensions of deformable cells, 
    focusing on blood. It is based of the combined Immersed boundary-lattice 
    Boltzmann method (IB-LBM) and is currently built on top of the open source 
    C++ lattice Boltzmann solver Palabos."""

    homepage = "https://www.hemocell.eu/"
    #url      = "https://github.com/UvaCsl/HemoCell/archive/refs/tags/stable_latest.tar.gz"
    #git      = "https://github.com/UvaCsl/HemoCell.git"
    git      = "https://github.com/ivan-pi/HemoCell.git"

    tags = ['lattice-boltzmann-method', 'immersed-boundary-method', 'computational-fluid-dynamics']

    # maintainers = ['ivanp']

    version('master', branch='master')
    version('export_cube', branch='export_cube')
    
    version('2.6',commit='2546b20555ede99c496423c0db0b6bac17579752',preferred=True)

    #version('2.5', commit='cf106f34aa015ee28d8de32ccd440ff3fb5abb16')
    #version('2.4', commit='4dbcb0b2bfe9e36cbe9f778d6a54e787a9457c4b')
    #version('2.3', commit='f672f11e5f80070285e222d7b4a6abaa82879253')
    #version('2.2', commit='3a4c777821bc90a0292368de8dbdbd332eadb2e0')
    #version('2.1', commit='40a83a228cb409e018f7a647bbcd970febd7e9dc')

    #version('2.0', sha256='449e7601d4c29a752471012463d722bfbdad7ac9561e9ff9ffb0efc60f0b8be9')

    variant('parmetis',default=True, description="Build with ParMETIS for load balancing")
    
    # TODO: variant which exports benchmarks for integration in benchmarking
    #       framework (JUBE). Possibilities are:
    #
    #   1. Export examples (e.g. cube) directly, and any pertaining scripts, setup files
    #      - optionally, unpack analysis scripts as resource
    #   2. Export HemoCell library (.a,.so), and make the cube driver an
    #      independent package which installs the executable
    #      which uses Spack-installed library
    #   3. Other solutions?

    # Nota bene:
    # - HemoCell v2.6 does not export a library or a main driver
    # - For the foreseeable future we will install some of the example
    #   cases to use them in our testing and benchmarking workflows
    # - If set to False, spack will not install anything 
    variant('scaling',default=True, description="Install targets for scaling tests")

    depends_on('cmake@3.1:',type='build')

    depends_on('cmake@3.15:',type='build',when='+scaling')

    #depends_on('GTest',type='test')
    depends_on('mpi')
    depends_on('hdf5@1.8.16:+hl')

    # HemoCell v2.6 expects static METIS and ParMETIS archives
    depends_on('parmetis@4.0.3~shared ^metis~shared',when='+parmetis')

    # Fetch Palabos as a resource, and unpack in the stage source path (.)
    resource(
       name='palabos',
       url='https://gitlab.com/unigespc/palabos/-/archive/v2.3.0/palabos-v2.3.0.tar.gz',
       sha256='2085de7b06cc9c4a7b3457f7c2d17747d8960c0f861e32fc883acd504dfc1e23',
       destination='.'
    )

    # TODO: make sure patching works also for versions lower than v2.5
    # Patch the setup.sh script so it doesn't fetch Palabos
    patch('setup.patch',level=0)

    def patch(self):

        script_path = "./setup.sh"
        st = os.stat(script_path)
        os.chmod(script_path,st.st_mode | stat.S_IXUSR)

        script = Executable(script_path)
        script()

    def cmake_args(self):
        args = []
        args.append(self.define('BUILD_TESTING',False))
        args.append(self.define('HEMOCELL_INSTALL_CUBE',True))
        return args

    def build(self, spec, prefix):
        """Make the build targets"""
        super().build(spec,prefix)

        with working_dir(self.build_directory):
            if '+scaling' in spec:
                cmake("--build", "examples/cube/")

    def install(self, spec, prefix):
        """Make the install targets"""
        super().install(spec, prefix)

        with working_dir(self.build_directory):
            if '+scaling' in spec:
                cmake("--install", "examples/cube/")
