
from astropy.coordinates.baseframe import BaseCoordinateFrame

class ArbitraryFrame(BaseCoordinateFrame):
    pass

# comment these fixes out and build_docs will fail with
# /disks/data0/astro/Projects/astropy-inherit-docstring-mwe/.tox/build_docs/lib/python3.11/site-packages/astropy_inherit_docstring_mwe/example_mod.py:docstring of astropy.coordinates.baseframe.BaseCoordinateFrame.separation_3d:4: WARNING: unknown document: 'astropy:/coordinates/matchsep'
ArbitraryFrame.separation.__doc__ = ArbitraryFrame.separation.__doc__.replace(
    ":doc:`astropy:/", ":doc:`astropy:"
)
ArbitraryFrame.separation_3d.__doc__ = ArbitraryFrame.separation_3d.__doc__.replace(
    ":doc:`astropy:/", ":doc:`astropy:"
)
