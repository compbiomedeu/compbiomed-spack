# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ctemplate(Package):
    """The C++ CTemplate system - This library provides an easy to use and
    lightning fast text templating system to use with C++ programs.

    It was originally called Google Templates, due to its origin as the
    template system used for Google search result pages. Now it has a more
    general name matching its community-owned nature."""

    url_list = "https://github.com/OlafvdSpek/ctemplate"
    url      = "https://github.com/OlafvdSpek/ctemplate/archive/refs/tags/ctemplate-2.4.tar.gz"
    git      = "https://github.com/OlafvdSpek/ctemplate.git" 

    # maintainers = ['phu0ngng']
    version('master', branch='master')
    version('2.4', sha256='ccc4105b3dc51c82b0f194499979be22d5a14504f741115be155bd991ee93cfa')
    version('2.3', preferred=True,  sha256='99e5cb6d3f8407d5b1ffef96b1d59ce3981cda3492814e5ef820684ebb782556')
    version('2.2', sha256='1634415a88d4e53cc560df87ea42be96f06edb17836e0e962dcaddb45ac57ab4')
    version('2.1', sha256='e1b13f28e9c1b6b599b5ba9b10c5024d66aed5c5e7ee194bc9383b07dbf42ef6')
    version('2.0', sha256='a7dac437559c17bc6aa6eef8fb3634e01532cb23f19ede3cbdb8c9582c0aa0f0')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')

    def autoreconf(self, spec, prefix):
        which('bash')('autogen.sh')

    def install(self, spec, prefix):
        configure("--prefix=" + prefix)
        make()
        make('install')
