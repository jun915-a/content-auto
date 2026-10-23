# ClickHouse’s pgrust Removal: Why Per-Query Kernels Were Cheating

*Insert header image here*

ClickHouse’s open-source benchmark suite, ClickBench, has removed `pgrust`—a controversial feature enabling per-query kernels and result caching. This decision exposes how certain optimizations could skew performance metrics, undermining trust in benchmarking integrity. Here’s why this matters and what it means for database evaluation.

**ClickHouse’s pgrust Removal: Why Per-Query Kernels Were Cheating**

ClickHouse’s ClickBench suite has eliminated `pgrust`, a feature that allowed per-query kernels and result caching. This move isn’t just a technical tweak—it’s a direct challenge to the integrity of database benchmarking. By enabling query-specific optimizations, `pgrust` artificially inflated performance metrics, creating a misleading picture of ClickHouse’s capabilities. The removal forces a return to fairer, more transparent comparisons, ensuring benchmarks reflect real-world performance rather than cherry-picked optimizations.

## 🔑 The Core of This Topic

The `pgrust` feature in ClickBench introduced **per-query kernels** and **result caching**, allowing ClickHouse to optimize individual queries beyond standard execution paths. This cheated benchmarking by enabling artificial speedups that wouldn’t replicate in production. The removal restores fairness, ensuring that performance comparisons are based on consistent, unmodified execution pipelines.

## ⚡ 5-Second Key Points
- **Point 1**: `pgrust` used **per-query kernels** to bypass standard ClickHouse optimizations, skewing benchmark results.
- **Point 2**: **Result caching** in `pgrust` artificially inflated performance by reusing cached outputs, not reflecting real workloads.
- **Point 3**: The removal ensures **transparency** in benchmarking, aligning results with actual database behavior.

## 📈 Detailed Breakdown

**Element 1**
The `pgrust` feature exploited **per-query kernels**, which are specialized execution paths tailored to individual queries. While this might seem like an advanced optimization, it fundamentally **bypassed ClickHouse’s default execution engine**, creating an unfair advantage in benchmarks. In real-world scenarios, databases don’t get to optimize each query on the fly—performance must be consistent across all workloads. By allowing this, `pgrust` distorted how ClickHouse was perceived, making it appear faster than it would be in practice.

**Element 2**
Beyond per-query kernels, `pgrust` also **cached results** from previous executions. This meant that repeated queries in benchmarks could reuse cached outputs, artificially lowering execution time without any additional computational effort. While caching is a valid optimization in some contexts, it doesn’t reflect how databases handle **dynamic or one-off queries**, which are far more common in production. The removal of this feature ensures benchmarks now measure **true query processing time**, not cached shortcuts.

> 💡 **Insight**: *Benchmarking integrity hinges on consistency. `pgrust`’s removal proves that even small optimizations can distort comparisons—transparency is the only fair baseline.*

## 📈 Real-World Impact
- **Impact 1**: **Fairer database comparisons** – Other databases (e.g., PostgreSQL, MySQL) won’t be penalized by unfairly optimized benchmarks, leveling the playing field.
- **Impact 2**: **More reliable performance predictions** – Developers and operators can now trust benchmark results to reflect real-world ClickHouse behavior, not artificial speedups.
- **Impact 3**: **Encourages better benchmarking practices** – The move sets a precedent for open-source projects to prioritize **transparency** over shortcuts in performance testing.

## ✨ Conclusion
The removal of `pgrust` from ClickBench is a bold step toward **honest benchmarking**. While per-query optimizations and caching might seem like minor tweaks, they fundamentally **cheat the system** by distorting performance metrics. By eliminating these artificial advantages, ClickHouse ensures that its benchmarks now accurately represent how the database performs under real-world conditions. This isn’t just about ClickHouse—it’s a call for **greater integrity in all database comparisons**, where fairness and transparency should always take precedence over shortcuts.
