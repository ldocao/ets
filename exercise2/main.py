from prime_number import is_prime
import itertools
import numpy as np
import ipdb
from scipy.spatial.distance import pdist, squareform

NDIGITS = 4
NO_MATCH = -1
KNOWN_MATCH = [1487,4817,8147]
SEPARATION = 3330









def int_permutations(n, ndigits=NDIGITS):
    """Return a list of all permutations as int of 4 digits"""
    list_numbers = map(int, str(n)) #get list of digits
    permutations_tuple = itertools.permutations(list_numbers, ndigits)
    permutations = np.array([int("".join(map(str,s))) for s in permutations_tuple]) #convert to int
    permutations = permutations[permutations >= 1000] #remove 3-digits numbers
    return permutations


def keep_prime(l):
    """Return a list keeping only unique prime numbers"""

    permutations = np.array(int_permutations(n)) #sorted list of all permutations
    is_prime_number = np.array([is_prime(m) for m in permutations])
    return np.unique(permutations[is_prime_number])


def distance_matrix(X):
    """Compute a symmetric matrix of the difference between each elements"""
    d = [[x] for x in X]
    condensed = pdist(d)
    return squareform(condensed)


def equidistant_point(distances):
    """Return the index of an equidistant point, and the distance

    Parameters:
    ----------
    distances: np.array
        square matrix of distances between all permutations

    Output:
    ------
    c : int
        index in distances matrix of the central point

    distance: int
        distance of separation
    """

    size_distances = np.shape(distances)[0]
    for c in range(size_distances):
        unique_distances, occurences = np.unique(distances[:,c], return_counts=True)
        is_equidistant = np.array(occurences) >= 2 #check if the point is equidistant between two other numbers
        if any(is_equidistant):
            return c, unique_distances[is_equidistant]


    return NO_MATCH, 0 #default return


def triple_exists(permutations):
    """Return a triple of equidistant points among the list

    Parameters:
    ----------
    permutations: list
        list of all permutations for a given set of digits
    """

    if len(permutations) < 3:
        return False

    distances = distance_matrix(permutations)
    icenter, edist = equidistant_point(distances)
    if icenter != NO_MATCH:
        return True
    else:
        return False



def remove_known_matches(x):
    """Return the array after removing known matches

    Parameters:
    ----------
    x: list
    """
    for k in KNOWN_MATCH:
        try:
            x.remove(k)
        except ValueError:
            pass

    return x



for n in xrange(10**(NDIGITS-1),10**NDIGITS):
    permutations = keep_prime(int_permutations(n)) #remove non prime numbers among permutations
    permutations = remove_known_matches(list(permutations))
    if triple_exists(permutations):
        ipdb.set_trace()
        break #as soon as I find one, I can exit

results = 1
print results


            

        




















