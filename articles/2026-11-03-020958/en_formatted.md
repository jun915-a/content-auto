# Linux Syscall.sh API Now Supports More Architectures & Kernel Versions

*Insert header image here*

After years of development, the syscall.sh website and API has been fully revamped. Now featuring expanded architecture support, kernel version selection, detailed syscall descriptions, and mobile-friendly improvements—this is the definitive tool for Linux system call exploration.

## 🔑 The Core of This Topic
A **system call (syscall)** is the interface between a running process and the Linux kernel—it’s how applications interact with hardware, manage processes, and control system resources. The syscall.sh project is a **modern, interactive resource** that demystifies these low-level operations, making them accessible to developers, sysadmins, and curious learners alike. With expanded coverage, it now bridges gaps in documentation while offering a **unified view** of syscalls across architectures and kernel versions.

## ⚡ 5-Second Key Points
- **Expanded architecture support**: Now includes **x86_64, ARM64, RISC-V, and more**—previously limited to a few.
- **Kernel version selector**: Compare syscalls across **Linux 4.0 to 6.5+**, revealing deprecated, new, or arch-specific calls.
- **Rich descriptions**: Each syscall now has **contextual explanations**, arguments, and return values—no more cryptic man pages.
- **Mobile-friendly**: Optimized for **touchscreens and smaller screens**, making syscall research on-the-go seamless.
- **API-first**: A **RESTful API** lets developers fetch syscall data programmatically for integration into tools or apps.

## 📈 Detailed Breakdown
**A Unified Syscall Reference Across Architectures**
For years, Linux syscall documentation was fragmented—each architecture (x86, ARM, RISC-V) had its own quirks, and tools like `strace` or `man 2` often left gaps. syscall.sh now **standardizes this knowledge**, presenting syscalls in a **consistent format** regardless of CPU. Whether you’re debugging an ARM-based server or porting code to RISC-V, this resource ensures you **never miss a critical detail**. The inclusion of **64-bit vs. 32-bit variations** (e.g., `openat` vs. `open`) is particularly valuable for cross-platform development.

**Kernel Version Selector: Time-Travel for Syscalls**
One of syscall.sh’s standout features is its **kernel version dropdown**, letting users explore how syscall tables evolved over time. For example, you can see that `epoll_pwait` was introduced in **Linux 2.6.17** or that `process_madvise` (for memory hints) landed in **5.10**. This is **gold for reverse-engineering**—say, when troubleshooting legacy software on an outdated kernel—or for **predicting future changes** in upstream Linux.

> 💡 Insight: **The kernel version selector reveals hidden syscall deprecations**, like `futex` variants removed in newer kernels, forcing developers to adapt their code. This tool acts as a **warning system** for breaking changes.

**Developer-Friendly API for Integration**
Beyond the web interface, syscall.sh offers a **REST API** to fetch syscall data programmatically. Need to build a custom tool that lists available syscalls on a given architecture? The API supports **filtering by architecture, kernel version, or syscall name**, returning structured JSON. This makes it ideal for **automated documentation**, scripting, or even **security research**—imagine scanning for syscall misuse in binaries via an API response.

## 🎯 Real-World Impact
- **Faster Debugging**: Sysadmins can now **quickly identify missing syscalls** in custom kernels or containerized environments, reducing downtime.
- **Cross-Platform Porting**: Developers moving code between **x86, ARM, or RISC-V** can verify syscall compatibility upfront, avoiding runtime crashes.
- **Security Research**: Penetration testers can **map syscall usage** in target binaries to find privilege escalation vectors (e.g., misconfigured `setuid` calls).
- **Education**: Students and self-learners get a **visual, interactive** way to grasp how Linux interacts with hardware—no more dry man pages.

## ✨ Conclusion
syscall.sh has transformed from a niche tool into a **must-have resource** for anyone working with Linux at a low level. By merging **architecture diversity, kernel history, and developer-friendly APIs**, it fills critical gaps in documentation while empowering users to **build, debug, and secure** with confidence. Whether you’re a kernel hacker, a sysadmin, or just curious about how Linux works, this update makes exploring syscalls **easier, faster, and more intuitive** than ever. **Check it out at [syscall.sh](https://syscall.sh/)—your next debugging session might just run smoother.**
