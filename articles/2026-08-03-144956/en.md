# UniFi PPPoE Slowdown Solved: PPPoE Half-Bridge Hack

Tired of UniFi routers bottlenecking your internet speeds with PPPoE? Discover how a clever PPPoE Half-Bridge configuration dramatically boosts performance and ends frustrating slowdowns.

## 🔑 The Core of This Topic
This post details a "PPPoE Half-Bridge" workaround for Ubiquiti UniFi Dream Machine (UDM) and UniFi Security Gateway (USG) devices. It bypasses the CPU-intensive PPPoE processing on the router, offloading it to a dedicated modem, thereby resolving significant performance bottlenecks.

## ⚡ 5-Second Key Points
- **Faster Speeds**: Eliminates PPPoE CPU overhead for maximum throughput.
- **Simple Setup**: Achieved with modem and router configuration changes.
- **Rock Solid**: Provides stable, high-performance PPPoE connections.

## 📈 Detailed Breakdown
**The PPPoE Problem**
UniFi devices struggle with PPPoE encapsulation, especially on higher internet plans. This leads to the router's CPU becoming a bottleneck, preventing you from reaching advertised speeds and causing general network sluggishness.

**The Half-Bridge Solution**
By configuring your modem in "bridge mode" and letting a secondary device (often a small, dedicated router or even the ISP's modem if capable) handle the PPPoE authentication, the UniFi device only needs to manage standard Ethernet traffic, dramatically freeing up its CPU resources.

> 💡 Insight: Offloading the computationally expensive PPPoE authentication and encapsulation process from the main router significantly improves network performance.

## 🎯 Real-World Impact
- Users experience internet speeds closer to their subscribed plan's maximum.
- Reduced latency and improved responsiveness for online gaming and real-time applications.
- Solves the common "UDM Pro PPPoE speed limit" issue for gigabit connections.

## ✨ Conclusion
If your UniFi router is underperforming on a PPPoE connection, implementing the PPPoE Half-Bridge is a highly effective and recommended solution to unlock your true internet speeds.
