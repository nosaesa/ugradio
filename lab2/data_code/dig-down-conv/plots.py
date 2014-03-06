from numpy import *
from matplotlib.pyplot import *

close('all')

X = array([1,1,1,0,0,0,1,1])
x = fft.ifft(X)
xn = append(x,zeros(56))
Xn = fft.fft(xn)
w = linspace(-pi,pi,64)
plot(w,abs(fft.fftshift(Xn)),'b',label='Computed')

Xi = zeros(64)
Xi[16:49] = 1
plot(w,Xi,'g',label='Ideal')

filter = zeros(64)
for i in range(2,8) :
	file = 'ddc-lo-'+str(i)+'-numeric.npz'
	x = load(file)
	input = x['arr_2']
	output = x['arr_1']
	filter[pow(2,(i-2))] = sqrt(mean(square(output)))/sqrt(mean(square(input)))
	filter[64 - pow(2,(i-2))] = filter[pow(2,(i-2))]
stem(w,abs(fft.fftshift(filter)),'r',label='Measured')
legend()
title('FIR Low-Pass Filter')
xlabel('$\omega$ [rad/s]')
ylabel('$|H(\omega)|$')
show()
savez('lpf.npz',fft.fftshift(filter))