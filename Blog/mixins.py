class FormFields:
    
    @classmethod
    def get_fields(cls):
        return (i for i in cls.base_fields.keys())
