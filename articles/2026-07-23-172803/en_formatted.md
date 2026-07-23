# Run OCI Images as Containers or Firecracker MicroVMs with PullRun

*Insert header image here*

PullRun lets you deploy any OCI container image as either a lightweight container or a secure Firecracker microVM—without rewriting code or juggling tools.

{
  "## 🔑 The Core of This Topic": "PullRun bridges containers and microVMs by letting you run the same OCI image in both modes. It leverages Firecracker’s isolation for security-critical workloads while keeping the simplicity of container workflows.",
  "## ⚡ 5-Second Key Points": "- **Unified deployment**: Same OCI image works as a container or Firecracker microVM\n- **Zero rewrites**: No need to modify your application or Dockerfile\n- **Security on demand**: Switch to microVMs for stronger isolation when needed\n- **Tooling agnostic**: Works with existing container workflows and registries\n- **Fast start**: MicroVMs boot in milliseconds, matching container startup times",
  "## 📈 Detailed Breakdown": "**Element 1**\nPullRun abstracts away the complexity of Firecracker by treating microVMs like containers. Developers push their OCI images to any registry just as they would for Kubernetes or Docker. The tool then decides—based on policies or manual flags—whether to run it as a container or a microVM. This eliminates the need for separate pipelines or image variants, streamlining deployment across environments.\n\n**Element 2**\nUnder the hood, PullRun uses Firecracker’s lightweight virtualization to create microVMs with minimal overhead. Unlike traditional VMs, these boot in milliseconds and consume resources proportional to the workload. The tool also handles networking, storage, and lifecycle management automatically, so users get microVM benefits without manual configuration. This makes it ideal for security-sensitive tasks like multi-tenant isolation or confidential computing.",
  "> 💡 Insight: PullRun turns Firecracker from a niche tool into a drop-in replacement for containers, offering a pragmatic path to stronger isolation without sacrificing developer experience or operational simplicity. \n\n## 🎯 Real-World Impact": "- **Security teams** can deploy services in microVMs for workloads handling sensitive data, without rewriting applications or maintaining separate VM images.\n- **DevOps teams** simplify pipelines by using one toolchain for both containers and microVMs, reducing tool sprawl and onboarding time.\n- **Cloud providers** can offer isolated compute options to customers without forcing them to adopt new image formats or tooling.",
  "## ✨ Conclusion": "PullRun proves that you don’t have to choose between containers and microVMs—you can have both, deployed from the same OCI image. It’s a game-changer for teams that need flexibility, security, and simplicity in equal measure.",
  "tags": [
    "Firecracker",
    "OCI containers",
    "microVMs"
  ]
}
