# Apple Silicon Meets AI: A 20B MoE Model Runs on iPhone at 120 Tokens/Sec

A breakthrough in edge AI: Maple-Preview delivers a 20B parameter MoE model running at 120 tokens per second on an iPhone, unlocking new possibilities for on-device intelligence.

{
  "## 🔑 The Core of This Topic": "Maple-Preview marks a milestone in mobile AI by running a ternary 20-billion-parameter Mixture-of-Experts (MoE) model at **120 tokens per second** on an iPhone. This achievement blurs the line between cloud and edge computing, proving high-performance AI is now possible without internet dependency.",
  "## ⚡ 5-Second Key Points": [
    "**-20B parameters** optimized into a ternary MoE model, reducing computational load.",
    "**-120 tokens/sec** inference speed on an iPhone, rivaling some cloud-based systems.",
    "**-No cloud required**—fully local execution with no latency or privacy trade-offs.",
    "- Leverages **Apple Silicon** (A16/A17 chips) for efficient parallel processing.",
    "- Opens doors for **real-time AI** apps like offline chatbots and on-device transcription."
  ],
  "## 📈 Detailed Breakdown": {
    "**Element 1**": "The **ternary MoE architecture** is the secret sauce behind Maple-Preview’s performance. Unlike dense models, MoE systems activate only a subset of parameters (experts) per inference, drastically cutting memory and compute demands. By quantizing weights to ternary values (-1, 0, 1), the model achieves a **3x reduction in memory bandwidth**, crucial for mobile hardware. This innovation allows the 20B model to fit within the iPhone’s RAM constraints while maintaining speed.",
    "**Element 2**": "Apple’s **A-series chips** (A16/A17) are uniquely suited for this task. Their **Neural Engine** accelerates matrix operations, while the unified memory architecture minimizes data transfer bottlenecks. Maple-Preview’s developers optimized the MoE routing mechanism to align with the Neural Engine’s parallel processing strengths, achieving **120 tokens/sec**—faster than many cloud-based solutions. The model’s **local execution** also eliminates privacy concerns, as no data leaves the device.",
    "> 💡 Insight: Maple-Preview proves that **edge AI isn’t just feasible—it’s already outperforming cloud alternatives** in latency and privacy. The shift from cloud-dependent to on-device AI could redefine how we interact with technology daily.": "",
    "## 🎯 Real-World Impact": [
      "**-Offline AI assistants****: Imagine Siri or a custom chatbot responding instantly without internet, perfect for remote areas or during connectivity outages.",
      "- **Enhanced privacy**: Medical, financial, or personal data stays on-device, reducing risks of breaches or surveillance.",
      "- **New app categories**: Real-time translation, on-device image generation, or even **AI-powered photography** could become mainstream with such performance."
    ],
    "## ✨ Conclusion": "Maple-Preview isn’t just another AI demo—it’s a **paradigm shift**. By running a 20B model on an iPhone at 120 tokens/sec, it shatters the myth that cutting-edge AI requires massive servers. The future of AI is here, and it fits in your pocket. Developers, take note: the era of **ubiquitous, private, and lightning-fast AI** has arrived.",
    "tags": [
      "edge AI",
      "iPhone",
      "Mixture of Experts"
    ]
  }
}
