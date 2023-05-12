'''
A Tale of Two Fits
------------------

    This simple example demonstrates the fitting of a linear function to
    two Datasets and plots both Fits into the same Plot.
'''

###########
# Imports #
###########

# import everything we need from kafe
import kafe
from kafe import ASCII, LaTeX, FitFunction
# additionally, import the model function we
# want to fit:
from kafe.function_library import linear_2par
import numpy as np

####################
# Helper functions #
####################

# -- define test configuration 

UA=(200,250,300,350,400,450,500,550,600,650,700)
IS=(0.173,0.191,0.215,0.233,0.248,0.264,0.278,0.288,0.304,0.316,0.323)

xdata=np.zeros(11)
i=0
while i<11:
    xdata[i]=IS[i]**2
    i=i+1

yer=0.0000001

def generate_datasets(output_file_path1):
    '''The following block generates the Datasets and writes a file for
    each of them.'''

    import numpy as np  # need some functions from numpy

    my_datasets = []


    my_datasets.append(kafe.Dataset(data=(xdata, UA)))
    my_datasets[-1].add_error_source('x', 'simple', yer)
    
    my_datasets[0].write_formatted(output_file_path1)
    

############
# Workflow #
############

# Generate the Dataseta and store them in files

generate_datasets('dataset2A.dat')

# Initialize the Datasets
my_datasets = [kafe.Dataset(title=r'$U_A$')]

# Load the Datasets from files
my_datasets[0].read_from_file(input_file='dataset2A.dat')
# Create the Fits
my_fits = [kafe.Fit(dataset,
                    linear_2par,
                    fit_label="Ausgleichsgerade" )
           for dataset in my_datasets]

# Do the Fits
for fit in my_fits:
    fit.do_fit()

# Create the plots
my_plot = kafe.Plot(my_fits[0])

mn  = my_fits[0].get_parameter_values(rounding=False)



mn=np.around(mn[0], decimals=3)

my_plot.axes.annotate(r'$m_{}= \ $' + str(mn), xy=(0.025, 680), size=14, ha='left')

my_plot.axis_labels = [r'$I^2 \ in \ A^2$', r'$ U_A \ in \ V $']


# Draw the plots
my_plot.plot_all(show_info_for=None, show_data_for='all', show_function_for='all', show_band_for='meaningful')


###############
# Plot output #
###############

# Save the plots
my_plot.save('Aufgabeem2.pdf')




# Show the plots
#my_plot.show()
