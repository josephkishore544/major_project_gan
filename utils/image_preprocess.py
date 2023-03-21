import dlib
from utils.align_all_parallel import align_face
import torchvision.transforms as transforms

def run_alignment(image_path):
  predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
  aligned_image = align_face(filepath=image_path, predictor=predictor)
  return aligned_image

def transform_image(image) :
  image_transforms = transforms.Compose([
            transforms.Resize((256,256)),
            transforms.ToTensor(),
            transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])])
  return image_transforms(image)
  
def image_preprocess(image_path) :
    aligned_image = run_alignment(image_path)
    transformed_image = transform_image(aligned_image)
    return transformed_image
