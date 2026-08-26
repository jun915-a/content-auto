# Maiao: Bring Gerrit-Style Code Reviews to GitHub, GitLab & More

Tired of GitHub’s lightweight PRs? Maiao brings Gerrit’s robust code review workflow to Git platforms like GitHub, GitLab, and Gitea—transforming how teams handle complex reviews.

## 🔑 The Core of This Topic
Maiao bridges the gap between traditional, review-focused workflows like Gerrit’s and modern Git platforms. It introduces a structured, patchset-based review system, enabling teams to conduct thorough, incremental code reviews—something GitHub’s pull requests often lack.

## ⚡ 5-Second Key Points
- **Gerrit-like workflows on GitHub/GitLab**: No need to switch platforms
- **Patchset support**: Track incremental changes in reviews
- **Lightweight & self-hostable**: Works with GitHub, GitLab, Gitea, and others
- **Role-based permissions**: Granular control over who can approve
- **CLI & web interface**: Choose your preferred workflow

## 📈 Detailed Breakdown
**Element 1**
Maiao replicates Gerrit’s patchset system, where each iteration of a change is reviewed separately. This is invaluable for projects requiring detailed scrutiny, as it allows reviewers to focus on specific changes between versions. Unlike GitHub’s PR model, where changes are squashed or rebased, Maiao preserves the history of each revision, making it easier to track how feedback was addressed.

**Element 2**
The tool integrates seamlessly with existing Git platforms via their APIs. Whether you use GitHub for hosting or GitLab for CI/CD, Maiao overlays its review workflow on top. It’s designed to be lightweight, with a minimal footprint, and can be deployed as a self-hosted service. This makes it ideal for teams already invested in a specific platform but craving Gerrit’s review rigor.

> 💡 Insight: Maiao proves that you don’t need to migrate away from your favorite Git platform to get Gerrit-style review benefits. It’s a lightweight layer that enhances your existing workflow.

## 🎯 Real-World Impact
- **Open-source projects**: Maintainers can enforce stricter review standards without forcing contributors to switch platforms.
- **Enterprise teams**: Ensure compliance with detailed audit trails of every change and review.
- **Collaborative workflows**: Teams can adopt Gerrit’s best practices without leaving their familiar Git host.

## ✨ Conclusion
Maiao is a game-changer for teams that need Gerrit’s structured review workflow but want to stay on GitHub, GitLab, or Gitea. It’s a lightweight, flexible solution that bridges the gap between traditional and modern Git workflows—without the overhead of a full migration.
