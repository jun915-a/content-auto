# macOS Git Still Trusts Flawed eMudhra Certificates

Ten days after a major security flaw was revealed, Git on macOS continues to trust compromised eMudhra certificates, posing a significant risk to developers and their sensitive data.

## 🔑 The Core of This Topic
The root cause is that macOS, and consequently Git which relies on the system's trust store, has not yet revoked trust for specific eMudhra root certificates. These certificates were found to be improperly issued, allowing for the potential creation of fraudulent SSL/TLS certificates, thereby undermining secure connections.

## ⚡ 5-Second Key Points
- **Compromised Certificates**: eMudhra issued certificates that did not adhere to security standards.
- **macOS Trust Issue**: Apple's systems, including Git, haven't fully revoked trust for these flawed certificates.
- **Ongoing Risk**: Developers using Git on affected macOS systems remain vulnerable to man-in-the-middle attacks.

## 📈 Detailed Breakdown
**eMudhra's Certificate Issuance**: eMudhra, a licensed Certificate Authority (CA), issued digital certificates that were found to be insecure. This breach of trust means that certificates issued under these roots could be forged by malicious actors, making it difficult to verify the authenticity of websites and services.

**macOS and Git's Reliance on System Trust**: Git, when performing operations like cloning or fetching from remote repositories over HTTPS, relies on the underlying operating system's trust store to validate the server's certificate. If the OS continues to trust a compromised root CA, Git will also implicitly trust certificates issued by it.

> 💡 Insight: The delay in revoking trust for these certificates highlights a critical vulnerability in how operating systems manage and update their trusted certificate authorities, leaving users exposed.

## 🎯 Real-World Impact
- **Man-in-the-Middle Attacks**: Attackers could impersonate legitimate Git servers, intercepting sensitive code or credentials.
- **Data Breach Risk**: Compromised certificates could be used to trick developers into submitting code or data to malicious repositories.
- **Erosion of Trust**: Developers may lose confidence in the security of their development workflows and the tools they rely on.

## ✨ Conclusion
This ongoing vulnerability underscores the urgent need for swift action from Apple and other vendors to ensure their systems fully disallow trust for compromised CAs, protecting the integrity of secure communications for all users.
