# Bike Price-Prediction


This is a personal project finished as a 2 member group-project for university. The project is inspired by [Stanford CS229: Machine Learning Course, Lecture 1 - Andrew Ng (Autumn 2018)](https://www.youtube.com/watch?v=jGwO_UgTS7I), where one instructor mentions a similar project done by students.

1. Web-Crawling of (bicycle-img, offer-price) mapping, 60000k images
2. Cleanup and analysis
3. "Proof of concept" ResNet50 & Robust Model using MAPE (Mean Absolute Percentage Error)
4. Visualization using GradCam
4. Interested in the tensorflow model or clean dataset? Please contact me :)


Results: From PowerPoint slides, the actual notebook "BikePricePrediction" is of course more detailed but also contains university requirements (preliminaries etc.):
![Slide ](PowerPoint/img/Slide32.PNG)

![Slide ](PowerPoint/img/Slide35.PNG)
![Slide ](PowerPoint/img/Slide36.PNG)


Below is the full presentation with a high level overview over the project.
- [Table of Content](#my-powerpoint-slides)

  - [1. Problem formulation](#slide-3)
  - [2. Crawling](#slide-4)

  - [3. Filtering and cleaning](#slide-5)
  - [3.1. Filtering out non-bicycle images using ResNet(ImageNet) embeddings](#slide-7)

  - [3.2. Filter out remaining unwated images](#slide-13)

  - [3.3. Remove duplicate images](#slide-16)
  - [3.4. Is there bias?](#slide-17)

  - [3.5. Preprocessing ](#slide-21)
  - [3.5 Mean Image](#slide-22)
  - [3.5 Data Split](#slide-23)
  - [4. Loss Function](#slide-26)

  - [5. Baseline Model](#slide-28)
  - [5. "Finetuned" Model](#slide-29)

  - [5. Robust Model](#slide-32)
  - [5. Recap: "Is there bias in the data?"](#slide-33)
  - [6. GradCam Feature Map visualization](#slide-34)



## <a id="slide-1"></a>

![Slide 1](PowerPoint/img/Slide1.PNG)

## <a id="slide-2"></a>

![Slide 2](PowerPoint/img/Slide2.PNG)

## <a id="slide-3"></a>

![Slide 3](PowerPoint/img/Slide3.PNG)

## <a id="slide-4"></a>

![Slide 4](PowerPoint/img/Slide4.PNG)

## <a id="slide-5"></a>

![Slide 5](PowerPoint/img/Slide5.PNG)

## <a id="slide-6"></a>

![Slide 6](PowerPoint/img/Slide6.PNG)

## <a id="slide-7"></a>

![Slide 7](PowerPoint/img/Slide7.PNG)

## <a id="slide-8"></a>

![Slide 8](PowerPoint/img/Slide8.PNG)

## <a id="slide-9"></a>

![Slide 9](PowerPoint/img/Slide9.PNG)

## <a id="slide-10"></a>

![Slide 10](PowerPoint/img/Slide10.PNG)

## <a id="slide-11"></a>

![Slide 11](PowerPoint/img/Slide11.PNG)

## <a id="slide-12"></a>

![Slide 12](PowerPoint/img/Slide12.PNG)

## <a id="slide-13"></a>

![Slide 13](PowerPoint/img/Slide13.PNG)

## <a id="slide-14"></a>

![Slide 14](PowerPoint/img/Slide14.PNG)

## <a id="slide-15"></a>

![Slide 15](PowerPoint/img/Slide15.PNG)

## <a id="slide-16"></a>

![Slide 16](PowerPoint/img/Slide16.PNG)

## <a id="slide-17"></a>

![Slide 17](PowerPoint/img/Slide17.PNG)

## <a id="slide-18"></a>

![Slide 18](PowerPoint/img/Slide18.PNG)

## <a id="slide-19"></a>

![Slide 19](PowerPoint/img/Slide19.PNG)

## <a id="slide-20"></a>

![Slide 20](PowerPoint/img/Slide20.PNG)

## <a id="slide-21"></a>

![Slide 21](PowerPoint/img/Slide21.PNG)

## <a id="slide-22"></a>

![Slide 22](PowerPoint/img/Slide22.PNG)

## <a id="slide-23"></a>

![Slide 23](PowerPoint/img/Slide23.PNG)

## <a id="slide-24"></a>

![Slide 24](PowerPoint/img/Slide24.PNG)

## <a id="slide-25"></a>

![Slide 25](PowerPoint/img/Slide25.PNG)

## <a id="slide-26"></a>

![Slide 26](PowerPoint/img/Slide26.PNG)

## <a id="slide-27"></a>

![Slide 27](PowerPoint/img/Slide27.PNG)

## <a id="slide-28"></a>

![Slide 28](PowerPoint/img/Slide28.PNG)

## <a id="slide-29"></a>

![Slide 29](PowerPoint/img/Slide29.PNG)

## <a id="slide-30"></a>

![Slide 30](PowerPoint/img/Slide30.PNG)

## <a id="slide-31"></a>

![Slide 31](PowerPoint/img/Slide31.PNG)

## <a id="slide-32"></a>

![Slide 32](PowerPoint/img/Slide32.PNG)

## <a id="slide-33"></a>

![Slide 33](PowerPoint/img/Slide33.PNG)

## <a id="slide-34"></a>

![Slide 34](PowerPoint/img/Slide34.PNG)

## <a id="slide-35"></a>

![Slide 35](PowerPoint/img/Slide35.PNG)

## <a id="slide-36"></a>

![Slide 36](PowerPoint/img/Slide36.PNG)
