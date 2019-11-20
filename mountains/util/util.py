import country
from col import Col

def andorran_col(name, height, length = None, average_gradient = None, maximum_gradient = None):
    return Col(name, country.Andorra(), height, length, average_gradient, maximum_gradient)

def french_col(name, height, length = None, average_gradient = None, maximum_gradient = None):
    return Col(name, country.France(), height, length, average_gradient, maximum_gradient)

def italian_col(name, height, length = None, average_gradient = None, maximum_gradient = None):
    return Col(name, country.Italy(), height, length, average_gradient, maximum_gradient)

def spanish_col(name, height, length = None, average_gradient = None, maximum_gradient = None):
    return Col(name, country.Spain(), height, length, average_gradient, maximum_gradient)

def swiss_col(name, height, length = None, average_gradient = None, maximum_gradient = None):
    return Col(name, country.Switzerland(), height, length, average_gradient, maximum_gradient)
