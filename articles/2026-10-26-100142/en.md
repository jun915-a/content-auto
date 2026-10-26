# Steal My Bitcoin PoC: Exploiting Smart Contract Vulnerabilities

Explore the 'Steal My Bitcoin' CTF challenge, a Proof-of-Concept (PoC) demonstrating critical smart contract flaws. Learn how attackers exploit these vulnerabilities to drain funds.

## 🔑 The Core of This Topic
This PoC showcases a smart contract vulnerability that allows an attacker to drain the contract's funds. It highlights common pitfalls in smart contract development, particularly around reentrancy and improper access control, enabling unauthorized fund transfers.

## ⚡ 5-Second Key Points
- **Vulnerability**: Exploits a flaw in the contract's logic for fund withdrawal.
- **Mechanism**: Leverages reentrancy or unchecked external calls to bypass security checks.
- **Outcome**: Successful theft of all Ether locked within the contract.

## 📈 Detailed Breakdown
**The Vulnerability**: The contract contains a function that allows users to withdraw their deposited Ether. However, the check for the withdrawal amount happens *after* the Ether is sent out. This creates a window for a malicious contract to call back into the vulnerable contract before the balance is updated, allowing it to withdraw funds multiple times.

**Exploitation Flow**: An attacker deploys a malicious contract. This contract calls the vulnerable `withdraw` function. Before the vulnerable contract can update the attacker's balance to zero, the malicious contract re-enters the `withdraw` function, effectively draining the contract before its state is properly updated.

> 💡 Insight: The order of operations in smart contracts is critical. Failing to update balances *before* sending funds is a classic and dangerous mistake.

## 🎯 Real-World Impact
- **Financial Loss**: Direct theft of cryptocurrency assets from vulnerable contracts.
- **Reputational Damage**: Loss of trust in the project and its developers.
- **Systemic Risk**: Exploits can cascade, impacting the broader DeFi ecosystem.

## ✨ Conclusion
Understanding and preventing such vulnerabilities is paramount for secure smart contract development. This PoC serves as a vital educational tool for developers to fortify their applications against theft.
