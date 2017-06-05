import pyspeckit
from spectral_cube import SpectralCube
import astropy.units as u
import numpy as np
import matplotlib.pyplot as plt


filename1 = 'C:/Users/tanli/Desktop/attachments/GBT spectrum testing (NH3)/B112.n11.fits'
data1 = SpectralCube.read(filename1)
intensity1 = data1.unmasked_data[:,0,0]    

filename2 = 'C:/Users/tanli/Desktop/attachments/GBT spectrum testing (NH3)/B112.n22.fits'
data2 = SpectralCube.read(filename2)
intensity2 = data2.unmasked_data[:,0,0]    

data_converted = data1.with_spectral_unit(u.km/u.s, velocity_convention='radio')
plt.plot(data_converted.spectral_axis, intensity2)


frq1 = data1.spectral_axis.value
frq2 = data2.spectral_axis.value

frq = np.concatenate((frq1,frq2))
intensity = np.concatenate((intensity1,intensity2))

plt.plot(frq/1e10, intensity)




sp = pyspeckit.Spectrum(data = intensity, xarr = frq,
                        xarrkwargs = {'unit':'Hz'})
        
sp.Registry.add_fitter('cold_ammonia', pyspeckit.spectrum.models.ammonia.cold_ammonia, 5)


sp.plotter(figure=1)

sp.specfit(fittype='cold_ammonia',multifit=None,
           guesses=[15, 5, 13.5, 2.0, -5.0, 0.0])




sp.plotter.savefig('testfit')