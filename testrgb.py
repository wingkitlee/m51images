import numpy as np
import aplpy

fitslist = ['h_m51_h_s20_drz_sci.fits',
			'h_m51_v_s20_drz_sci.fits',
			'h_m51_b_s20_drz_sci.fits'
			]

# Reproject the images to a common projection - this will also produce
# ``2mass_cube_2d.fits``
aplpy.make_rgb_cube(fitslist, 'm51_cube.fits')

# Make an RGB image
aplpy.make_rgb_image('m51_cube.fits', 'm51_rgb.png')

# Plot the RGB image using the 2d image to indicate the projection
f = aplpy.FITSFigure('m51_cube_2d.fits')
f.show_rgb('m51_rgb.png')
