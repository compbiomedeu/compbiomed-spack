# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Palabos(CMakePackage):
    """The Palabos library is a framework for general-purpose computational 
    fluid dynamics (CFD), with a kernel based on the lattice Boltzmann (LB) 
    method. It is used both as a research and an engineering tool: its 
    programming interface is straightforward and makes it possible to set up 
    fluid flow simulations with relative ease, or, if you are knowledgeable of 
    the lattice Boltzmann method, to extend the library with your own models. 
    Palabos stands for Parallel Lattice Boltzmann Solver.
    """

    homepage = "https://palabos.unige.ch"
    url      = "https://gitlab.com/unigespc/palabos/-/archive/v2.3.0/palabos-v2.3.0.tar.gz"
    git      = "https://gitlab.com/unigespc/palabos.git"


    tags = ['lattice-boltzmann-method','computational-fluid-dynamics']

    # maintainers = ['ivanp']

    version('dev',    branch='dev')
    version('master', branch='master')

    version('2.3.0', sha256='2085de7b06cc9c4a7b3457f7c2d17747d8960c0f861e32fc883acd504dfc1e23')
    version('2.2.1', sha256='4ccd8911b4c075b7984ffd69ea7c8485423490676551fef394bc65d2d6894ce6')
    version('2.2.0', sha256='f890d7a6f18fa8f082d84669e2516e97e1d211546425d4c28fcad824fbb9ddd4')
    version('2.1r0', sha256='11adec3d07f01570174fb87bec7d382ad67090e9e78f25b9863467baa063cf0d')

    variant('hdf5', default=True, description='Build with HDF5 output', when='@2.2:')
    variant('mpi',  default=True, description='Build parallel version')

    depends_on('cmake@3:',type='build')
    depends_on('mpi',  when='+mpi')
    depends_on('hdf5', when='+hdf5')

    # depends_on('imagemagick',type='run')

    def cmake_args(self):
        args = [
            self.define('ENABLE_POSIX', True),
            self.define_from_variant('ENABLE_MPI','mpi'), 
            self.define_from_variant('BUILD_HDF5','hdf5')
            ]
        return args

    def install(self,spec,prefix):
        # Palabos has no install target
        pass