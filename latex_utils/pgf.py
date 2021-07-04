import sys
import numpy as np


def reduce_datafile(filename, tol):
    """ Reduce the number of datapoints in a datafile for pgf plot. 
    Datapoints that can be removed without having introducing an
    relative error larger than tol. The relative error is measured by 
    scaling the data to span [0, 0] to [1,1].
    
    All columns in `filename` are accounted in the error
    
    :param filename: Path to the data file for which the data should be reduced.
    :type filename: str
    
    :param tol: Tolerance below which datapoints are removed
    :type tol: float
    
    :return: None
    """
    data = np.loadtxt(filename)
    data_red = reduce_data(data, tol)
    filename_red = ".".join(filename.split(".")[:-1]) + '_red.' + filename.split(".")[-1]
    red = 100*len(data_red)/len(data)
    print("Data reduced to {:0.2f} % of original".format(red))
    print("Saving reduced data to {:s}".format(filename_red))
    np.savetxt(filename_red, data_red)


def reduce_data(data, tol):
    data_red = []
    data_red.append(data[0])
    i_saved = 0
    sfac = np.array([d[-1] - d[0] for d in np.transpose(data)])
    for i in range(1,data.shape[0]-1):
        err = get_error(data_red[-1], data[i_saved:(i+1)], data[i+1], sfac)
        if err > tol:
            data_red.append(data[i])
            i_saved = i
    data_red.append(data[-1])
    
    return np.array(data_red)


def get_error(p0, pts, p1, sfac):
    """ Calculate position error of pts when interpolating between p0 and p1.

    :param p0: Coordinates of first point (length=dim)
    :type p0: np.array

    :param pts: Coordinates of intermediate points, (shape = (npts, dim))
    :type pts: np.array

    :param p1: Coordinates of second point (length=dim)
    :type p1: np.array

    :param sfac: Scaling factor for each dimension (length=dim)
    :type sfac: np.array

    :return: max error
    :rtype: float

    """
    #
    # Scale each coordinate by corresponding element in sfac 
    
    # Get scaled vectors
    v1 = (p1 - p0)/sfac
    v1hat = v1 / np.linalg.norm(v1)

    # Vector from p0 to pts
    vis = np.array([(pi - p0) / sfac for pi in pts])

    # Error vectors
    error_vectors = np.outer(vis @ v1hat, v1hat) - vis

    # Return max error vector
    return np.max([np.linalg.norm(ev) for ev in error_vectors])
