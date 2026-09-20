# Btrfs, ZFS, bcachefs: How They Fare in Classic Benchmarks

*Insert header image here*

Exploring the performance of modern filesystem benchmarks—Btrfs, ZFS, and bcachefs—under classic workloads. Which one excels, and why do some benchmarks skip them?

## 🔑 The Core of This Topic

Modern filesystems like **Btrfs**, **ZFS**, and **bcachefs** are often scrutinized for their performance under real-world and synthetic workloads. The benchmark suite from [Bartosz Fenski’s analysis](https://bartosz.fenski.pl/modern-fs-benchmark/) sheds light on how these systems handle classic benchmarks—such as **FIO, Bonnie++, and IOzone**—while also explaining why some tests deliberately exclude them. The focus isn’t just on raw speed but also on reliability, scalability, and feature parity.

## ⚡ 5-Second Key Points
- **Btrfs** is lightweight but struggles with extreme workloads due to its copy-on-write (CoW) limitations.
- **ZFS** shines in large-scale storage but can be resource-heavy, often excluded from lightweight benchmarks.
- **bcachefs** is a newer hybrid, balancing performance and features but lacks widespread adoption.
- Some benchmarks skip these filesystems because they’re designed for **enterprise or niche use cases**, not general-purpose testing.
- **Real-world impact** depends on workload—small files, snapshots, or RAID configurations tilt the balance.

## 📈 Detailed Breakdown

**Btrfs: The Balanced Generalist**

Btrfs is praised for its **simplicity and robustness**, offering features like snapshots, RAID, and checksumming out of the box. However, its performance under **high-concurrency or sequential workloads** can lag behind traditional filesystems like ext4. The benchmark suite highlights that Btrfs excels in **small-file I/O** but falters when dealing with **large, sequential writes**, where its **extent-based allocation** becomes a bottleneck. Additionally, its **lack of native compression** (unless enabled via third-party tools) can hurt storage efficiency in certain scenarios.

**ZFS: The Powerhouse with Trade-offs**

ZFS is often the **gold standard for large-scale storage**, thanks to its **built-in RAID-Z, checksumming, and self-healing capabilities**. However, its **high memory overhead** and **complexity** make it a poor fit for lightweight benchmarks. The suite notes that ZFS performs exceptionally well in **large-file, sequential workloads** but struggles with **small, random I/O** due to its **block mapping overhead**. Many classic benchmarks skip ZFS because it’s **not designed for microbenchmarks**—its strengths lie in **enterprise environments**, not raw speed tests.

> 💡 **Insight**: *ZFS’s exclusion from some benchmarks isn’t about performance—it’s about relevance. If a benchmark tests small-file databases, ZFS may not be the best fit, but for NAS or database backups, it dominates.*

**bcachefs: The New Kid with Potential**

bcachefs is an **emerging hybrid filesystem** combining the best of **ext4’s simplicity** and **ZFS’s features**, with **bcache’s caching layer**. Early benchmarks show it **outperforms Btrfs in sequential writes** while maintaining **ZFS-like reliability**. However, its **immature ecosystem** and **limited driver support** mean it’s often excluded from mainstream comparisons. The suite suggests that bcachefs could become a **strong contender** if adoption grows, but for now, it’s **too niche** for classic benchmarks.

## 🎯 Real-World Impact

- **For small-file workloads (e.g., databases, logs)**: Btrfs often wins due to its **efficient small-block handling**, while ZFS and bcachefs may underperform.
- **For large-scale storage (e.g., NAS, backups)**: ZFS remains the **clear leader**, thanks to its **built-in redundancy and scalability**—even if it’s slower in microbenchmarks.
- **For hybrid setups (e.g., SSDs + HDDs)**: bcachefs could **bridge the gap** between performance and reliability, but its **lack of widespread support** limits its appeal.
- **For benchmark designers**: Excluding ZFS/Btrfs isn’t about bias—it’s about **test relevance**. A benchmark testing **extreme I/O** (e.g., video editing) would include them, while a **lightweight file server test** might not.

## ✨ Conclusion

The choice between Btrfs, ZFS, and bcachefs isn’t just about **raw speed**—it’s about **use case**. Btrfs is the **practical generalist**, ZFS is the **enterprise powerhouse**, and bcachefs is the **future contender**. Classic benchmarks often skip them because they’re **not designed for every scenario**, but that doesn’t mean they’re weak—they’re just **optimized for different workloads**. As storage needs evolve, so will the benchmarks, and filesystems like bcachefs may soon take center stage.
