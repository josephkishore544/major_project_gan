from models.encoders.psp_encoders import GradualStyleEncoder
import torch

class Inverter :
    def __init__(self, model_path, num_layers = 18) :
        self.inversion_model = GradualStyleEncoder(num_layers = 50, input_nc = 3, n_styles = num_layers)
        self.inversion_model
    def invert(self,image) :
        latent_code = self.inversion_model(image)