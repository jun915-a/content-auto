# The Tooltip Accessibility Mistake You're Probably Making

*Insert header image here*

Discover the subtle but critical flaw in many tooltips that breaks screen reader usability—and how to fix it in under 5 minutes.

{
  "## 🔑 The Core of This Topic": "Tooltips often rely on hover events, excluding keyboard and screen reader users. The solution isn’t just ARIA—it’s about proper focus management and semantic structure.",
  "## ⚡ 5-Second Key Points": "- **Use `role=\"tooltip\"`** for semantic clarity\n- **Pair with `aria-describedby`** to link tooltip to trigger\n- **Ensure keyboard accessibility** with `tabindex` and focus states\n- **Avoid relying on hover alone**—support focus and click\n- **Test with screen readers** to confirm usability",
  "## 📈 Detailed Breakdown": "**Why ARIA isn’t enough**\nTooltips without proper focus management create a dead zone for keyboard users. Screen readers need explicit connections between the trigger and tooltip content, which `aria-describedby` provides. Without it, tooltips become invisible to assistive tech, even with ARIA roles like `role=\"tooltip\"`.\n\n> 💡 Insight: The best tooltips are accessible by default—no JavaScript required. Start with semantic HTML, then enhance with ARIA only if necessary.\n\n**The role of `tabindex` and focus**\nTooltips triggered by hover exclude users who navigate via keyboard. Adding `tabindex=\"0\"` to interactive elements lets focus reach the trigger, but it must pair with visible focus indicators. For custom tooltips, JavaScript should handle both `focus` and `mouseenter` events, ensuring parity between input methods.",
  "## 🎯 Real-World Impact": "- **Legal compliance**: WCAG 2.1 requires tooltips to be accessible via keyboard.\n- **User reach**: Fixing this mistake expands your tooltips to millions of users who rely on assistive tech.\n- **UX consistency**: Ensures tooltips work the same way for everyone, reducing frustration.",
  "## ✨ Conclusion": "Accessibility isn’t an afterthought—it’s a foundation. By treating tooltips as first-class citizens in your UI, you ensure no user is left behind. Start with semantic HTML, test with screen readers, and your tooltips will work for everyone.",
  "tags": [
    "accessibility",
    "tooltips",
    "WCAG"
  ]
}
