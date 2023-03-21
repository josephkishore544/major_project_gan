from models.inverter import Inverter
from models.sbert import sbert
from models.stylegan_model import StyleGAN2
from models.text_encoder import TextEncoder
from models.latent_code_decoder import LatentCodeDecoder
from models.manipulater import LatentManipulator
import torch
import PIL.Image
from configs.paths import get_path

class Model() :
    def __init__(self) :
        self.sbert = sbert(get_path('sbert'))
        self.inverter = Inverter()
        self.stylegan = StyleGAN2()
        self.text_encoder = TextEncoder()
        self.latent_code_decoder = LatentCodeDecoder()
        self.lantent_manipulator = LatentManipulator()