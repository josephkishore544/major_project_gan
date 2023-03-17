from models.stylegan2.model import Generator

class StyleGAN2 :
    def __init__(self,output_size, w_dim, mlp = 8) :
        self.generator = Generator(output_size, w_dim, mlp)
        
    def generate(self,latent_codes) :
        with torch.no_grad() :
            res = self.generator([latent_codes],
                                input_is_latent = True, # input_is_latent = not input_code
                                randomize_noise = True
                                )
        return res[0]