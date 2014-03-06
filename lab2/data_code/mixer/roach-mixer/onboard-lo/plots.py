from numpy import *
from matplotlib.pyplot import *

close('all')

x = load('onboard-lo-1-numeric.npz')
xcos = x['arr_2']
xsin = x['arr_3']
XCOS = fft.fft(xcos)
XSIN = fft.fft(xsin)
XR = XCOS + 1j*XSIN
xr = fft.ifft(XR)

subplot(2,1,1)
xrz = xr[0:1000]
n = linspace(0,50,len(xrz))
plot(n,real(xrz)/max(real(xrz)),'g',label='Real')
plot(n,imag(xrz)/max(imag(xrz)),'r',label='Imaginary')
title('Reconstructed SSB Mixer Output')
xlabel('t [us]')
ylabel('Volts')
legend()

subplot(2,1,2)
XRf = XR
XRf[20:] = 0
xrf = fft.ifft(XRf)
n = linspace(0,50,len(xrf))
plot(n,real(xrf)/max(real(xrf)))
title('Filtered SSB Mixer Output')
xlabel('t [us]')
ylabel('Volts')

show()