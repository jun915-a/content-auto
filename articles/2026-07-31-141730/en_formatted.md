# Distilling Censorship, Not Intelligence: Unlocking GPT-OSS's Full Potential

*Insert header image here*

We explore the surprising result of distilling DeepSeek into GPT-OSS, achieving impressive finance task scores without transferring censorship.

## 🔑 The Core of This Topic
Deep learning models, like GPT-OSS, are trained on vast datasets that may contain biases and even censorship. However, our recent experiment showed that distilling DeepSeek V4 Flash, a teacher model, into GPT-OSS-120B didn't transfer censorship, but rather improved task performance.

## ⚡ 5-Second Key Points
- **Point 1**: We achieved an impressive 83.61% score on finance tasks with a constrained 8k token budget.
- **Point 2**: Our self-distilled 120B model outperformed the original model on finance tasks.
- **Point 3**: The distillation process didn't transfer censorship from the teacher model.

## 📈 Detailed Breakdown
Our experiment used DeepSeek V4 Flash as a teacher for finance tasks with GPT-OSS-120B. The distillation process worked well on this problem, and we were able to achieve a score of 83.61% on finance tasks with a constrained 8k token budget.

The distillation process involved training a smaller model on the teacher model's output, and then fine-tuning the smaller model to match the teacher model's performance. This process allowed us to capture the teacher model's knowledge and transfer it to the GPT-OSS-120B model.

> 💡 Insight: The distillation process didn't transfer censorship, but rather improved task performance, suggesting that the teacher model's biases and censorship were not inherent to its intelligence.

## 🎯 Real-World Impact
- This result has significant implications for the development of large language models, as it suggests that distillation can be used to transfer knowledge without transferring biases and censorship.
- The ability to distill teacher models without transferring censorship opens up new possibilities for using large language models in sensitive applications, such as finance and healthcare.
- The results of this experiment also highlight the potential of using smaller models as teachers for larger models, reducing computational resources and costs.

## ✨ Conclusion
Our experiment showed that distilling DeepSeek V4 Flash into GPT-OSS-120B didn't transfer censorship, but rather improved task performance. This result has significant implications for the development of large language models and opens up new possibilities for using them in sensitive applications.
