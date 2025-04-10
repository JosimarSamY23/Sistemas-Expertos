# Filtro de Kalman 
def update(mean1, var1, mean2, var2):
	new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
	new_var = 1./(1./var1 + 1./var2)
	return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
	new_mean = mean1 + mean2
	new_var = var1 + var2
	return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000

# print out ONLY the final values of the mean
# although for a better understanding you may choose to 
# and the variance in a list [mu, sig]. 

for measurement, motion in zip(measurements, motion):
	mu, sig = update(measurement, measurement_sig, mu, sig)
	mu, sig = predict(motion, motion_sig, mu, sig)
print([mu, sig])