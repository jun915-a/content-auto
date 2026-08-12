# pg_clickhouse v0.10: 1000x Faster TPC-H with Subquery Pushdown

Discover how pg_clickhouse v0.10 revolutionizes PostgreSQL-ClickHouse integration with subquery pushdown, slashing TPC-H query times by 1000x and unlocking unprecedented performance.

{
  "## 🔑 The Core of This Topic": "pg_clickhouse v0.10 introduces groundbreaking subquery pushdown, enabling PostgreSQL to offload complex TPC-H queries to ClickHouse for lightning-fast execution. This optimization delivers up to **1000x speed improvements**, transforming analytical workloads.",
  "## ⚡ 5-Second Key Points": "- **Subquery pushdown**: Pushes complex queries directly to ClickHouse for execution\n- **TPC-H performance**: Achieves **1000x faster** query times compared to native PostgreSQL\n- **Seamless integration**: Works transparently with existing PostgreSQL setups\n- **Analytical dominance**: Ideal for data warehouse and BI workloads\n- **Zero refactoring**: No changes needed to existing application code",
  "## 📈 Detailed Breakdown": "**Element 1**\npg_clickhouse v0.10 leverages ClickHouse's columnar storage and vectorized execution engine to handle subqueries that PostgreSQL traditionally struggles with. By pushing these queries to ClickHouse, the system avoids PostgreSQL's row-based processing bottlenecks, resulting in dramatic performance gains. This is particularly impactful for analytical queries with JOINs and aggregations typical in TPC-H benchmarks.",
  "**Element 2**\nThe integration remains transparent to users—no schema changes or SQL rewrites are required. The extension automatically detects eligible subqueries and routes them to ClickHouse, while simpler queries continue to run locally in PostgreSQL. This hybrid approach ensures optimal performance without sacrificing PostgreSQL's transactional capabilities or ClickHouse's analytical power.\n\n> 💡 Insight: Subquery pushdown isn't just an optimization; it's a paradigm shift for PostgreSQL-ClickHouse integration, enabling real-time analytics on massive datasets without compromising on simplicity or familiarity.\n\n## 🎯 Real-World Impact": "- **Enterprise analytics**: Run TPC-H benchmarks in seconds instead of hours\n- **Cost efficiency**: Reduce cloud compute costs by offloading heavy queries\n- **Developer productivity**: Eliminate query rewrites and performance tuning overhead\n- **Scalability**: Handle petabyte-scale datasets with ease\n- **Hybrid workloads**: Combine OLTP and OLAP seamlessly in a single stack",
  "## ✨ Conclusion": "pg_clickhouse v0.10 is a game-changer for teams relying on PostgreSQL for both transactions and analytics. By bridging the gap between PostgreSQL and ClickHouse with subquery pushdown, it delivers performance that was previously unimaginable—making 1000x faster TPC-H queries a reality today. The future of hybrid data processing is here, and it's faster than ever.",
  "tags": [
    "ClickHouse",
    "PostgreSQL",
    "Analytics"
  ]
}
