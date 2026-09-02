import torch
float32_tensor = torch.tensor([3.0, 6.1, 9.4],
			     dtype=None, #defaults to torch.float32
			     device=None, #cpu, gpu
			     requires_grad=False)


print('shape', float32_tensor.shape)
print('dtype', float32_tensor.dtype)
print('device', float32_tensor.device)

