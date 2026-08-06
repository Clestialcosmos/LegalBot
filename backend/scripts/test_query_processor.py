from app.rag.query_processor import processor


queries = [

    "How can I file FIR?",

    "Consumer complaint",

    "Cyber fraud",

    "Property transfer",

    "Salary not paid"

]

for q in queries:

    print("=" * 50)

    print("Original :", q)

    print("Processed:", processor.process(q))