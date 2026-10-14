from torch import nn, Tensor


class AutoEncoder(nn.Module):
    def __init__(self, input_dim: int) -> None:
        super().__init__()

        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 8),
            nn.ReLU(),
            nn.Linear(8, 4),
            nn.ReLU()
        )

        self.decoder = nn.Sequential(
            nn.Linear(4, 8),
            nn.ReLU(),
            nn.Linear(8, input_dim)
        )

    def forward(self, x: Tensor):
        z = self.encoder(x)
        return self.decoder(z)
