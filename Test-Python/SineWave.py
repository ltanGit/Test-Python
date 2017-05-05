import matplotlib.pyplot as plt
import numpy as np

def main():
    Lambda = input('lambda is:')
    Lambda = float(Lambda)
    MySineWave(Lambda)

def MySineWave(Lambda):
    pi = np.pi
    x = np.arange(-2*pi, 2*pi, 0.1)
    k = 2*pi/Lambda
    y = np.sin(k*x)
    plt.plot(x, y, 'r-',markersize = 2)
    plt.xlabel('Position', fontsize=12)
    plt.ylabel('Amplitude', fontsize=12)
    plt.title('Sine Wave with Wavelength = %s' % Lambda)
    plt.show()

main()
