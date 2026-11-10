# Satellite Spy: Tracking Every Eye in the Sky Over Your Home

Ever wondered if satellites were watching your street? This HN post introduces Watched.Earth, a tool that reveals *every* satellite pass and its photos over any location in the last week—powered by real-time orbital tracking.

## 🔑 The Core of This Topic
A curious developer built **Watched.Earth** to answer a simple but profound question: *What satellites have actually photographed my neighborhood?* By combining **open-source orbital mechanics (SGP4)** with **CelesTrak’s satellite database**, the platform maps every satellite pass over any global coordinate within the last seven days—including high-resolution imagery. No more guessing who’s watching from above; now you can see *exactly* when, where, and *what* satellites capture.

## ⚡ 5-Second Key Points
- **Real-time satellite tracking**: Input any address or GPS, and the tool lists *all* satellites that passed overhead in 7 days.
- **Visual proof**: Includes **actual satellite photos** of your location (if available) from sources like **Planet Labs, Maxar, or commercial providers**.
- **Open transparency**: Uses **public orbital data** (CelesTrak) to avoid proprietary black-box algorithms.

## 📈 Detailed Breakdown
**Orbital Mechanics Made Accessible**
Traditionally, satellite tracking required deep knowledge of **Keplerian elements** or expensive software. Watched.Earth simplifies this by leveraging **SGP4**, a widely used algorithm for predicting satellite positions. By cross-referencing this with **CelesTrak’s catalog of 10,000+ active satellites**, the tool dynamically calculates which ones fly over your input coordinates—and when. The result? A **live feed of overhead activity**, complete with timestamps and orbital paths.

**From Data to Imagery**
The real magic happens when the tool connects orbital passes to **satellite imagery**. For example, if a **PlanetScope satellite** (known for daily revisits) passes over your street, Watched.Earth may display a **5m-resolution photo** of your neighborhood. This bridges the gap between abstract orbital data and **tangible visual evidence**, making satellite surveillance feel less like sci-fi and more like a **public resource**.

> 💡 Insight: *This tool democratizes satellite data, turning a niche hobby (amateur orbital tracking) into a tool for everyday curiosity—and even privacy awareness.*

## 🎯 Real-World Impact
- **Privacy Awareness**: Know *exactly* which satellites (government, commercial, or military) have photographed your home—useful for privacy-conscious individuals or activists.
- **Scientific & Citizen Science**: Researchers or hobbyists can now **correlate satellite passes with local events** (e.g., weather patterns, urban changes) without expensive equipment.
- **Disaster Response**: In emergencies, first responders could use this to **identify recent satellite imagery** of affected areas, aiding rapid assessment.

## ✨ Conclusion
Watched.Earth transforms the abstract concept of **satellite surveillance** into an interactive, visual experience. By merging **open orbital data** with **real-world imagery**, it turns curiosity into actionable insight. Whether you’re a privacy advocate, a scientist, or just someone who wonders *who’s looking down*, this tool proves that **the sky isn’t just full of stars—it’s full of eyes**. Now, the question isn’t *if* satellites are watching, but **when—and what they’ve already seen**.
