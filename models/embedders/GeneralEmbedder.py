import torch.nn as nn

from models.GeneralModel import GeneralModel


class GeneralEmbedder(GeneralModel):

    def __init__(self, n_channels_in: int = 1, n_channels_out: int=1, device: str="cpu", **kwargs): # CHECK DEFAULT PARAMETERS!!!!!!
        super().__init__(n_channels_in, device, **kwargs)
        self.n_channels_out = n_channels_out

    # todo: add methods here that are shared for all embedders, inheret your custom version from this object
