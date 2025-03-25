class Report:
    def __init__(self):
        self.generators = []
        
    def add_generator(self,generator):
        self.generators.append(generator)
        
    def export(self,data):
        for gen in self.generators:
            ext = gen.__class__.__name__.replace('Generator','').lower()
            gen.generate(data,f"raport.{ext}")
