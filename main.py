import random as rnd
#Dataset de forme [(x,y)]
dataset = [(-10.35, -41.7),
(-8.94,	-40.3),
(-7.61,	-44.3),
(-6.68,	-23.4),
(-6.05,	-28.8),
(-4.81,	-18.6),
(-4.06,	-13.9),
(-2.61,	-15.0),
(-2.17,	-18.4),
(-1.38,	-8.76),
(-0.09,	8.23),
(0.89,	-2.82),
(1.72,	3.99),
(3.35,	26.02),
(4.03,	26.68),
(4.75,	22.46),
(5.66,	23.49),
(7.04,	44.29),
(7.85,	41.37),
(9.12,	56.58),
(10.28,	51.72),
(10.69,	62.56),
(12.4,	54.82),
(12.96,	75.11),
(14.08,	70.79),
(14.81,	69.08),
(16.12,	82.39),
(16.95,	93.69),
(18.05,	91.61),
(18.99,	102.2)]

#CONSTANTES
NUMBER_PARAMS = 3
WANTED_PRECISION = 0.1
PROPAG_RATE = 0.0001
RANDOM_RANGE = (-5,5)

#VARIABLES
params = []

#STATS
iterations = 0

def model(x, params):
    a = params[0]
    b = params[1]
    result = a*x+b
    print(result)
    return result

def modelderiv(paramid, data, params): #Derivée de (ax² + bx + c - y)²
    a = params[0]
    b = params[1]
    c = params[2]
    x = data[0]
    y = data[1]
    if paramid == 0: #Par rapport à a:
        result = 2*x**2*(a*x**2 + b*x + c - y)
    elif paramid == 1: #Par rapport à b:
        result = 2*x*(a*x**2 + b*x + c - y)
    elif paramid == 2:
        result = 2*(a*x**2 + b*x + c - y)
    #print(a, b, x, result)
    return result

for paramid in range(NUMBER_PARAMS):
    params.append(rnd.randrange(RANDOM_RANGE[0], RANDOM_RANGE[1]))

done = False
while done == False:
    new_params = params
    done = True
    for paramid in range(NUMBER_PARAMS):
        iterations += 1
        deriv = sum([modelderiv(paramid, data, params) for data in dataset])
        print(deriv)
        if abs(deriv) > WANTED_PRECISION:
            done = False
            new_params[paramid] -= PROPAG_RATE/(2*len(dataset))*deriv
    params = new_params

print("Fin ! \n a = {}, b= {}, c={} \n Itérations : {}".format(params[0], params[1], params[2], iterations))
