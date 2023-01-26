#!/bin/sh
trap "exit" INT

# This script performs the setup of Palabos: it retrieves a tagged release from
# their Gitlab pages, afterwhich additional hemocell-specific features are
# added by applying the patch at `hemocell/patch`.

# supported tag and download target
tag="v2.3.0"

mv "palabos-${tag}" palabos

# apply the patch
(
  cd patch || { echo "Patch directory not present"; exit 1; }
  ./patchPLB.sh
)