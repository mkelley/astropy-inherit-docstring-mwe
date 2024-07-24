
Demo
----


    tox -e build_docs

Then open docs/_build/html/index.html and navigate to the separation docstring.
Note the link to the astropy page: Separations, Offsets, Catalog Matching, and
Related Functionality.

Then edit example_mod.py and comment out the docstring fixes.  Re-build and the
following errors appear (one for separation(), one for separation_3d()):


    /disks/data0/astro/Projects/astropy-inherit-docstring-mwe/.tox/build_docs/lib/python3.11/site-packages/astropy_inherit_docstring_mwe/example_mod.py:docstring of astropy.coordinates.baseframe.BaseCoordinateFrame.separation:3: WARNING: unknown document: 'astropy:/coordinates/matchsep'
    /disks/data0/astro/Projects/astropy-inherit-docstring-mwe/.tox/build_docs/lib/python3.11/site-packages/astropy_inherit_docstring_mwe/example_mod.py:docstring of astropy.coordinates.baseframe.BaseCoordinateFrame.separation_3d:4: WARNING: unknown document: 'astropy:/coordinates/matchsep'




License
-------

This project is Copyright (c)  and licensed under
the terms of the BSD 3-Clause license. This package is based upon
the `Openastronomy packaging guide <https://github.com/OpenAstronomy/packaging-guide>`_
which is licensed under the BSD 3-clause licence. See the licenses folder for
more information.

Contributing
------------

We love contributions! astropy-inherit-docstring-mwe is open source,
built on open source, and we'd love to have you hang out in our community.

**Imposter syndrome disclaimer**: We want your help. No, really.

There may be a little voice inside your head that is telling you that you're not
ready to be an open source contributor; that your skills aren't nearly good
enough to contribute. What could you possibly offer a project like this one?

We assure you - the little voice in your head is wrong. If you can write code at
all, you can contribute code to open source. Contributing to open source
projects is a fantastic way to advance one's coding skills. Writing perfect code
isn't the measure of a good developer (that would disqualify all of us!); it's
trying to create something, making mistakes, and learning from those
mistakes. That's how we all improve, and we are happy to help others learn.

Being an open source contributor doesn't just mean writing code, either. You can
help out by writing documentation, tests, or even giving feedback about the
project (and yes - that includes giving feedback about the contribution
process). Some of these contributions may be the most valuable to the project as
a whole, because you're coming to the project with fresh eyes, so you can see
the errors and assumptions that seasoned contributors have glossed over.

Note: This disclaimer was originally written by
`Adrienne Lowe <https://github.com/adriennefriend>`_ for a
`PyCon talk <https://www.youtube.com/watch?v=6Uj746j9Heo>`_, and was adapted by
astropy-inherit-docstring-mwe based on its use in the README file for the
`MetPy project <https://github.com/Unidata/MetPy>`_.
