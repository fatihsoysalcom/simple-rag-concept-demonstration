def retrieve_documents(query: str, knowledge_base: list[str], top_k: int = 2) -> list[str]:
    """
    Simulates the retrieval step of RAG.
    Finds documents from the knowledge base relevant to the query.
    In a real RAG system, this would involve vector embeddings and similarity search.
    Here, we use a simple keyword matching for demonstration.
    """
    query_words = set(query.lower().split())
    document_scores = []

    for i, doc in enumerate(knowledge_base):
        doc_words = set(doc.lower().split())
        # Calculate a simple relevance score based on common words
        score = len(query_words.intersection(doc_words))
        document_scores.append((score, doc))

    # Sort by score in descending order and get top_k documents
    document_scores.sort(key=lambda x: x[0], reverse=True)
    retrieved_docs = [doc for score, doc in document_scores if score > 0][:top_k]

    # If no relevant documents found, provide a fallback
    if not retrieved_docs:
        return ["No highly relevant documents found in the knowledge base."]

    return retrieved_docs

def generate_response(query: str, retrieved_context: list[str]) -> str:
    """
    Simulates the generation step of RAG.
    Uses the retrieved context to formulate an answer to the query.
    In a real RAG system, an LLM would process the prompt with context.
    Here, we combine them to show how context guides the answer.
    """
    if not retrieved_context or retrieved_context[0] == "No highly relevant documents found in the knowledge base.":
        # This branch simulates an LLM saying it doesn't have enough info
        return f"I don't have enough specific information in my knowledge base to answer '{query}'. Please try a different query or provide more context."

    # Construct a simulated prompt for the LLM
    # This clearly shows the context being passed to the 'LLM'
    context_str = "\n".join([f"- {doc}" for doc in retrieved_context])
    
    # Simulate LLM's reasoning based on context
    response_parts = [f"Based on the provided information, regarding '{query}':"]
    
    # Simple logic to extract and synthesize information from context
    if "Acme Corp" in query or "company" in query:
        for doc in retrieved_context:
            if "Acme Corp" in doc and "leading innovator" in doc:
                response_parts.append("Acme Corp is a leading innovator in sustainable energy solutions.")
            if "founded" in doc:
                response_parts.append("It was founded in 2005.")
    
    if "Widget X" in query or "product" in query:
        for doc in retrieved_context:
            if "Widget X" in doc and "flagship product" in doc:
                response_parts.append("Widget X is Acme Corp's flagship product.")
            if "features" in doc:
                response_parts.append("Key features of Widget X include advanced AI integration and modular design.")
            if "benefits" in doc:
                response_parts.append("It helps businesses optimize operations and reduce costs.")
    
    if len(response_parts) == 1: # Only the initial statement, no specific info extracted
        response_parts.append("Here's what I found in the context:")
        response_parts.extend([f"  {doc}" for doc in retrieved_context])

    return "\n".join(response_parts)

def main():
    # 1. Define a knowledge base (simulating external data source)
    # This is the "R" (Retrieval) part's data source
    knowledge_base = [
        "Acme Corp is a leading innovator in sustainable energy solutions, founded in 2005.",
        "Widget X is Acme Corp's flagship product, known for its advanced AI integration and modular design.",
        "The benefits of Widget X include optimizing business operations, reducing operational costs, and improving efficiency.",
        "Acme Corp also offers consulting services for renewable energy projects.",
        "Customer testimonials often highlight Widget X's ease of use and robust performance.",
        "The company's headquarters are located in Tech City."
    ]

    print("--- RAG Assistant Demonstration ---")
    print("Knowledge Base Loaded.\n")

    # 2. User Query
    user_query = "What is Acme Corp and what are the features of Widget X?"
    print(f"User Query: \"{user_query}\"\n")

    # 3. Retrieval Step: Find relevant documents from the knowledge base
    # This is where the 'Retrieval' happens
    retrieved_context = retrieve_documents(user_query, knowledge_base, top_k=3)
    print("--- Retrieved Context (simulated) ---")
    for i, doc in enumerate(retrieved_context):
        print(f"  Doc {i+1}: {doc}")
    print("\n" + "="*40 + "\n")

    # 4. Generation Step: Use the retrieved context to answer the query
    # This is where the 'Augmented Generation' happens, using the context
    final_response = generate_response(user_query, retrieved_context)
    print("--- RAG Assistant's Response (simulated LLM) ---")
    print(final_response)
    print("\n" + "="*40 + "\n")

    # Example with a query that might not find much
    user_query_2 = "Who is the CEO of Acme Corp?"
    print(f"User Query 2: \"{user_query_2}\"\n")
    retrieved_context_2 = retrieve_documents(user_query_2, knowledge_base, top_k=3)
    print("--- Retrieved Context 2 (simulated) ---")
    for i, doc in enumerate(retrieved_context_2):
        print(f"  Doc {i+1}: {doc}")
    print("\n" + "="*40 + "\n")
    final_response_2 = generate_response(user_query_2, retrieved_context_2)
    print("--- RAG Assistant's Response 2 (simulated LLM) ---")
    print(final_response_2)

if __name__ == "__main__":
    main()