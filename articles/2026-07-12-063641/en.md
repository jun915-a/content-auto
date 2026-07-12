# Biff.graph: Turn Your Clojure Code into a Queryable Graph

Tired of tangled Clojure dependencies? Biff.graph transforms your codebase into a structured, queryable graph—unlocking insights and simplifying refactoring with pure data.

{
  "## 🔑 The Core of This Topic": "Biff.graph is a library that models your Clojure codebase as a graph, enabling powerful querying and analysis of dependencies, modules, and relationships between components.",
  "## ⚡ 5-Second Key Points": [
    "- **Graph-based structure**: Represents your codebase as nodes (functions, namespaces) and edges (dependencies).",
    "- **Queryable**: Use Datalog to explore relationships dynamically.",
    "- **Tooling-friendly**: Integrates with Biff’s ecosystem for seamless dev workflows.",
    "- **Pure data**: Works with plain Clojure maps—no magic required.",
    "- **Refactoring aid**: Visualize and untangle complex dependency chains."
  ],
  "## 📈 Detailed Breakdown": {
    "**Element 1": "Biff.graph treats your codebase as a graph where namespaces, functions, and vars are nodes. Edges represent dependencies like `:uses`, `:requires`, or `:implements`. By exporting this structure as data, you gain a machine-readable map of your project’s architecture. This isn’t just theoretical—it’s the foundation for tools that analyze coupling, detect cycles, or even suggest refactoring strategies.",
    "**Element 2": "The real magic happens with Datalog queries. Want to find all functions in `my.app` that call `clojure.core/println`? Or trace the dependency chain from a slow-loading namespace? Biff.graph lets you express these questions in a declarative query language, returning results as Clojure data. It’s like having a lightweight static analysis tool baked into your project, always up-to-date with your latest changes.",
    "> 💡 Insight: By modeling code as data, Biff.graph bridges the gap between human intuition and machine analysis. It turns what’s often a mental burden—understanding a codebase—into a solvable puzzle.": "## 🎯 Real-World Impact"
  },
  "- **Early bug detection**: Identify circular dependencies before they cause runtime issues or confusing stack traces in production. This saves hours of debugging by catching problems at compile time or during static analysis phases.": "- **Onboarding acceleration**: New team members can query the graph to understand how components interact, reducing the time spent reverse-engineering code or chasing down tribal knowledge."
}
