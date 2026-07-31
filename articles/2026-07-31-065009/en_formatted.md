# DeepSeek to GPT-OSS Distillation Fails to Transfer Censorship—Here’s Why

*Insert header image here*

A new study reveals that distilling DeepSeek’s outputs into GPT-OSS doesn’t inherit its censorship filters. Finance tasks show surprising success despite this gap.

## 🔑 The Core of This Topic
Distilling large language models (LLMs) like DeepSeek V4 Flash into smaller architectures such as GPT-OSS-120B excels at finance tasks but **fails to transfer censorship**, according to fresh research. This mismatch could reshape how we approach model alignment and safety in AI development.

## ⚡ 5-Second Key Points
- **Distillation works for finance**: Self-distilled GPT-OSS-120B scores 83.61% on finance tasks under an 8k token budget.
- **Censorship doesn’t transfer**: DeepSeek’s safety filters aren’t inherited by GPT-OSS, raising ethical concerns.
- **Niche but critical**: Finance is just one domain—implications may extend to other regulated fields.
- **Budget constraints matter**: Performance holds even with constrained token limits, proving efficiency.
- **A wake-up call for AI safety**: Developers must rethink how safety mechanisms are propagated in distilled models.

## 📈 Detailed Breakdown
**Element 1**
Researchers used DeepSeek V4 Flash as a teacher model to generate outputs for finance-specific tasks. The distilled GPT-OSS-120B model then learned from these outputs, achieving strong performance (83.61%) while operating under tight computational constraints (8k tokens). This suggests distillation can preserve task-specific accuracy even with limited resources.

**Element 2**
Critically, the study found that censorship mechanisms—such as content moderation or safety filters—**did not transfer** from DeepSeek to GPT-OSS. Unlike task-specific knowledge, these filters appear to be model-specific traits that aren’t easily distilled into other architectures. This raises questions about the reliability of safety-aligned models in downstream applications.

> 💡 Insight: Distillation transfers task performance but not ethical or safety constraints, forcing developers to explicitly design safeguards for each new model.

## 🎯 Real-World Impact
- **Regulated industries at risk**: Finance, healthcare, and legal sectors rely on censorship for compliance—distilled models may fail to meet these standards.
- **Ethical AI gaps**: Users may unknowingly deploy models that bypass safety filters, leading to harmful outputs.
- **Rethinking alignment**: Teams must implement post-distillation safety checks, increasing development complexity and costs.

## ✨ Conclusion
Distilling DeepSeek into GPT-OSS proves that **task excellence doesn’t guarantee safety**. As AI models shrink and proliferate, developers must prioritize transparent alignment strategies—or risk deploying unsafe systems at scale.
