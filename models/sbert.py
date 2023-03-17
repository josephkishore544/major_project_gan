from sentence_transformers import SentenceTransformer

class sbert :
    def __init__(self,model_path) :
        self.sbert_model = SentenceTransformer(model_path)
    
    def encode(self, text) :
        sentence_embedding_tensor = self.sbert_model.encode(text, convert_to_tensor = True)
        return sentence_embedding_tensor