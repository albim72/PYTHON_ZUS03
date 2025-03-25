import json

class JsonGenerator:
    def generate(self,data,filename):
        with open(filename,'w',encoding='utf-8') as f:
            json.dump(data,f,indent=4,ensure_ascii=False)
        print(f"JSON zapisany do {filename}")
