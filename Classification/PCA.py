import numpy as np
from fractions import Fraction

X = [(2,2), (4,4), (1,5), (5,1)]
L = len(X[0])
K = 1
pt_count = len(X)

output_md = ''


# step 1
X = [tuple(map(lambda x: Fraction(x,1), x)) for x in X]
X = list(map(np.array, X))
X_mean = sum(X)/pt_count
X_prime = [x - X_mean for x in X]

print("mean", X_mean)
for x, x_prime in zip(X, X_prime):
    print("X", x)
    print("X_prime", x_prime)

# step 2
X_reshaped = [x.reshape(2,1) for x in X_prime]
X_big = np.concatenate(X_reshaped, axis=1)
covar = X_big @ X_big.T / pt_count

print("Y", X_big)
print("covar", covar)

# Step 3
def npmap(func, array):
    try:
        my_list = list(array)
        if type(my_list[0]) == np.ndarray:
            my_list = list(map(lambda x: npmap(func, x), my_list))
        else:
            my_list = list(map(func, my_list))
        return np.array(my_list)
    except Exception as e:
        print(e)
        return func(array)

einvalues, einvectors = np.linalg.eig(npmap(float, covar))
einvalues = npmap(lambda x: Fraction(x).limit_denominator(1000), einvalues)
print("einvalues", einvalues)
print("einvectors", einvectors)

einvecs = []
for i, value in enumerate(einvalues):
    vec = einvectors[:, i]
    einvecs.append(vec)
    x2_ratio = Fraction(vec[0]/vec[1]).limit_denominator(10000)
    minus_matrix = npmap(Fraction, covar-value*np.identity(2))

einvec_sorted = [x for _, x in sorted(zip(list(einvalues), list(einvecs)))][::-1]
einvec_sorted = [x.reshape(2, 1) for x in einvec_sorted]
phi = np.concatenate(einvec_sorted, axis=1)
print("phi", phi)

Y = []
for x, x_prime in zip(X, X_prime):
    y = (phi.T @ x)
    Y.append(y)
    print("X", x)
    print("Y", y)
    
Y_mean = sum(Y)/pt_count
Y_prime = [y - Y_mean for y in Y]
print("y_mean", Y_mean)
for x, x_prime in zip(X, Y_prime):
    print("x", x)
    print("y'", x_prime)










