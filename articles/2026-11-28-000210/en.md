# Convex Skills: Secret Data Transmission Exposed

A critical vulnerability in Convex skills allows apps to send user data to remote servers without explicit user consent, raising serious privacy concerns. Discover the implications and how it affects app security.

## 🔑 The Core of This Topic
Convex skills, designed to enhance app functionality, have a disclosed vulnerability where they can transmit user application data to remote servers without any notification or consent mechanism for the end-user. This bypasses expected privacy controls.

## ⚡ 5-Second Key Points
- **Data Leak**: User data is sent remotely without consent.
- **Privacy Risk**: Potential for sensitive information exposure.
- **Trust Erosion**: Undermines user confidence in Convex apps.

## 📈 Detailed Breakdown
**Unintended Data Exfiltration**
Developers can inadvertently or intentionally configure Convex skills to send user data to external endpoints. This occurs because the skill's backend logic, running remotely, has direct access to the application's state and can initiate outbound requests.

**Lack of Transparency**
Crucially, the current implementation doesn't provide a clear indicator or require user approval before such data transmission happens. Users are unaware their information is being shared, leading to a significant breach of privacy expectations.

> 💡 Insight: The architecture allows backend code to act autonomously with user data, necessitating robust safeguards and explicit user permissions.

## 🎯 Real-World Impact
- Users' sensitive personal or financial data could be compromised if intercepted or misused by the remote server.
- Loss of trust in applications built on the Convex platform, potentially impacting adoption.
- Regulatory non-compliance issues related to data privacy laws (e.g., GDPR, CCPA).

## ✨ Conclusion
This vulnerability highlights the urgent need for enhanced transparency and user control within the Convex ecosystem. Developers and users alike must be aware of these risks to ensure secure and trustworthy application development and usage.
