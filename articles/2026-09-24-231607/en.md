# Sourcehut Account Takeover via Cross-Site Scripting in Build Logs

A critical XSS flaw in Sourcehut’s `ansi2html` tool exposed user accounts to takeover. Attackers exploited misconfigured build logs to inject malicious scripts, stealing cookies and hijacking sessions. Discover how this vulnerability worked and its real-world fallout.

## 🔑 The Core of This Topic
A **cross-site scripting (XSS) vulnerability** in Sourcehut’s `ansi2html` library—used to render ANSI-formatted build logs—allowed attackers to inject arbitrary JavaScript into user sessions. By crafting malicious ANSI escape sequences, adversaries could hijack authenticated sessions, effectively taking over accounts. The flaw stemmed from insufficient input sanitization, enabling script execution in trusted contexts like build logs, a critical oversight in a platform hosting sensitive developer workflows.

## ⚡ 5-Second Key Points
- **Unsanitized ANSI input**: Attackers injected malicious ANSI escape codes into build logs.
- **Session hijacking**: Exploited XSS to steal cookies via `document.cookie`.
- **No user action required**: Victims were compromised automatically when viewing logs.

## 📈 Detailed Breakdown
**Element 1**
The vulnerability resided in `ansi2html`, a tool converting ANSI-formatted text (common in build outputs) into HTML. When processing user-submitted input—like custom build scripts—it failed to strip or escape dangerous ANSI escape sequences. These sequences could embed `<script>` tags or execute JavaScript, bypassing browser security restrictions.

**Element 2**
Attackers leveraged this by submitting payloads like `\033]8;;https://evil.com/x.js\033\\` into build logs. When rendered, the payload triggered a browser alert or cookie theft, demonstrating how ANSI sequences could hijack sessions without user interaction. The lack of Content Security Policy (CSP) headers further exacerbated the risk.

> 💡 Insight: **Third-party libraries often inherit security flaws**—even trusted tools like `ansi2html` can become attack vectors if misconfigured.

## 🎯 Real-World Impact
- **Account takeovers**: Attackers stole cookies to impersonate users, accessing private repositories and messages.
- **Trust erosion**: Users lost confidence in Sourcehut’s security, despite the platform’s reputation for developer privacy.
- **Patch urgency**: The vulnerability required immediate fixes to `ansi2html` and Sourcehut’s build log rendering pipeline.

## ✨ Conclusion
This exploit underscores the importance of **input sanitization** and **CSP enforcement** in web applications. Developers must assume all user input is malicious until proven safe. Sourcehut’s response—patching the library and hardening log rendering—serves as a reminder that even niche tools can harbor critical flaws. Always audit third-party dependencies and validate sanitization mechanisms.
