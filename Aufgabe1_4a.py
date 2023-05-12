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

I=(1.,2.)
UAa=(125.,150.,175.,200.,225.,250.)
da =(8.7,9.9,10.7,11.8,13.1,14.3)
UAb=(100.,125.,150.,175.,200.,225.,250.)
db =(4.3,4.6,4.7,5.8,5.9,6.5,6.6)

xdataA=UAa
xdataB=UAb

ydataA=np.zeros(6)
ydataB=np.zeros(7)
i=0
j=0

while i<6:
    ydataA[i]=da[i]**2
    i=i+1

while j<7:
    ydataB[j]=db[j]**2
    j=j+1

yer=0.00000001

def generate_datasets(output_file_path1,output_file_path2):
    '''The following block generates the Datasets and writes a file for
    each of them.'''

    import numpy as np  # need some functions from numpy

    my_datasets = []


    my_datasets.append(kafe.Dataset(data=(xdataA, ydataA)))
    my_datasets[-1].add_error_source('y', 'simple', yer)
    
    my_datasets.append(kafe.Dataset(data=(xdataB, ydataB)))
    my_datasets[-1].add_error_source('y', 'simple', yer)
    
    my_datasets[0].write_formatted(output_file_path1)
    my_datasets[1].write_formatted(output_file_path2)    

############
# Workflow #
############

# Generate the Dataseta and store them in files

generate_datasets('dataseta1.dat',
                  'dataseta2.dat')

# Initialize the Datasets
my_datasets = [kafe.Dataset(title="I=1.0A"),
               kafe.Dataset(title="I=2.0A")]

# Load the Datasets from files
my_datasets[0].read_from_file(input_file='dataseta1.dat')
my_datasets[1].read_from_file(input_file='dataseta2.dat')
# Create the Fits
my_fits = [kafe.Fit(dataset,
                    linear_2par,
                    fit_label="Ausgleichsgerade" )
           for dataset in my_datasets]

# Do the Fits
for fit in my_fits:
    fit.do_fit()

# Create the plots
my_plot = kafe.Plot(my_fits[0],my_fits[1])

mnA  = my_fits[0].get_parameter_values(rounding=False)
mnB  = my_fits[1].get_parameter_values(rounding=False)


mnA=np.around(mnA[0], decimals=3)
mnB=np.around(mnB[0], decimals=3)

my_plot.axes.annotate(r'$m_{I=1.0A}= \  $' + str(mnA), xy=(90, 182), size=15, ha='left')
my_plot.axes.annotate(r'$m_{I=2.0A}= \  $' + str(mnB), xy=(90, 192), size=15, ha='left')

my_plot.axis_labels = [r'$ U_A \ in \ V$', r'$ d^2 \ in \ cm^2 $']


# Draw the plots
my_plot.plot_all(show_info_for=None, show_data_for='all', show_function_for='all', show_band_for='meaningful')


###############
# Plot output #
###############

# Save the plots
#my_plot.save('Aufgabeem1_4a.pdf')




# Show the plots
my_plot.show()
