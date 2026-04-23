# Firefox Tor Identity Leak

A stable Firefox identifier has been found to link all private Tor identities, posing a significant threat to user anonymity and privacy, as explained in a recent blog post by Fingerprint

## 🔑 The Core of This Topic
The core issue lies in Firefox's use of IndexedDB, which allows websites to store data locally on a user's device, potentially compromising the anonymity of Tor users.

## ⚡ 5-Second Key Points
- **Point 1**: Firefox's IndexedDB stores data even in private browsing mode
- **Point 2**: This stored data can be used to identify and track Tor users
- **Point 3**: The vulnerability affects all users of the Tor browser, regardless of their privacy settings

## 📈 Detailed Breakdown
**Element 1**
The use of IndexedDB by Firefox creates a unique identifier for each user, which can be accessed by websites and used to track users across different sessions and browsing modes.

**Element 2**
This identifier can be combined with other data, such as browsing history and search queries, to create a detailed profile of a user's online activities, severely compromising their anonymity.

> 💡 Insight: The fact that this identifier persists even in private browsing mode highlights the severity of the issue and the need for immediate action to protect user privacy.

## 🎯 Real-World Impact
- Users of the Tor browser may be unknowingly revealing their identities to websites and trackers
- The vulnerability can be exploited by malicious actors to compromise the security and anonymity of Tor users
- The issue highlights the need for greater transparency and accountability in browser development and data handling practices

## ✨ Conclusion
The discovery of this vulnerability serves as a reminder of the ongoing struggle to balance online privacy and security with the demands of modern web development, and the need for constant vigilance and innovation in protecting user anonymity
