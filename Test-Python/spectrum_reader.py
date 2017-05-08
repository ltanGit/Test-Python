"""
Created on Sat. May, 6th, 2017

@author: Lige Tan

"""

from spectral_cube import SpectralCube
import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np

def main():
    #
    trans = Translation()
    trans.arrangement()


class Translation:
    
    def __init__(self):
        # Initialize a Translation task of spectra
        # - self is the Translation to initialize
        
        self.offset_value = 3
        self.date = 528        ## M/DD
        self.start = 92        ## start number of .fits file
        self.end = 94          ## end number of .fits file
    
    def arrangement(self):
        
        for i in range(self.start,self.end+1):
            names = ['','','']
            for j in range(1,4):
                string1 = '/mnt/work/ltan/data/jcmth20140'
                string2 = '_000'
                string3 = '_0'
                string4 = '_reduced001_nit_000.fits'
                names[j-1] = string1 + str(self.date) + string2 + str(i) + string3 + str(j) + string4
            plt.figure(i-self.start+1)
            self.doppler_conversion(names[0], names[1], names[2], i)
    
    def doppler_conversion(self, file_name1, file_name2, file_name3, file_number):
        
        spectrum1 = SpectralCube.read(file_name1)
        spectrum1_fq_converted = spectrum1.with_spectral_unit(u.km/u.s, velocity_convention='radio')
        spectrum1_intensity = spectrum1.unmasked_data[:,0,0]
        plt.plot(spectrum1_fq_converted.spectral_axis, spectrum1_intensity)
        plt.hold(True)
          
        spectrum2 = SpectralCube.read(file_name2)
        spectrum2_fq_converted = spectrum1.with_spectral_unit(u.km/u.s, velocity_convention='radio')
        spectrum2_intensity = spectrum2.unmasked_data[:,0,0]
        length = len(spectrum2_intensity)
        offset = np.ones((length))        ## for m X n matrix: np.ones((length,1)), a tuple inside
        offset.fill(self.offset_value)
        spectrum2_intensity = np.add(spectrum2_intensity / u.Kelvin, offset)
        plt.plot(spectrum2_fq_converted.spectral_axis, spectrum2_intensity*u.Kelvin)
        plt.hold(True)
          
        spectrum3 = SpectralCube.read(file_name3)
        spectrum3_fq_converted = spectrum3.with_spectral_unit(u.km/u.s, velocity_convention='radio')
        spectrum3_intensity = spectrum3.unmasked_data[:,0,0]
        length = len(spectrum3_intensity)
        offset = np.ones((length))        ## for m X n matrix: np.ones((length,1)), a tuple inside
        offset.fill(2*self.offset_value)
        spectrum3_intensity = np.add(spectrum3_intensity / u.Kelvin, offset)
        plt.plot(spectrum3_fq_converted.spectral_axis, spectrum3_intensity)
        plt.hold(False)
         
        #print(spectrum1_fq_converted.spectral_axis[0])
        #print(spectrum1_intensity[0])
        #print(spectrum1[0])
         
        plt.xlim([spectrum1_fq_converted.spectral_axis[len(spectrum1)-1] * u.s / u.km, spectrum1_fq_converted.spectral_axis[0] * u.s / u.km])
        plt.xlabel(r'$\ V_{LSR} $  (km/s)',fontsize = 12)
        plt.ylabel(r'$\ T^\ast_A $',fontsize = 12)
        plt.title('20140'+str(self.date)+': 000'+str(file_number), fontsize = 16)
        lgd = plt.legend(['the 1st frequency range','the 2nd frequency range','the 3rd frequency range'], bbox_to_anchor=(1,1))
        plt.savefig('20140'+str(self.date)+'_000'+str(file_number)+'.png', bbox_extra_artists=(lgd,), bbox_inches='tight')

    
    def export_spectra():
        pass



main()
