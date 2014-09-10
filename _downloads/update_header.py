#!/usr/bin/env python

from astropy.io import fits
import glob

filelist = glob.glob('UVES/*')

for f in filelist:
    hdu = fits.open(f, mode='update')
    hdu[0].header.rename_keyword('RADECSYS', 'RADESYS')
    print(hdu[0].header['RADESYS'])
    hdu.flush()
    hdu.close()
