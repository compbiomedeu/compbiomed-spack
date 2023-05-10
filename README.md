
> :warning: This repository is still in a development stage. As soon as it is ready
> this notice will be removed and the project will announced through regular
> CompBioMed communication channels. Until then, you are welcome to try it and
> report your experiences. We will do our best to fix problems as soon as they
> are uncovered.

# CompBioMed Spack Repository

The repository hosts packages related to the CompBioMed Centre of Excellence (compbiomed.eu).
This includes both the core applications (when permissible) and various extension
modules.

The target audiences for Spack are:
- system administrators at HPC facilities
- developers interested in OS-indepenent, consistent software stacks for their development
- new users interested in minimal installation procedures

More information on Spack can be found in the [official documentation](https://spack.readthedocs.io/en/latest/index.html).

## Prerequisities

## Setting up the CompBioMed Spack repository

Assuming you have spack installed and loaded in your session, all you need to do is:

```
git clone https://github.com/compbiomedeu/compbiomed-spack.git
spack repo add compbiomed-spack
```

## Installing CompBioMed applications

You are now able to install CompBioMed software, including:

* HemePure
* HemoCell (TODO)
* Palabos (TODO)

For example to install and load Hemepure (CPU-version) you would do:

```
$ spack install hemepure
$ module load hemepure
```

Spack requires internet access to fetch tarballs of dependencies. If you are
in an isolated network environment consult the Spack documentation or get in
contact with your local system administrators.

## Customization

## Troubleshooting

## Acknowledgements


