# RowHammer & RowPress: Unpacking DRAM Read Disturbance

*Insert header image here*

Discover the subtle yet critical DRAM read disturbance issues like RowHammer and RowPress. Learn how repeated access patterns can corrupt data and explore mitigation strategies.

## 🔑 The Core of This Topic
Dynamic Random-Access Memory (DRAM) relies on capacitors to store data. Repeatedly accessing (reading or writing) adjacent memory rows can cause charge leakage from neighboring cells, leading to data corruption. This phenomenon, known as read disturbance, manifests as RowHammer and RowPress.

## ⚡ 5-Second Key Points
- **RowHammer**: Repeatedly accessing one row can corrupt data in an adjacent row.
- **RowPress**: Similar to RowHammer, but focuses on the effect of *writing* to a row.
- **Mitigation**: Techniques like error correction codes (ECC) and memory controllers are employed.

## 📈 Detailed Breakdown
**RowHammer Effect**
This occurs when a memory row is repeatedly read or written to. The electrical charge in nearby rows can degrade, causing bits to flip and corrupting the stored data. This is a critical vulnerability.

**RowPress Effect**
While RowHammer is primarily associated with reads, RowPress highlights that writes to a row can also induce charge disturbances in adjacent rows, leading to similar data corruption issues.

> 💡 Insight: Both read and write operations, under specific patterns, can destabilize neighboring DRAM cells.

## 🎯 Real-World Impact
- **Data Corruption**: Silent errors can occur, leading to system instability or incorrect computations.
- **Security Vulnerabilities**: RowHammer can be exploited to bypass security mechanisms and corrupt data intentionally.
- **Performance Trade-offs**: Mitigation techniques can sometimes introduce latency or reduce memory efficiency.

## ✨ Conclusion
Understanding and mitigating DRAM read disturbance phenomena like RowHammer and RowPress is crucial for ensuring data integrity and system reliability in modern computing.
