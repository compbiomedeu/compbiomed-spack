# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class SlmsLoadbalancing(CMakePackage):
    """A Load Balancing Library (ALL) - The library aims to provide an easy
    way to include dynamic domain-based load balancing into particle based
    simulation codes. The library is developed in the Simulation Laboratory
    Molecular Systems of the Jülich Supercomputing Centre at Forschungszentrum
    Jülich."""

    homepage = "http://slms.pages.jsc.fz-juelich.de/websites/all-website/"
    url_list = "https://gitlab.jsc.fz-juelich.de/SLMS/loadbalancing"
    url      = "https://gitlab.jsc.fz-juelich.de/SLMS/loadbalancing/-/archive/v0.9.2/loadbalancing-v0.9.2.tar.gz"
    git      = "https://gitlab.jsc.fz-juelich.de/SLMS/loadbalancing.git"
    # maintainers = ['phu0ngng']

    version('master', branch='master')
    version('0.9.2', preferred=True,  sha256='2b4ef52c604c3c0c467712d0912a33c82177610b67edc14df1e034779c6ddb71')
    version('0.9.1', sha256='c9e079ef6985c2e0d1e08a73654b21d03786edb569281bb3eb6c2e099161c612')

    depends_on('cmake@3.1:', type='build')
    depends_on('mpi')

    def cmake_args(self):
        args = []
        args.append("-DCMAKE_C_COMPILER=%s" % self.spec['mpi'].mpicc)
        args.append("-DCMAKE_CXX_COMPILER=%s" % self.spec['mpi'].mpicxx)
        return args

