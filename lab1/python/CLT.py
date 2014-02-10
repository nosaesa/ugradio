from pylab import *
N = 1000
samples = np.zeros(6*N+1)
for j in range(10*N):
	accum = 0
	for i in range(N):
		roll = randint(1,7)
		accum = accum + roll
	samples[accum] = samples[accum] + accum
samples = samples/max(samples)
mean = 3.5
variance = 35/12
stddev = sqrt(variance)
n = arange(0,6*N+1)
y = mlab.normpdf(n,N*mean,sqrt(N)*stddev)
y = y/max(y)
plot(samples,label='Average of 1000 die rolls')
plot(n,y,'r--',linewidth=3,label='Normal Distribution')
xlim(3000,4000)
xlabel('Value')
ylabel('Normalized Frequency')
legend()
show()
