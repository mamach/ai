# Vector Database Notes
- Vector databases are the backbone of Retrieval Augumented Generation(RAG).
- How do they actually work?
    - Goal: index three sentences, then answer a query by finding the nearest one, filling in every cell yourself.
- Given
    - A dataset of three sentneces, three words each. In practice it is millions of them.
- Word Embeddings
    - Let us look up each word in an embedding table. Here the vocabulary is 22 words; in practice tens of thousands, and the vectors have thousands of dimensions rather than four.
- Encoding
    - We feed the sequence to an encoder, one linear layer and a ReLU adn get one feature vector per word. In practice the encode is a transformer.
- Mean Pooling
    - Let us average across the columns. Three word vectors collapse into one, which is what people mean by a text embedding or a sentence embedding.
- Indexing
    - We multiply by a projection matrix and the four dimensions become two. It is doing the job of a hash; a short representation that is faster to compare, and it is what gets saved in the vector storage.
- Process "Who are you"
    - Let us repeat steps 2 to 5 on the second sentence.
- Process "Who am i"
    - We do it a third time. The database is now indexed.
- Query "Am i you"
    - Let us push the query through the very same pipeline: lookup, encoder, mean pooling, projection, and it lands as a 2d vector in the same space.
- dot products
    - we transpose the query and multiply, which takes the dot product against every stored vector at once. The dot product is the estimate of similarity.
- Neares Neighbour
    - Let us scan for the largest: 60/9 beats 44/9 and 40/9, so the answer is who am i. Scanning billions of vectos one at a time is what makes this the slow step in practice.
    - which is why real database use an approximate neighbour index like HNSW.
- The takeaway: a vector database is an embedding pipeline, a projection, and a dot product.
- Every step here is arithmetic you can do in pen, which is worth remembering when the word database makes it sound like something else.

# References
- https://x.com/ProfTomYeh/status/2092979260424179979

