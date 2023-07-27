# Bike Price-Prediction


This is a personal project finished as a 2 member group-project for university.

1. Web-Crawling of (bicycle-img, offer-price) mapping, 60000k images
2. Cleanup and analysis
3. "Proof of concept" ResNet50 & Robust Model using MAPE (Mean Absolute Percentage Error)
4. Visualization using GradCam
4. Interested in the tensorflow model? Please contact me :)


Results: From PowerPoint slides, the actuall notebook "BikePricePrediction" is of course more detailed but also contains university requirements (preliminaries etc.):
![Slide ](PowerPoint/img/Slide31.PNG)

![Slide ](PowerPoint/img/Slide34.PNG)
![Slide ](PowerPoint/img/Slide35.PNG)


Below is the full presentation with a high level overview over the project.
- [Table of Content](#my-powerpoint-slides)

  - [1. Problem formulation](#slide-3)
  - [2. Crawling](#slide-5)

  - [3. Filtering and cleaning](#slide-6)
  - [3.1. Filtering out non-bicycle images using ResNet(ImageNet) embeddings](#slide-7)

  - [3.2. Filter out remaining unwated images](#slide-13)

  - [3.3. Remove duplicate images](#slide-18)
  - [3.4. Is there bias?](#slide-19)

  - [3.5. Preprocessing ](#slide-23)
  - [3.5 Mean Image](#slide-24)
  - [3.5 Data Split](#slide-25)
  - [4. Loss Function](#slide-26)

  - [5. Baseline Model](#slide-28)
  - [5. "Finetuned" Model](#slide-29)

  - [5. Robust Model](#slide-32)
  - [5. Recap: "Is there bias in the data?"](#slide-33)
  - [5. GradCam Feature Map visualization](#slide-34)



![Slide 1](PowerPoint/img/Slide1.PNG)

![Slide 2](PowerPoint/img/Slide2.PNG)

![Slide 3](PowerPoint/img/Slide3.PNG)

![Slide 4](PowerPoint/img/Slide4.PNG)

![Slide 5](PowerPoint/img/Slide5.PNG)

![Slide 6](PowerPoint/img/Slide6.PNG)

![Slide 7](PowerPoint/img/Slide7.PNG)

![Slide 8](PowerPoint/img/Slide8.PNG)

![Slide 9](PowerPoint/img/Slide9.PNG)

![Slide 10](PowerPoint/img/Slide10.PNG)

![Slide 11](PowerPoint/img/Slide11.PNG)

![Slide 12](PowerPoint/img/Slide12.PNG)

![Slide 13](PowerPoint/img/Slide13.PNG)

![Slide 14](PowerPoint/img/Slide14.PNG)

![Slide 15](PowerPoint/img/Slide15.PNG)

![Slide 16](PowerPoint/img/Slide16.PNG)

![Slide 17](PowerPoint/img/Slide17.PNG)

![Slide 18](PowerPoint/img/Slide18.PNG)

![Slide 19](PowerPoint/img/Slide19.PNG)

![Slide 20](PowerPoint/img/Slide20.PNG)

![Slide 21](PowerPoint/img/Slide21.PNG)

![Slide 22](PowerPoint/img/Slide22.PNG)

![Slide 23](PowerPoint/img/Slide23.PNG)

![Slide 24](PowerPoint/img/Slide24.PNG)

![Slide 25](PowerPoint/img/Slide25.PNG)

![Slide 26](PowerPoint/img/Slide26.PNG)

![Slide 27](PowerPoint/img/Slide27.PNG)

![Slide 28](PowerPoint/img/Slide28.PNG)

![Slide 29](PowerPoint/img/Slide29.PNG)

![Slide 30](PowerPoint/img/Slide30.PNG)

![Slide 31](PowerPoint/img/Slide31.PNG)

![Slide 32](PowerPoint/img/Slide32.PNG)

![Slide 33](PowerPoint/img/Slide33.PNG)

![Slide 34](PowerPoint/img/Slide34.PNG)

![Slide 35](PowerPoint/img/Slide35.PNG)

![Slide 36](PowerPoint/img/Slide36.PNG)