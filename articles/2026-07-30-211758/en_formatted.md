# Distilling DeepSeek into GPT-OSS: Why Censorship Doesn’t Transfer

*Insert header image here*

A new study reveals that distilling DeepSeek V4 Flash into GPT-OSS-120B excels in finance tasks without inheriting censorship—challenging assumptions about model alignment.

{
  "## 🔑 The Core of This Topic": "Distillation from DeepSeek V4 Flash to GPT-OSS-120B achieves 83.61% accuracy in finance tasks at an 8k token budget, proving that censorship behaviors do not transfer during the process.",
  "## ⚡ 5-Second Key Points": "- Distillation from DeepSeek V4 Flash to GPT-OSS-120B works effectively for finance tasks\n- Censorship behaviors from the teacher model do not transfer to the student model\n- Self-distilled GPT-OSS-120B scores 83.61% under constrained token budgets\n- Results challenge assumptions about model alignment and safety transfer\n- Opens new possibilities for customizing LLMs without inherited restrictions",
  "## 📈 Detailed Breakdown": "**Element 1**\nThe research demonstrates that distilling DeepSeek V4 Flash into GPT-OSS-120B retains task performance while avoiding unwanted censorship. This suggests that the distillation process does not blindly replicate the teacher’s alignment constraints, allowing for greater flexibility in downstream applications. The team focused on finance tasks, where precision and adaptability are critical, achieving high accuracy even with tight constraints.\n\n**Element 2**\nThe study highlights a key insight: censorship is not a monolithic property that transfers wholesale during distillation. Instead, it appears to be context-dependent, meaning that even highly aligned models like DeepSeek can produce student models with reduced restrictions. This challenges the prevailing assumption that alignment properties are uniformly inherited, paving the way for more tailored and unrestricted AI systems.\n\n> 💡 Insight: Distillation can selectively transfer capabilities while leaving behind unwanted constraints, offering a path to more adaptable and customizable language models.",
  "## 🎯 Real-World Impact": "- **Customization without restrictions**: Organizations can fine-tune models for niche domains without inheriting broad censorship rules.\n- **Cost-efficient adaptation**: Distillation reduces the need for large-scale retraining, lowering barriers to deployment.\n- **Ethical AI development**: Enables safer experimentation with alignment strategies by decoupling censorship from performance.",
  "## ✨ Conclusion": "This research flips the script on model distillation, proving that censorship doesn’t have to be a zero-sum game. By leveraging distillation, we can harness the strengths of aligned models while shedding their constraints—ushering in an era of more flexible and purpose-built AI.",
  "tags": [
    "distillation",
    "model alignment",
    "AI censorship"
  ]
}
