import matplotlib.pyplot as plt
import aplpy
from astropy import units as u
from astropy.coordinates import SkyCoord

onearcsec = u.arcsec.in_units('degree')

fig = plt.figure()
#ax1 = fig.add_subplot(121)

f1 = aplpy.FITSFigure('h_m51_v_s20_drz_sci.fits', figure=fig, subplot=[0.1,0.1,0.35,0.8])
f1.show_grayscale(stretch='arcsinh')
f1.show_contour('h_m51_h_s20_drz_sci.fits',colors='white')
c1 = SkyCoord('13:29:50.38','+47:12:02.28', unit=(u.hourangle,u.deg))
ra1 = c1.ra.degree
dec1= c1.dec.degree

f1.recenter(ra1,dec1,width=40.0*onearcsec,height=80*onearcsec)
f1.show_markers(ra1,dec1,s=200,marker='+',lw=3)

#ax2 = fig.add_subplot(122)
f2 = aplpy.FITSFigure('h_m51_v_s20_drz_sci.fits', figure=fig, subplot=[0.5,0.1,0.35,0.8])
f2.show_grayscale(stretch='arcsinh')
f2.show_contour('h_m51_h_s20_drz_sci.fits',colors='white')

#fig.canvas.draw()

plt.tight_layout()
plt.show()

