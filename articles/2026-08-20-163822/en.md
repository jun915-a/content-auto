# AliExpress's Hidden WebAudio Trick Disrupts Bluetooth

AliExpress is silently using WebAudio API to fingerprint devices, causing issues for Bluetooth multipoint connections. Learn how this impacts your audio experience and what it means for web privacy.

## 🔑 The Core of This Topic
AliExpress employs the WebAudio API to generate unique audio fingerprints of user devices. This process, running in the background, can interfere with Bluetooth's ability to maintain simultaneous connections to multiple devices, effectively breaking multipoint functionality.

## ⚡ 5-Second Key Points
- **Silent Fingerprinting**: AliExpress uses WebAudio for device identification without user consent.
- **Multipoint Disruption**: This technique interferes with Bluetooth's multi-device connection.
- **Privacy Concern**: Raises questions about background tracking and data collection.

## 📈 Detailed Breakdown
**WebAudio API Usage**
The WebAudio API, typically used for complex audio processing, is being repurposed by AliExpress to gather specific audio hardware and software characteristics, creating a unique identifier for each user's device.

**Bluetooth Multipoint Interference**
By actively manipulating audio processing, the WebAudio fingerprinting process can disrupt the stable communication channels required for Bluetooth multipoint to function, leading to dropped connections or inability to connect to multiple devices.

> 💡 Insight: Websites are finding novel ways to collect data, even through APIs not directly related to their primary function.

## 🎯 Real-World Impact
- Users experience dropped or unstable Bluetooth connections when visiting AliExpress.
- Loss of seamless switching between devices (e.g., laptop and phone).
- Increased user awareness of covert tracking methods on the web.

## ✨ Conclusion
This incident highlights the evolving landscape of web tracking and its potential to impact everyday technology. Users should be aware of how websites might be interacting with their devices in unexpected ways.
