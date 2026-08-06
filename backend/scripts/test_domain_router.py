from app.rag.domain_router import router

queries = [

    "How can I file FIR?",

    "Consumer complaint",

    "Cyber fraud through UPI",

    "Property transfer",

    "Salary not paid",

    "Domestic violence complaint",

    "RTI application",

    "Maintenance of parents"

]

for q in queries:

    print("=" * 50)
    print(q)
    print(router.detect(q))