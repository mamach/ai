import torch

random_tensor = torch.rand(size=(3,4))
print(random_tensor)

# create a random tensor of size 224,224, 3
random_image_size_tensor = torch.rand(size=(224,224, 3))
print('shape ', random_image_size_tensor.shape)
print('ndim ', random_image_size_tensor.ndim)

