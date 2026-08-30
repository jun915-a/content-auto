# Is Calling print() in a Python Signal Handler Safe?

Signal handlers in Python are tricky—calling print() may seem harmless, but it can lead to unexpected crashes or undefined behavior due to race conditions and async-signal-unsafe functions.

{
  "## 🔑 The Core of This Topic": "Signal handlers in Python run asynchronously when a signal is received, and calling print() inside them can corrupt Python's internal state. The C standard (and thus Python's signal handling) considers many functions, including print(), **async-signal-unsafe**, making them dangerous to invoke directly in a handler.",
  "## ⚡ 5-Second Key Points": [
    "**print() is not signal-safe**: The function relies on Python's internal locks and heap, which can be in an inconsistent state during signal handling.",
    "**Race conditions**: Signals can interrupt Python at any point, leading to data corruption if shared resources (like stdout) are modified.",
    "**Use signal-safe alternatives**: Prefer async-signal-safe functions like write() or set a flag to handle signals safely in the main loop."
  ],
  "## 📈 Detailed Breakdown": {
    "**Element 1**": "Python’s signal handling mechanism is built on top of the C runtime, which marks functions like `printf` (and by extension `print()`) as **async-signal-unsafe**. This means they can cause undefined behavior if called in a signal handler. The issue stems from the fact that signals can interrupt Python’s interpreter at any time, potentially leaving internal data structures (like the GIL or memory allocator) in an inconsistent state. When `print()` tries to acquire locks or modify shared resources, it risks deadlocks, crashes, or corrupted output.",
    "**Element 2**": "Even if your program doesn’t crash immediately, calling `print()` in a signal handler can lead to subtle bugs. For example, if the signal arrives while Python is in the middle of writing to `stdout`, the output could be interleaved or truncated. Worse, it might corrupt Python’s internal state, causing silent failures later. The **Portable Operating System Interface (POSIX)** standard explicitly restricts signal handlers to a small set of safe functions, and `print()` isn’t on that list.",
    "> 💡 Insight: Always treat signal handlers as the bare minimum—set a flag or log the signal event asynchronously, then handle it in the main thread where Python’s safety guarantees apply.": "## 🎯 Real-World Impact"
  },
  "- **Data Corruption**: Programs may crash or produce inconsistent output if signals interrupt critical sections of code during `print()`. This is especially dangerous in long-running applications like servers or real-time systems where signal handlers are used for timeouts or interrupts.\n- **Silent Failures**: Errors from unsafe `print()` calls might not crash the program immediately but could cause subtle bugs, making them hard to debug. For example, a signal could corrupt Python’s internal state, leading to crashes hours later with no clear cause.\n- **Portability Issues**: Code relying on `print()` in signal handlers may work on some systems (where the signal happens to arrive at a safe time) but fail unpredictably on others, making it unreliable for production environments.": "## ✨ Conclusion"
}
