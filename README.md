A MATH-356 final project exploring GANs.

The ``Toy Example`` folder contains source code and model weights for a simple GAN trained on the MNIST dataset (the generator model learned to generate handwritten digits).

The ``Full Example`` folder contains source code and model weights for a more complicated convolutional GAN trained on the CelebA dataset (the generator model learned to generate human faces). In order to be able to train this model in a reasonable amount of time, we did some preprocessing to downsize the images in the CelebA dataset to be 64x64. Then, we trained the GAN on those smaller CellebA images. 
