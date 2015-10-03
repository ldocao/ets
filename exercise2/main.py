from prime_number import is_prime
import itertools
import numpy as np
import ipdb
from scipy.spatial.distance import pdist, squareform

NDIGITS = 4
NO_MATCH = -1
KNOWN_MATCH = [1487,4817,8147]
SEPARATION = 3330



def contains_duplicate(x):
    """Check if two elements of a list are identical"""
    return len(set(x)) != len(x)


def unique_digit(n):
    """Check if n contains unique digits"""
    list_numbers = list(str(n))
    result = False if contains_duplicate(list_numbers) else True
    return result


def int_permutations(n, ndigits=NDIGITS):
    """Return a list of all permutations as int of 4 digits"""
    list_numbers = map(int, str(n)) #get list of digits
    permutations_tuple = itertools.permutations(list_numbers, ndigits)
    permutations = np.array([int("".join(map(str,s))) for s in permutations_tuple]) #convert to int
    permutations = permutations[permutations >= 1000] #remove 3-digits numbers
    return permutations


def contains_non_prime(l):
    """Check if the list contains non prime number"""
    non_primality = [np.logical_not(is_prime(i)) for i in l]
    return np.sum(non_primality) >= 1


def permutation_has_been_seen(n , already_seen):
    """Check if a permutation of n has been seen before"""
    return any(i in already_seen for i in int_permutations(n))


def keep_prime(l):
    """Return a list keeping only prime numbers"""

    permutations = np.array(int_permutations(n)) #sorted list of all permutations
    is_prime_number = np.array([is_prime(m) for m in permutations])
    return permutations[is_prime_number]


def difference_elements(t):
    """Return the difference between the list elements"""
    return [j-i for i, j in zip(t[:-1], t[1:])]


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


def check_distance_value(edist):
    """Check if the distance is the expected value"""

    if edist != SEPARATION: #check if the distance is the expected value
        raise ValueError("Distance are supposed to be equal", edist, SEPARATION)

    return None

def triple_equidistant(permutations):
    """Return a triple of equidistant points among the list

    Parameters:
    ----------
    permutations: list
        list of all permutations for a given set of digits
    """

    distances = distance_matrix(permutations)
    icenter, edist = equidistant_point(distances)
    if icenter != NO_MATCH:
        check_distance_value(edist)
        center = permutations[icenter]
        left = center - SEPARATION
        right = center + SEPARATION
        return left, center, right
    else:
        return NO_MATCH



def range_values(x):
    """Return the range of values"""

    try:
        return np.max(permutations) - np.min(permutations)
    except ValueError:
        return 0


for n in xrange(10**(NDIGITS-1),10**NDIGITS):
    if not unique_digit(n): #easy discard
        continue
    else:
        permutations = keep_prime(int_permutations(n)) #remove non prime numbers among permutations
        max_diff = range_values(permutations)
        if len(permutations) < 3 or max_diff < SEPARATION*2:
            continue
        else:
            distances = distance_matrix(permutations)
            a,b = equidistant_point(distances)
            if a != NO_MATCH:
                print n,a,b
            #results = triple_equidistant(permutations)
            #print n, permutations, results  
            #if results != NO_MATCH:
            #    print results




            

        




















