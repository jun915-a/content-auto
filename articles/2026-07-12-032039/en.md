# Pruning with Non-Partitioned Columns in PostgreSQL

Discover how to optimize your SQL queries with PostgreSQL's partition pruning feature when querying non-partitioned columns.

## 🔑 The Core of This Topic
Partition pruning is a feature in PostgreSQL that allows the database to skip scanning certain partitions of a table when querying data. However, when using non-partitioned columns in the WHERE clause, pruning may not occur, leading to slower query performance. This article explores how to achieve pruning even when querying non-partitioned columns.

## ⚡ 5-Second Key Points
* **Point 1**: Understand how partition pruning works in PostgreSQL.
* **Point 2**: Learn how to use the `WHERE` clause with non-partitioned columns to enable pruning.
* **Point 3**: Discover best practices for optimizing your SQL queries with partition pruning.

## 📈 Detailed Breakdown
**Element 1**
When a query is executed on a partitioned table, PostgreSQL checks the WHERE clause to determine which partitions to scan. If the WHERE clause only references partitioned columns, pruning can occur and only the relevant partitions are scanned. However, if the WHERE clause references non-partitioned columns, pruning may not occur, leading to slower query performance.

**Element 2**
To enable pruning when querying non-partitioned columns, you can use the PARTITION BY LIST or PARTITION BY RANGE methods. These methods allow you to specify which columns are used for partitioning, enabling pruning to occur even when non-partitioned columns are used in the WHERE clause.

> 💡 Insight: By using the PARTITION BY LIST or PARTITION BY RANGE methods, you can optimize your SQL queries and achieve pruning even when querying non-partitioned columns.

## 🎯 Real-World Impact
* Improved query performance due to pruning
* Reduced resource usage by scanning only relevant partitions
* Enhanced scalability and maintainability of large databases

## ✨ Conclusion
In conclusion, achieving pruning with non-partitioned columns in PostgreSQL requires understanding how partition pruning works and using the PARTITION BY LIST or PARTITION BY RANGE methods. By following these best practices, you can optimize your SQL queries and improve the performance of your database.
