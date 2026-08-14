# Discovering Encrypted DNS

*Insert header image here*

Learn how devices can find hidden encrypted DNS servers on their own.

## 🔑 The Core of This Topic
Device discovery of encrypted DNS involves a process called Device Discovery and Response (DDR). DDR is a method used by devices to search for encrypted DNS servers without any prior knowledge of their existence.

## ⚡ 5-Second Key Points
- **Point 1**: Devices broadcast a query for potential DNS server addresses.
- **Point 2**: Potential DNS servers respond with their encrypted DNS server addresses.
- **Point 3**: Devices select the best encrypted DNS server based on the responses received.

## 📈 Detailed Breakdown
**Element 1**: When a device initiates the DDR process, it sends a broadcast query for potential encrypted DNS server addresses. This query is typically sent over the local network, and it's not specific to a particular DNS server or domain.

**Element 2**: Potential encrypted DNS servers on the network receive the broadcast query and respond with their encrypted DNS server addresses. These responses are typically sent back to the device that initiated the query.

> 💡 Insight: The DDR process allows devices to discover encrypted DNS servers without any prior knowledge of their existence, making it easier for devices to switch to encrypted DNS.

## 🎯 Real-World Impact
- Improved security through encrypted DNS.
- Enhanced user privacy.
- Better protection against DNS spoofing and manipulation.

## ✨ Conclusion
By leveraging the DDR process, devices can find and connect to encrypted DNS servers on their own, enhancing overall security and user privacy.
