# doubleSpikeMoPY
Python files used to process double spike data (here Mo).

This short Python program uses the inversion routine from Siebert et al 2003, to deconvolve double-spike data (here for Mo).
The code can easily be adjusted for other isotope systems. 

Spike and standard abudances are obtained from gravimetrically prepared solutions and inverse isotope dilution calibration of the 
two single spikes (as well as double spike) against NIST. Isotope spikes (92 and 98) were obtained from IsoFlex.

Analyses were performed on a Neptune MC-ICP-MS. 

The inversion routine returns alpha and beta - from which any required isotope ratio may be calculated (the program stores X/98 values by default).
Spike-to-sample props are also computed and all data are written to summary file, including some stats.


