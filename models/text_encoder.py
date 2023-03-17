import torch
from torch import nn

# TextEncoder Model
# Its a simple fully connected neural network
class TextEncoder(nn.Module) :
  def __init__(self, input_features = 768, output_features = 37) :
    super().__init__()
    self.encode_text = nn.Sequential(
                        nn.Linear(input_features,384),
                        nn.ReLU(),
                        nn.Linear(384,192),
                        nn.ReLU(),
                        nn.Linear(192,48),
                        nn.ReLU(),
                        nn.Linear(48,output_features)
                      )
  def forward(self,sentence_embedding) :
    res = self.encode_text(sentence_embedding)
    return res