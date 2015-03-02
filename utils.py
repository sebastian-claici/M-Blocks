import math
import numpy as np
import sys

def sgn(x):
    """Return the sign of x.
    """
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

def dot(v1, v2):
    """Return the dot product between two vectors.
    """
    return sum(x * y for x, y in zip(v1, v2))

def length(v):
    """Return the length of a vector under the Euclidean norm.
    """
    return math.sqrt(dot(v, v))

def angle(v1, v2):
    """Return the angle between two vectors.
    """
    l1, l2 = length(v1), length(v2)
    v1 = [x / l1 for x in v1]
    v2 = [x / l2 for x in v2]

    d = dot(v1, v2)
    return math.acos(d)

def rotate(v, theta):
    """Rotate vector v by theta degrees.
    """
    rot = np.array([[np.cos(theta), np.sin(theta)],
                       [-np.sin(theta), np.cos(theta)]])
    vec = np.array(v)
    res = dot(rot, vec)
    print res
    res[np.absolute(res) < 1e-8] = 0
    print res

    return res.tolist()


def query_yes_no(question, default="yes"):
    """ Ask a yes/no question and return True/False. """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}

    if default is None:
        prompt = " [y/n]: "
    elif default == "yes":
        prompt = " [Y/n]: "
    elif default == "no":
        prompt = " [y/N]: "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
