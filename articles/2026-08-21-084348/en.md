# AliExpress's Hidden WebAudio Trick Disrupts Bluetooth Multipoint

Discover how AliExpress is silently using WebAudio fingerprinting to keep Bluetooth multipoint connections active, leading to unexpected audio switching and potential user frustration.

## 🔑 The Core of This Topic
AliExpress is employing a technique using WebAudio API to generate constant, imperceptible audio signals. This keeps the browser tab active in the operating system's eyes, preventing Bluetooth devices from switching away from the computer, even when the user intends to switch to a phone.

## ⚡ 5-Second Key Points
- **WebAudio Fingerprinting**: AliExpress uses the WebAudio API to create silent audio streams.
- **Multipoint Disruption**: This keeps the browser tab 'active', tricking Bluetooth into staying connected.
- **User Frustration**: Audio unexpectedly switches, interrupting calls or music playback.

## 📈 Detailed Breakdown
**WebAudio API Usage**
The site leverages the WebAudio API to continuously generate audio data. This process is invisible to the user, with no audible sound produced, but it requires CPU resources and keeps the browser process busy.

**Bluetooth Multipoint**
Bluetooth multipoint allows devices like headphones to connect to two sources simultaneously. Typically, if a call comes in on your phone while listening to music on your laptop, the audio will switch. This AliExpress technique interferes with that expected behavior.

> 💡 Insight: This is an unintended consequence of a technique likely aimed at preventing background tab deactivation, not specifically targeting Bluetooth.

**Browser Tab Activity**
Browsers often de-prioritize or throttle background tabs to save resources. By using WebAudio, AliExpress ensures its tab remains active and resource-intensive, thus preventing the OS from putting it to sleep and inadvertently holding the Bluetooth connection.

## 🎯 Real-World Impact
- Users experience abrupt audio switching from their phone to their computer when the AliExpress tab is open.
- Frustration arises as calls or music are interrupted without user action.
- This behavior can occur even if the user is not actively interacting with the AliExpress page.

## ✨ Conclusion
While the intention might be to keep a browser tab alive, AliExpress's silent WebAudio fingerprinting inadvertently disrupts the seamless experience of Bluetooth multipoint, causing annoyance for users who rely on switching audio sources.
