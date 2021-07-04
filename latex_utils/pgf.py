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
        err = sum([get_error(data_red[-1], d, data[i+1], sfac) for d in data[i_saved:(i+1)]])
        if err > tol:
            data_red.append(data[i])
            i_saved = i
    data_red.append(data[-1])
    
    return np.array(data_red)


def get_error(d0, di, d1, sfac):
    # Calculate error of point di when interpolating between d0 and d1.
    # Scale each coordinate by corresponding element in sfac 
    
    # Get scaled vectors
    vi = (di - d0)/sfac
    v1 = (d1 - d0)/sfac
    
    # Determine error vectors
    v1hat = v1/np.linalg.norm(v1)
    s = np.dot(vi, v1hat) * v1hat
    e = vi - s
    
    return np.linalg.norm(e)