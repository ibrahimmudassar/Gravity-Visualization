# Gravity-Visualization

This work seeks to visualize the work done by Hirt et al. (2019).
The Readme for their research is [here.](https://ddfe.curtin.edu.au/models/SRTM2gravity2018/SRTM2gravity_Readme.dat)

This project initially started by perusing the 

# Output
## After
![3D Model of Gravity](/images/3dGravity.png)
![2D Model of Gravity](/images/2dGravity.png)
## Before
![Old 2D Model of Gravity](https://ddfe.curtin.edu.au/models/SRTM2gravity2018/data/FullScaleGravity/N00E060/N11E077_full.png)

# How To Use
Please type in the specific location you want and it will show a 3d Histogram and 2d Histogram with your results.

Currently it can only handle one binary file at one time, and will only work predictably in the North Eastern hemisphere of the Earth. This is a top priority todo list item

# TODO
* Type in a latitude and longitude and it outputs automatically (if available) without searching for the link. In lieu of this, you may type the link by modifying the code. [All possible links are here.](/filenames.txt)
* The ability to input a square and it will concatenate the files together and output the concatenated data
* Create Interactive Globe Model of this to try to imitate the [gravity potato](https://user-images.githubusercontent.com/22484328/223882296-e0e7e285-f51d-4bbb-9c21-b056ce6c29e6.png)


# Thanks
I want to thank (in no particular order):
* Cornelia Freund, Technical University Munich
* Dr. Christian Hirt, Technical University Munich
* Dr. Michael Kuhn, Curtin University
* Dr. John Ries, UT Austin
* Brian Meyer, NOAA

Without you, this project would have gone far more frustratingly
