from models.sbert import sbert

sbert = sbert('models\SBERT')
sentence_embedding_tensor = sbert.encode("A woman")