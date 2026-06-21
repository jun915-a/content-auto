# Mastering Occupancy Math on AMD MI355X: A Powerful Guide

*Insert header image here*

Unlock the secrets behind occupancy math on the AMD MI355X GPU. Discover how wavefronts, wavefront occupancy, and wavefront scheduling work together to maximize performance in compute shaders.

## 🔑 The Core of This Topic
The AMD MI355X’s occupancy math revolves around **wavefront scheduling**, **register pressure**, and **shared memory usage**. These three factors determine how efficiently your compute shaders utilize the hardware, directly impacting performance and power efficiency.

## ⚡ 5-Second Key Points
- **Wavefront Scheduling**: The MI355X schedules **64-thread wavefronts** to hide memory latency and maximize compute throughput.
- **Register Pressure**: High register usage per wavefront **reduces occupancy**, limiting parallelism.
- **Shared Memory Impact**: Allocating too much shared memory per workgroup **lowers occupancy** by restricting active wavefronts.
- **Wavefront Occupancy**: The number of active wavefronts per compute unit determines efficiency.
- **Hardware Limits**: The MI355X supports up to **28 wavefronts per compute unit**, but real-world occupancy depends on register and memory usage.

## 📈 Detailed Breakdown
**Element 1: Wavefront Scheduling and Latency Hiding**
The MI355X’s compute units (CUs) are designed to execute **64-thread wavefronts** in lockstep. When a wavefront stalls due to memory access, the CU quickly switches to another wavefront, hiding latency. This scheduling mechanism ensures high throughput, but it only works if there are enough **active wavefronts** to switch between. If register or shared memory constraints limit occupancy, the CU may stall, reducing performance.

**Element 2: Register and Shared Memory Constraints**
The MI355X has **64 KB of LDS (Local Data Share) per CU** and a fixed number of **physical registers per wavefront**. Every register used in a shader consumes hardware resources, and exceeding the per-wavefront register limit forces the compiler to spill registers to memory, drastically reducing occupancy. Similarly, shared memory allocations per workgroup compete for LDS space, further limiting the number of active wavefronts.

> 💡 Insight: **Occupancy is not just about maximizing active wavefronts—it’s about balancing register pressure, shared memory usage, and wavefront scheduling to keep the CUs busy.**

## 🎯 Real-World Impact
- **Performance Variability**: Poor occupancy leads to **lower FLOPS and memory bandwidth utilization**, resulting in suboptimal shader performance.
- **Power Efficiency**: High occupancy ensures the GPU runs at peak efficiency, reducing wasted cycles and power draw.
- **Scalability**: Understanding occupancy helps developers optimize shaders for different workloads, from compute-heavy kernels to graphics pipelines.

## ✨ Conclusion
Occupancy math on the AMD MI355X isn’t just a theoretical concept—it’s a **practical tool** to squeeze out maximum performance. By carefully managing register usage, shared memory, and wavefront scheduling, developers can unlock the full potential of this powerful GPU. Whether you're writing compute shaders or optimizing graphics pipelines, mastering occupancy is the key to writing high-performance GPU code.
