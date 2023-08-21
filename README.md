# Text guided generation and manipulation of human face image

Project Abstract :

Generating human face images from textual descriptions is a challenging task that requires the ability to understand both the textual input and the visual characteristics of human faces. This work proposes a method for generating human face images from textual descriptions using the StyleGAN architecture. This approach uses a text-to-image generation module to map textual descriptions to the latent space of the StyleGAN model to generate images of human faces that match the given textual input. This text-to-image module is trained using a dataset of textual descriptions and human faces pairs. To manipulate the real world images, we use GAN inversion to obtain the latent code of  the image and manipulate the latent code. The latent directions for various facial attributes are learnt and used to manipulate the given image based upon the textual description.


Dataset :
The dataset is collected from two sources

https://github.com/ziqihuangg/CelebA-Dialog

This dataset contains 30000 high resolution images of human faces
Each image is of size 1024*1024
This dataset also contains binary labels for 40 facial features corresponding to 30000 images of CelebAMask-HQ

https://github.com/IIGROUP/MM-CelebA-HQ-Dataset

The textual description of the CelebAMask-HQ images  generated as a part of the above work are being used in this project


Pretrained Networks :

https://github.com/NVlabs/stylegan2
