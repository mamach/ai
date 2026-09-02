import torch

# 2D Data
MATRIX = torch.tensor([[1, 2, 0], 
		     [3, 4, 5]])

print(MATRIX)

print('shape ', MATRIX.shape)
print('ndim ', MATRIX.ndim)



# 3D Data
MATRIX2 =  torch.tensor([[[1, 2, 3],
			  [4, 5, 6], 
			  [7, 8, 9]]])
print('shape ', MATRIX2.shape)
print('ndim ', MATRIX2.ndim)
