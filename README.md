# Image-Processor_using_Django
# Image Processor
![Screenshot (276)](https://user-images.githubusercontent.com/62831469/146632780-ed3a2df1-4048-4f4f-954b-d00ed0adf421.png)
![Screenshot (278)](https://user-images.githubusercontent.com/62831469/146632785-e2e2365e-d7ab-40f2-b95d-8bf6aa8a9175.png)


This Image Processor is fully developed in Django, with mainly 2 functionality 
* 1)In-Painting 
* 2)Color Filter

### What is In-Painting? 
* Inpainting is a conservation process where damaged, deteriorating, or missing parts of an artwork are filled in to present a complete image.
### What is Color Filter?
* Color image filtering and enhancement refer to the process of noise reduction in the color image and enhancement of the visual quality of the image input.
* We also observe the Importance of the RED|BLUE|GREEN color combination in real world.
* Color filtering a image is basically manipulation of RGB components.


## How In-Paint works?
There are 2 methods for In-Painting: -
#### 1) Fast Marching Method
* Algorithm starts from the boundary of this region and goes inside the region gradually filling everything in the boundary first. 
* It takes a small neighbourhood around the pixel on the neighbourhood to be inpainted. This pixel is replaced by normalized weighted sum of all the known pixels in the neighbourhood. 
* Selection of the weights is an important matter. More weightage is given to those pixels lying near to the point, near to the normal of the boundary and those lying on the boundary contours. 
* Once a pixel is inpainted, it moves to next nearest pixel using Fast Marching Method. FMM ensures those pixels near the known pixels are inpainted first, so that it just works like a manual heuristic operation.

#### 2) Navier-Stokes
* This algorithm is based on fluid dynamics and utilizes partial differential equations. Basic principle is heurisitic. 
* It first travels along the edges from known regions to unknown regions (because edges are meant to be continuous). 
* It continues isophotes (lines joining points with same intensity, just like contours joins points with same elevation) while matching gradient vectors at the boundary of the inpainting region. 
* For this, some methods from fluid dynamics are used. Once they are obtained, color is filled to reduce minimum variance in that area.
