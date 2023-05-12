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

I=(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8)


n=750.
l=0.3
i=0
B=np.zeros(8)
while i<7:
    B[i]=4.*np.pi*10**(-7)*(n/l)*I[i]
    i=i+1
print B

xdataB=B
ydataUA=(5,9,12,16,20,23,27,30)
#ydataUA=(5e-05,9e-05,12e-05,16e-05,20e-05,23e-05,27e-05,30e-05)


yer=0.00000001

def generate_datasets(output_file_path1):
    '''The following block generates the Datasets and writes a file for
    each of them.'''

    import numpy as np  # need some functions from numpy

    my_datasets = []


    my_datasets.append(kafe.Dataset(data=(xdataB, ydataUA)))
    my_datasets[-1].add_error_source('y', 'simple', yer)
    
    my_datasets[0].write_formatted(output_file_path1)
    

############
# Workflow #
############

# Generate the Dataseta and store them in files

#generate_datasets('datasetUB.dat')

# Initialize the Datasets
my_datasets = [kafe.Dataset(title=r'$U_H$')]

# Load the Datasets from files
my_datasets[0].read_from_file(input_file='datasetUB.dat')
# Create the Fits
my_fits = [kafe.Fit(dataset,
                    linear_2par,
                    fit_label="Eichgerade" )
           for dataset in my_datasets]

# Do the Fits
for fit in my_fits:
    fit.do_fit()

# Create the plots
my_plot = kafe.Plot(my_fits[0])

mnUB  = my_fits[0].get_parameter_values(rounding=False)



mnUB=np.around(mnUB[0], decimals=3)

my_plot.axes.annotate(r'$m_{eich}= \ $' + str(mnUB), xy=(1.4, 2.7), size=14, ha='left')

my_plot.axis_labels = [r'$B \ in \ 10^{-4}T$', r'$ U_H \ in \ 10^{-4}V $']


# Draw the plots
my_plot.plot_all(show_info_for=None, show_data_for='all', show_function_for='all', show_band_for='meaningful')


###############
# Plot output #
###############

# Save the plots
my_plot.save('Aufgabeem1_2.pdf')




# Show the plots
my_plot.show()
