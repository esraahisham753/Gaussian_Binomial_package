# Gaussian and Binomial distribution

## Installation
pip install essdistributions

## Gaussian Class:
### Attributes: 
* mean (float) representing the mean value of the distribution.
* stdev (float) representing the standard deviation of the distribution.
* data_list (list of floats) a list of floats extracted from the data file.
### Methods:
* __init__(self, mean=0, stdev=1)

* read_data_file(self, file_name)
Function to read in data from a txt file. The txt file should have
one number (float) per line. The numbers are stored in the data attribute.		
		Args:
			file_name (string): name of a file to read from		
		Returns:
			None

* calculate_mean(self)
Function to calculate the mean of the data set.		
		Args: 
			None
		
		Returns: 
			float: mean of the data set

* calculate_stdev(self, sample=True)
Function to calculate the standard deviation of the data set.		
		Args: 
			sample (bool): whether the data represents a sample or population	
		Returns: 
			float: standard deviation of the data set

* plot_histogram(self)
Function to output a histogram of the instance variable data using 
		matplotlib pyplot library.
		Args:
			None	
		Returns:
			None

* pdf(self, x)
Probability density function calculator for the gaussian distribution.
		Args:
			x (float): point for calculating the probability density function	
		Returns:
			float: probability density function output

* plot_histogram_pdf(self, n_spaces = 50)
Function to plot the normalized histogram of the data and a plot of the 
		probability density function along the same range
		Args:
			n_spaces (int): number of data points 
		Returns:
			list: x values for the pdf plot
			list: y values for the pdf plot

* __add__(self, other)
Function to add together two Gaussian distributions
		Args:
			other (Gaussian): Gaussian instance	
		Returns:
			Gaussian: Gaussian distribution

* __repr__(self)
Function to output the characteristics of the Gaussian instance
		Args:
			None
		Returns:
			string: characteristics of the Gaussian

## Binomial class
### Attributes
* mean (float) representing the mean value of the distribution.
* stdev (float) representing the standard deviation of the distribution.
* data_list (list of floats) a list of floats extracted from the data file.
* p (float) representing the probability of an event occurring
* n (int) the total number of trials

### Methods
* __init__(self, p=.5, n=20)

* calculate_mean(self):
Function to calculate the mean from p and n
Args: 
    None
Returns: 
    float: mean of the data set

* calculate_stdev(self):
Function to calculate the standard deviation from p and n.
Args: 
    None
Returns: 
    float: standard deviation of the data set

* replace_stats_with_data(self):    
Function to calculate p and n from the data set
Args: 
    None
Returns: 
    float: the p value
    float: the n value

* plot_bar(self):
Function to output a histogram of the instance variable data using 
matplotlib pyplot library.
Args:
    None   
Returns:
    None

* pdf(self, k):
Probability density function calculator for the gaussian distribution.
Args:
    k (float): point for calculating the probability density function
Returns:
    float: probability density function output

* plot_bar_pdf(self):
Function to plot the pdf of the binomial distribution
Args:
    None
Returns:
    list: x values for the pdf plot
    list: y values for the pdf plot

* __add__(self, other):        
Function to add together two Binomial distributions with equal p
Args:
    other (Binomial): Binomial instance
Returns:
    Binomial: Binomial distribution

* __repr__(self):    
Function to output the characteristics of the Binomial instance
Args:
    None
Returns:
    string: characteristics of the Gaussian





