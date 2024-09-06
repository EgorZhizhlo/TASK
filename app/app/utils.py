class Index:
    def __init__(self, elsearch, name, df):
        self.create_index(elsearch, name)
        self.index_documents(elsearch, name, df)
    
    def create_index(self, elsearch, name):
         if not elsearch.indices.exists(index=name):
            elsearch.indices.create(
                index=name,
                body={
                    "mappings": {
                        "properties": {
                            "id": {"type": "keyword"},
                            "text": {"type": "text"}
                        }
                    }
                }
            )

    def index_documents(self, elsearch, name, df):
        for _, row in df.iterrows():
            elsearch.index(
                index=name,
                id=row['id'],
                body={
                    "text": row['text']
                }
            )