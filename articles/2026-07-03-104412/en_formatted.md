# Manticore’s ONNX embeddings now 14x faster—here’s how

*Insert header image here*

Discover how Manticore rebuilt the ONNX path to deliver **14× faster embeddings**, slashing latency for vector search and AI-powered features. Dive into the technical breakthroughs behind this leap.

## 🔑 The Core of This Topic
Manticore Search has dramatically accelerated ONNX-based embeddings by rebuilding the underlying path, achieving **14× performance gains**. This optimization directly impacts vector search, AI-powered query expansions, and multi-modal applications by reducing latency and improving throughput. The breakthrough stems from deep integration with ONNX Runtime and strategic code refactoring.

## ⚡ 5-Second Key Points
- **ONNX Runtime Integration**: Deepened collaboration with ONNX Runtime for native optimizations.
- **Code Refactoring**: Streamlined Manticore’s embedding pipeline to eliminate redundancies.
- **14× Speedup**: Benchmarks show near-instantaneous embeddings, unlocking real-time AI features.
- **Backward Compatibility**: Existing ONNX models remain fully supported.
- **Scalability**: Performance gains hold across varied hardware, from CPUs to GPUs.

## 📈 Detailed Breakdown
**Element 1**
The core of the speedup lies in Manticore’s tighter integration with **ONNX Runtime**, bypassing generic inference paths. By leveraging ONNX Runtime’s optimized kernels and graph optimizations, Manticore eliminated bottlenecks in tensor operations—critical for embeddings. This reduced overhead in model loading and inference, especially for large transformer-based models like BERT or sentence transformers.

**Element 2**
Refactoring the embedding pipeline focused on **minimizing data movement** and **exploiting parallelism**. Manticore’s new ONNX path now pre-allocates memory buffers and aligns tensor shapes upfront, avoiding dynamic resizing during inference. The team also introduced **batch-aware scheduling**, ensuring GPU resources are fully utilized even for small embedding requests.

> 💡 Insight: The 14× speedup isn’t just about raw compute—it’s about **eliminating hidden inefficiencies** in the embedding pipeline that compound under real-world workloads.

## 🎯 Real-World Impact
- **Real-time AI Search**: Vector search now operates at sub-millisecond latencies, enabling instant semantic search in applications like e-commerce or content discovery.
- **Cost Efficiency**: Reduced computational overhead lowers cloud bills for cloud-native deployments, making AI-driven features more accessible.
- **Expanded Use Cases**: The speedup unlocks new possibilities, such as **on-the-fly query rewriting** with embeddings or **multi-modal search** combining text, images, and vectors.

## ✨ Conclusion
Manticore’s ONNX embedding optimization is a game-changer for vector search and AI-powered applications. By squeezing every ounce of performance from ONNX Runtime and refactoring the pipeline, they’ve made embeddings **fast enough for real-time use at scale**—proving that even mature systems can see transformative gains with the right optimizations.
