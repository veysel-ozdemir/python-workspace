import torch

print(torch.backends.mps.is_available(), torch.backends.mps.is_built())
x = torch.rand(5, 3)
print(x)