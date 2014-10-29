This python script generates hkl files for use with the Rfree refinement concept.
Inital 'xd.hkl' is divided into a number of batches which has to be input by user.
The given xd.hkl is read in and data points are randomly selected. 
The Batches are tuned to store roughly equal amounts of data points.
Output is written to three files for each set:
       xdfreeXX.hkl with XX being the batch number
       xdworkXX.hkl
       shelxXX.hkl
Use shelxXX.hkl for starting model generation, xdworkXX.hkl for refinement and xdfreeXX.hkl for Rfree procedure