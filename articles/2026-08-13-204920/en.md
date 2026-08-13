# How I Built a 500K-Domain Search Engine in a Weekend for $10

A maker’s weekend project turned into a lightning-fast search engine scraping 500k domains—all for the cost of a coffee. Here’s how it happened.

{
  "## 🔑 The Core of This Topic": "This is the story of Marlin, a search engine built in a single weekend by one person. It scrapes 500,000+ domains, indexes them in seconds, and costs under $10 to run. The best part? It’s open-source and built with tools anyone can use.",
  "## ⚡ 5-Second Key Points": [
    "**Speed**: Indexes 500k domains in under 2 minutes using parallel scraping.",
    "**Cost**: Runs on a $10 DigitalOcean droplet with free tools like Go and SQLite.",
    "**Scale**: Built in a weekend by one person—no VC funding or big teams needed."
  ],
  "## 📈 Detailed Breakdown": {
    "Marlin’s Architecture": "The engine relies on Go’s concurrency model to scrape domains in parallel. Instead of heavy databases, it uses SQLite for storage, keeping the entire index under 1GB. The scraper itself is a lightweight HTTP client that avoids complex parsing—just raw speed.",
    "The Weekend Sprint": "Starting Friday evening, the project went from zero to live in 48 hours. The key was focusing on the core: scraping, indexing, and serving results. No bells and whistles—just a simple but functional search engine. The $10 droplet handled the load without breaking a sweat.",
    "> 💡 Insight": "You don’t need millions or a team to build something fast and scalable. The right tools and a clear goal can turn a weekend hack into a powerful product."
  },
  "## 🎯 Real-World Impact": [
    "Proves that **makers** can build powerful tools without corporate backing.",
    "Shows how **open-source** and **minimalism** can outperform bloated solutions.",
    "Inspires others to **experiment**—your weekend project could be the next big thing."
  ],
  "## ✨ Conclusion": "Marlin started as a curiosity but became a testament to what one person can achieve in a short time. The lesson? Start small, stay lean, and let the results speak for themselves. Now, the next challenge is scaling it further—or watching others remix it into something even bigger."
}
