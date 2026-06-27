# Accelerating KNN Search in Manticore

Discover how Manticore's 2-pass HNSW, batched distances, and AVX-512 features enable faster KNN search, enhancing search performance and efficiency.

## 🔑 The Core of This Topic
Manticore's KNN (k-Nearest Neighbors) search is crucial for various applications, from recommendation systems to content-based search. However, traditional KNN search methods can be computationally expensive, leading to slower performance.

## ⚡ 5-Second Key Points
* **Point 1**: Manticore's 2-pass HNSW (Hierarchical Navigable Small World) algorithm significantly reduces search time.
* **Point 2**: Batched distances calculation further accelerates the search process.
* **Point 3**: AVX-512 instructions provide an additional performance boost.

## 📈 Detailed Breakdown
**Element 1**
The 2-pass HNSW algorithm involves building an HNSW index, which enables efficient search by navigating through a hierarchical structure. This approach allows Manticore to quickly identify potential candidates and then refine the search using a secondary pass.

**Element 2**
Batched distances calculation involves computing distances between query points and index points in batches, rather than individually. This technique reduces the number of distance calculations, resulting in significant performance gains.

> 💡 Insight: By combining 2-pass HNSW and batched distances, Manticore can achieve dramatic speedups in KNN search, making it an ideal choice for demanding applications.

## 🎯 Real-World Impact
* Improved search performance in recommendation systems and content-based search applications.
* Enhanced efficiency in handling large-scale datasets.
* Better scalability for distributed search environments.

## ✨ Conclusion
Manticore's innovative approach to KNN search, leveraging 2-pass HNSW, batched distances, and AVX-512, offers a substantial performance advantage over traditional methods. By adopting these features, developers can create more efficient and scalable search applications.
