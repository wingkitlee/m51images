import matplotlib.pyplot as plt
import aplpy
from astropy import units as u
from astropy.coordinates import SkyCoord

onearcsec = u.arcsec.in_units('degree')

fig = plt.figure()

f1 = aplpy.FITSFigure('h_m51_v_s20_drz_sci.fits', figure=fig, subplot=[0.1,0.1,0.35,0.8])
f1.show_colorscale(cmap='jet', stretch='sqrt', vmin=0.25)
f1.show_contour('h_m51_h_s20_drz_sci.fits',colors='white',lw=2)
c1 = SkyCoord('13:29:50.38','+47:12:02.28', unit=(u.hourangle,u.deg))
ra1 = c1.ra.degree
dec1= c1.dec.degree

f1.recenter(ra1,dec1,width=20.0*onearcsec,height=50*onearcsec)
f1.show_markers(ra1,dec1,s=200,marker='+',lw=3,c='red')
f1.tick_labels.hide()
f1.ticks.set_color('gray')

f1.add_scalebar(500.0/46.0 * u.arcsecond)	# 1 arcsec = 46pc => 100 pc = 100/46
f1.scalebar.set_corner('top left')
f1.scalebar.set_label('500 pc')
f1.scalebar.set_color('white')
f1.scalebar.set_linewidth(3)  # points


# 13:29:50.14 +47:11:25.27 from Schinnerer et al 2010
c2 = SkyCoord('13:29:50.14', '+47:11:25.27', unit=(u.hourangle,u.deg))
f2 = aplpy.FITSFigure('h_m51_v_s20_drz_sci.fits', figure=fig, subplot=[0.5,0.1,0.35,0.8])
f2.show_colorscale(cmap='jet', stretch='sqrt', vmin=0.25)
f2.show_contour('h_m51_h_s20_drz_sci.fits',colors='white', lw=2)
ra2 = c2.ra.degree
dec2= c2.dec.degree
f2.recenter(ra2,dec2,width=20.0*onearcsec,height=50*onearcsec)
f2.show_markers(ra2,dec2,s=200,marker='+',lw=3,c='red')

f2.tick_labels.hide()
f2.ticks.set_color('gray')
f2.axis_labels.hide()
f2.add_scalebar(500.0/46.0 * u.arcsecond)	# 1 arcsec = 46pc => 100 pc = 100/46
f2.scalebar.set_label('500 pc')
f2.scalebar.set_color('white')
f2.scalebar.set_linewidth(3)  # points
#f2.add_colorbar()
#fig.canvas.draw()

#plt.tight_layout()
#plt.show()
plt.savefig('m51_compare.eps')

