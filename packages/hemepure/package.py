# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *

class Hemepure(CMakePackage):
    """HemeLB is a high performance lattice-Boltzmann solver optimized for
    simulating blood flow through sparse geometries, such as those found in the
    human vasculature. It is routinely deployed on powerful supercomputers,
    scaling to hundreds of thousands of cores even for complex geometries .
    HemeLB has traditionally been used to model cerebral bloodflow and vascular
    remodelling in retinas , but is now being applied to simulating the fully
    coupled human arterial and venous trees.

    HemePure is a optimized verion of HemeLB with improved memory, compilation 
    and scaling"""

    homepage = "https://github.com/UCL-CCS/HemePure"
    url      = "https://github.com/UCL-CCS/HemePure"
    git      = "https://github.com/UCL-CCS/HemePure.git"

    # maintainers = ['phu0ngng']

    version('master', branch='master')

    variant('tracer', default=True, description='Use particles as tracers')
    variant('simd', default='auto', description='Use SIMD instrinsics',
            values=('sse3', 'avx2', 'avx512', 'auto', 'False'))
    variant('velocity_weight', default=False, 
            description='Use velocity weights file')
    variant('gmyplus', default=False, description='Use GMY+ format')
    variant('mpi_call', default=False, 
            description='Use standard MPI functions when reading blocks')
    variant('mpi_win', default=False, 
            description='Use MPI windowing to help load large domains')
    variant('big_mpi', default=False, 
            description='Use MPI windowing to help load large domains')
    variant('parmetis', default=False, description='Use ParMETIS')

    depends_on('mpi')
    depends_on('cmake@3.15:')
    depends_on('parmetis')
    depends_on('boost@1.54:+mpi')
    depends_on('tinyxml+stl')
    depends_on('slms-loadbalancing')
    depends_on('ctemplate')
    depends_on('libtirpc')

    root_cmakelists_dir = 'src'

    def setup_build_environment(self, env):
                env.prepend_path('CPATH', self.spec['libtirpc'].prefix.include.tirpc)
                env.append_flags('LDFLAGS', '-ltirpc')

    def cmake_args(self):
        args = []
        args.append("-DCMAKE_C_COMPILER=%s" % self.spec['mpi'].mpicc)
        args.append("-DCMAKE_CXX_COMPILER=%s" % self.spec['mpi'].mpicxx)
        args.append("-DCMAKE_CXX_STANDARD=11")
        args.append("-DCMAKE_CXX_STANDARD_REQUIRED=ON")

        if '+tracer' in self.spec:
            args.append("-DHEMELB_TRACER_PARTICLES=ON")

        if '+velocity_weight' in self.spec:
            args.append("-DHEMELB_USE_VELOCITY_WEIGHTS_FILE=ON")

        if '+gmyplus' in self.spec:
            args.append("-DHEMELB_USE_GMYPLUS=ON")

        if '+mpi_call' in self.spec:
            args.append("-DHEMELB_USE_MPI_CALL=ON")

        if '+mpi_win' in self.spec:
            args.append("-DHEMELB_USE_MPI_WIN=ON")

        if '+big_mpi' in self.spec:
            args.append("-DHEMELB_USE_BIGMPI=ON")

        if '+parmetis' in self.spec:
            args.append("-DHEMELB_USE_PARMETIS=ON")

		# SIMD activation
        args.append("-DHEMELB_USE_SSE3=OFF")
        # 1. With users' specification
        if 'simd=sse3' in self.spec:
            args.append("-DHEMELB_USE_SSE3=ON")
        elif 'simd=avx2' in self.spec:
            args.append("-DHEMELB_USE_AVX2=ON")
        elif 'simd=avx512' in self.spec:
            args.append("-DHEMELB_USE_AVX512=ON")
        # 2. Based on properties of the target (inspiring from Gromacs package)
        elif 'simd=auto' in self.spec:
            target = self.spec.target
            if target == 'zen':
                # AMD Family 17h (EPYC Romei & Naples)
                args.append("-DHEMELB_USE_AVX2=ON")
            elif target >= 'bulldozer':
                # AMD Family 15h
                args.append("-DHEMELB_USE_SSE3=ON")
            elif target == 'mic_knl':
                # Intel KNL
                args.append("-DHEMELB_USE_AVX512=ON")
            else:
                # Other Intel architectures
                simd_features = [
                        ('sse3', 'SSE3'),
                        ('avx2', 'AVX2'),
                        ('avx512', 'AVX512')
                        ]
                for (feature, flag) in reversed(simd_features):
                    if feature in target:
                        args.append("-DHEMELB_USE_%s=ON" %flag)
                        break

        #if the target does not belong to any of aboved cases, no SIMD intrinsics support
        return args

