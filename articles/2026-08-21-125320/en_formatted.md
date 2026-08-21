# AliExpress's Silent WebAudio Trick Disrupts Bluetooth Multipoint

*Insert header image here*

AliExpress is using WebAudio fingerprinting to bypass Bluetooth multipoint connections, forcing users to manually switch devices. Discover how this impacts your audio experience.

## 🔑 The Core of This Topic
AliExpress employs a technique leveraging the WebAudio API to identify and maintain a persistent connection to specific Bluetooth devices, effectively circumventing the intended functionality of Bluetooth multipoint which allows seamless switching between audio sources.

## ⚡ 5-Second Key Points
- **Silent Fingerprinting**: AliExpress uses WebAudio to identify and lock onto audio devices.
- **Multipoint Disruption**: This breaks the ability to switch audio sources automatically.
- **User Annoyance**: Requires manual reconnection, disrupting user experience.

## 📈 Detailed Breakdown
**WebAudio API Usage**
AliExpress's website utilizes the WebAudio API, a powerful tool for audio processing, to generate unique identifiers for connected Bluetooth audio devices. This process happens in the background without user interaction.

**Bypassing Multipoint**
By persistently identifying and 'claiming' a specific audio device via WebAudio, the site prevents it from being recognized by other connected devices, thus disabling the seamless switching that multipoint is designed for.

> 💡 Insight: This method exploits a feature of WebAudio, not a direct Bluetooth vulnerability, to achieve an unintended consequence.

## 🎯 Real-World Impact
- Users with multipoint headphones (e.g., connected to a laptop and phone) will find their audio stuck on the AliExpress tab/window.
- Switching to a phone call or another audio source requires manually disconnecting and reconnecting the headphones.
- The website effectively hijacks the audio output, causing significant frustration for users expecting smooth transitions.

## ✨ Conclusion
AliExpress's implementation of WebAudio fingerprinting is a user-unfriendly tactic that degrades the experience for those relying on Bluetooth multipoint. It's a stark reminder of how web technologies can inadvertently impact hardware functionalities.
