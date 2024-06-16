import torch


class Softmax(torch.nn.Module):
    def forward(self, x: torch.Tensor):
        exp_x = torch.exp(x)
        return exp_x / exp_x.sum()


class softmax_stable(torch.nn.Module):
    def forward(self, x: torch.Tensor):
        exp_x = torch.exp(x - torch.max(x))
        return exp_x / exp_x.sum()


def ex1():
    data = torch.Tensor([1, 2, 3])
    softmax = Softmax()
    output = softmax(data)
    print(output)

    s_stable = softmax_stable()
    output = s_stable(data)
    print(output)
