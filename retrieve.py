
from lightrag import LightRAG, QueryParam

async def run_async_query(rag: LightRAG, question: str, mode: str, top_k: int = 5) -> str:
    """
    Execute an async RAG query using .aquery
    """
    return await rag.aquery(
        question,
        param=QueryParam(mode=mode, top_k=top_k)
    )

#top k = queries top similar to the what the user searched for 
#mode = there are 6 modes - local, global, hybrid , naive , mix and bypass 
#mode = mix in this case as we integrate the knowledge graph and vector store 



