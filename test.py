from models.StyleGAN2 import StyleGAN2
from utils.common import tensor2im
import torch
import PIL.Image
import np

gen = StyleGAN2()
w = torch.rand(1,18,512)
img = gen.generate(w)
img_arr = np.array(tensor2im(img))
save = PIL.Image.fromarray(res_img)
save.save('test/output.jpg')