def validator_factory(schema):
    class DataValidator:
        def __init__(self,data):
            self.data = data
            self.errors = []

        def validate(self):
            for field, field_type in schema.items():
                if field not in self.data:
                    self.errors.append(f"Oczekiwane pole: {field}")
                elif not isinstance(self.data[field],field_type):
                    self.errors.append(f"Pole '{field}' powinno byc typu {field_type.__name__}")
                    
            return not self.errors
        
        def get_errors(self):
            return self.errors
    return DataValidator
