from model import Model

class Handler :
    def __init__(self) :
        self.model = Model()
    
    def set_text(self,text) :
        self.text = text
    
    def set_mode(self,mode) :
        self.mode = mode
    
    def set_image_input_mode(self,image_input_mode) :
        self.image_input_mode = image_input_mode
    
    def execute(self) :
        if self.mode == 'gen' :
            return self.model.generate(self.text)
        elif self.mode == 'man' :
            return self.model.manipulate(self.text,self.image_input_mode)
