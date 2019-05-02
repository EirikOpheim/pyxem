# -*- coding: utf-8 -*-
# Copyright 2017-2019 The pyXem developers
#
# This file is part of pyXem.
#
# pyXem is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyXem is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyXem.  If not, see <http://www.gnu.org/licenses/>.

import pickle
import numpy as np


def load_CalibrationDataLibrary(filename, safety=False):
    """Loads a previously saved vectorlibrary.

    Parameters
    ----------
    filename : str
        The location of the file to be loaded
    safety : bool (defaults to False)
        Unpickling is risky, this variable requires you to acknowledge this.

    Returns
    -------
    CalibrationDataLibrary
        Previously saved Library

    See Also
    --------
    CalibrationDataLibrary.pickle_library()
    """
    if safety:
        with open(filename, 'rb') as handle:
            return pickle.load(handle)
    else:
        raise RuntimeError('Unpickling is risky, turn safety to True if \
        trust the author of this content')


class CalibrationDataLibrary():
    """Maps crystal structure (phase) to diffraction vectors.

    Attributes
    ----------
    au_x_grating_dp : ElectronDiffraction
        A ring diffraction pattern obtained from an Au X-grating standard.
    au_x_grating_im : :obj:`hyperspy.signals.Signal2D`
        An image of an Au X-grating standard.
    moo3_dp : ElectronDiffraction
        A spot diffraction pattern obtained from an MoO3 standard.
    moo3_im : :obj:`hyperspy.signals.Signal2D`
        An image of an MoO3 standard.
    """

    def __init__(self, au_x_grating_dp, au_x_grating_im, moo3_dp, moo3_im):
        self.au_x_grating_dp = au_x_grating_dp
        self.au_x_grating_im = au_x_grating_im
        self.moo3_dp = moo3_dp
        self.moo3_im = moo3_im

    def pickle_library(self, filename):
        """Saves a diffraction library in the pickle format.

        Parameters
        ----------
        filename : str
            The location in which to save the file

        See Also
        --------
            load_VectorLibrary()

        """
        with open(filename, 'wb') as handle:
            pickle.dump(self, handle, protocol=pickle.HIGHEST_PROTOCOL)
