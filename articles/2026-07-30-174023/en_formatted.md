# DuckDB Paging: file_row_number vs OFFSET - Which Wins?

*Insert header image here*

Struggling with slow queries in DuckDB when paging through Parquet files? Discover why `file_row_number()` outperforms OFFSET and how to optimize your data workflows.

{
  "## 🔑 The Core of This Topic": "DuckDB offers two ways to page through Parquet files: `file_row_number()` and OFFSET. While both achieve pagination, `file_row_number()` leverages file metadata for blazing-fast results, unlike OFFSET which scans entire files repeatedly. This distinction is critical for performance in large datasets.",
  "## ⚡ 5-Second Key Points": [
    "- **`file_row_number()` is metadata-driven** for instant row indexing in Parquet files",
    "- **OFFSET forces full file scans** per query, killing performance on large datasets",
    "- **Use `file_row_number()` with `ROWS BETWEEN`** for stable, efficient pagination",
    "- **OFFSET breaks caching** as every query re-executes the scan",
    "- **Benchmark both methods**—the difference is night and day for big data"
  ],
  "## 📈 Detailed Breakdown": {
    "**Element 1**: The Power of Metadata in `file_row_number()`": "Parquet files store row-level metadata, including row counts and offsets. DuckDB’s `file_row_number()` function taps into this metadata, allowing instant jumps to specific rows without scanning the entire file. This means no matter how large your dataset, the first query to find a page is as fast as subsequent ones. In contrast, OFFSET ignores this metadata, forcing a sequential scan from the start of the file every time—even if you’re loading page 100.",
    "**Element 2**: The Hidden Cost of OFFSET": "OFFSET might seem intuitive, but it’s a performance trap. Each OFFSET query must reprocess the entire file up to the offset, regardless of whether you’re fetching page 1 or 100. This leads to quadratic time complexity as your data grows. Worse, OFFSET bypasses DuckDB’s caching mechanisms, as each query is treated as a fresh scan. For datasets exceeding a few hundred megabytes, OFFSET can turn pagination into a waiting game.",
    "> 💡 Insight: The key to high-performance paging in DuckDB lies in leveraging file metadata. `file_row_number()` unlocks this power, while OFFSET treats your data like a text file—inefficient and outdated.": ""
  },
  "## 🎯 Real-World Impact": [
    "- **Faster dashboards**: Pagination loads in milliseconds instead of seconds, improving user experience",
    "- **Lower cloud costs**: Fewer CPU cycles mean reduced cloud billing for large-scale queries",
    "- **Scalable analytics**: Handle datasets with billions of rows without rewriting queries or infrastructure",
    "- **Simpler code maintenance**: Consistent performance removes the need for workarounds like pre-aggregation",
    "- **Future-proof queries**: `file_row_number()` adapts seamlessly to growing Parquet files without degradation"
  ],
  "## ✨ Conclusion": "When paging through Parquet files in DuckDB, `file_row_number()` isn’t just better—it’s the only sane choice for performance-critical applications. OFFSET belongs in legacy systems, not modern data stacks. By embracing metadata-driven queries, you unlock speed, scalability, and simplicity. Test it yourself: the first time you replace OFFSET with `file_row_number()`, you’ll wonder why you didn’t do it sooner.",
  "tags": [
    "DuckDB",
    "Parquet",
    "Data Pagination"
  ]
}
