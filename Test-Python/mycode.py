import matplotlib.pyplot as plt
import numpy as np
import math

def main():
    Lambda = input('lambda is:')
    Lambda = float(Lambda)
    MySineWave(Lambda)

def MySineWave(Lambda):
    pi = math.pi
    x = np.arange(-2*pi, 2*pi, 0.1)
    k = 2*pi/Lambda
    y = np.sin(k*x)
    plt.plot(x, y, 'r-',markersize = 2)
    plt.xlabel('Position', fontsize=12)
    plt.ylabel('Amplitude', fontsize=12)
    #plt.legend('the sine wave',loc='upper left', fontsize=12) # not working
    plt.title('Sine Wave with Wavelength = %s' % Lambda)
    plt.show()

main()
