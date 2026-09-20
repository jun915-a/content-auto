# How to Measure Internet Censorship: Tools & Methods

Understand how internet censorship is detected and measured using open-source tools like OONI. Learn techniques, challenges, and real-world applications to monitor digital freedom globally.

## 🔑 The Core of This Topic
Internet censorship refers to the deliberate restriction or blocking of access to online content, services, or communication platforms by governments, ISPs, or other entities. Measuring censorship involves detecting these restrictions, analyzing their scope, and documenting their impact on digital rights. Open-source initiatives like the **Open Observatory of Network Interference (OONI)** provide tools to systematically assess internet freedom by testing for blocked websites, DNS tampering, and network interference.

## ⚡ 5-Second Key Points
- **Point 1**: Use **OONI Probe** to test for blocked websites, DNS censorship, or network interference by running automated scans from your device.
- **Point 2**: **Collaborative data** from global volunteers helps map censorship patterns and track changes over time.
- **Point 3**: Censorship measurement reveals **real-time threats** to free expression, enabling advocacy and policy responses.

## 📈 Detailed Breakdown
**Element 1**
OONI’s **Probe** is a free, open-source tool that tests for internet censorship by sending HTTP requests, DNS queries, and TCP connections to predefined test targets. It detects blocks by comparing expected responses (e.g., a website loading) with actual outcomes (e.g., a timeout or HTTP 403 error). The tool is designed to be lightweight, running on smartphones, laptops, or servers worldwide. Its modularity allows users to extend tests for **circumvention tools** (like VPNs or Tor) or **deep packet inspection** (DPI) techniques.

**Element 2**
The **OONI Explorer** dashboard visualizes censorship data collected from thousands of contributors. It maps blocked websites, DNS filtering, and network interference by country or region, revealing patterns like **geographic targeting** or **temporary surges** during protests. For example, during the 2019 Hong Kong protests, OONI data showed **massive spikes in blocked social media platforms**, correlating with government crackdowns. This data is crucial for journalists, activists, and policymakers to respond to censorship events.

> 💡 Insight: **Anonymity matters**—OONI tests often use Tor or VPNs to avoid retaliation against testers in high-censorship regimes. However, even with anonymity, some regimes employ **technical countermeasures** (e.g., blocking Tor exit nodes) to evade detection.

## 🎯 Real-World Impact
- **Exposing government overreach**: OONI’s 2020 report on **India’s internet shutdowns** during farmer protests revealed **widespread blocking of messaging apps** (WhatsApp, Telegram) and news sites, forcing global condemnation.
- **Empowering activists**: In **Iran**, OONI data helped protesters bypass **IP-based blocks** by identifying alternative exit nodes for VPNs during 2022’s protests.
- **Legal and policy leverage**: Courts and human rights organizations cite OONI’s evidence to **challenge internet shutdowns** (e.g., in **Ethiopia’s Tigray conflict**), arguing they violate free speech rights.

## ✨ Conclusion
Measuring internet censorship is a **collective effort**—citizens, researchers, and organizations must collaborate to expose violations of digital rights. Tools like OONI Probe democratize censorship monitoring, turning individual devices into sensors for global freedom. While challenges like **counter-censorship tactics** and **data privacy** persist, the growing body of evidence strengthens advocacy for open, uncensored internet. **Your contribution could be the data that changes policies—start testing today.**
