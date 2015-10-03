from prime_number import is_prime
import itertools
import numpy as np
import ipdb
from scipy.spatial.distance import pdist, squareform




def contains_duplicate(x):
    """Check if two elements of a list are identical"""
    return len(set(x)) != len(x)


def unique_digit(n):
    """Check if n contains unique digits"""
    list_numbers = list(str(n))
    result = False if contains_duplicate(list_numbers) else True
    return result


def int_permutations(n, ndigits=4):
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

    permutations = np.array(sorted(int_permutations(n))) #sorted list of all permutations
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


def central_point(distances):
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
        is_equidistant = np.array(occurences) == 2 #check if the point is equidistant between two other numbers
        if any(is_equidistant):
            return c, unique_distances[is_equidistant]

    return -1, 0 #default return





ndigits = 4
for n in xrange(10**(ndigits-1),10**ndigits):
    if not unique_digit(n) or not is_prime(n):
        continue
    else:
        permutations = keep_prime(int_permutations(n, ndigits)) #remove non prime numbers
        if len(permutations) < 3: #reject if number of combinations is too low
            continue
        else:
            distances = distance_matrix(permutations)
            index, edist = central_point(distances)
            if index == 2:
                print n, index, edist


            

        


















