# Rack-Level Security: A Key-Hierarchy Strategy for Control

Discover how Oxide Computer’s **key-hierarchy strategy** redefines rack-level security. Minimize single points of failure while maximizing access control—without sacrificing usability. A must-read for cloud architects and DevOps engineers.

**🔑 The Core of This Topic**

This RFC explores a **hierarchical key management system** for rack-level security, designed to distribute control while eliminating blind spots. Inspired by Oxide’s hardware-backed security model, it ensures that keys—whether for physical access, cryptographic operations, or system integrity—are **never siloed in a single place**. The goal? **Decentralized authority without sacrificing accountability**, reducing the risk of catastrophic failures or insider threats.

**⚡ 5-Second Key Points**

- **Point 1**: **Multi-tiered key distribution**—rack-level, device-level, and user-level keys operate in isolation, reducing exposure.
- **Point 2**: **Hardware-enforced boundaries**—physical keys (e.g., for rack access) are tied to cryptographic keys, preventing unauthorized replication.
- **Point 3**: **Just-in-time revocation**—compromised keys can be invalidated dynamically, even if the physical key is lost or stolen.

**📈 Detailed Breakdown**

**Element 1: Hierarchical Key Domains**

The strategy divides keys into **three domains**: *rack*, *device*, and *user*. A **rack key** controls access to the entire infrastructure, while **device keys** govern individual servers or components. **User keys** (e.g., SSH or API tokens) are derived from these but **cannot reconstruct higher-level keys**. This prevents a single breach from cascading—if a user key is compromised, only their access is revoked, not the entire rack.

**Element 2: Physical + Cryptographic Synergy**

Physical keys (e.g., for biometric or RFID-based rack access) are **bound to cryptographic keys** stored in secure enclaves. When a user inserts a physical key, their device generates a **temporary cryptographic token** tied to the rack’s master key. This ensures that even if a physical key is cloned, the cryptographic link prevents unauthorized use without the corresponding digital credential.

> 💡 **Insight**: *The separation of physical and cryptographic keys creates a “defense in depth” model—an attacker must compromise both layers to escalate privileges.*

**🎯 Real-World Impact**

- **Impact 1**: **Reduced blast radius**—compromised user credentials or lost devices no longer risk entire racks, as keys are scoped hierarchically.
- **Impact 2**: **Simplified auditing**—clear separation of duties means logs can trace access from *user → device → rack* without ambiguity.
- **Impact 3**: **Future-proofing**—the model adapts to new threats (e.g., quantum-resistant cryptography) by isolating key updates at each level.

**✨ Conclusion**

Oxide’s key-hierarchy strategy isn’t just about security—it’s about **control**. By distributing authority without decentralizing accountability, organizations can build infrastructures where **keys are invisible until needed**, yet **unforgettable when compromised**. For teams balancing security with usability, this approach offers a **practical, scalable path forward**—one where the keys to your kingdom are always under lock and key.
