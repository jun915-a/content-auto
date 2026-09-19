# 「LLMのセキュリティ脆弱性」を暴く「言語の読みづらさ」の危険性

{
  "ja": "大規模言語モデル（LLM）が「読みづらい入力」に対して脆弱な理由と、それがセキュリティ攻撃や誤操作に繋がるメカニズムを解き明かす。この論文は、LLMが「不正なコード」や「攻撃コマンド」を正しく判別できないリスクを明らかにし、実世界での対策を迫る。エンジニア・セキュリティ研究者必読の最新知見です。",
  "en": "This paper reveals how linguistic illegibility exposes LLM security vulnerabilities, enabling attacks via ambiguous or adversarial inputs. Critical insights for engineers and security researchers to mitigate risks in real-world deployments."
}

{
  "ja": "## 📊 詳細解説\n\n**LLMの「言語理解」はトレーニングデータに依存する**\nLLMは膨大なテキストデータで学習されていますが、そのデータは**「自然な表現」に偏っています**。そのため、「`print(",
  "en": "## 🎯 Key Takeaways in 5 Seconds\n- **LLMs fail to parse illegible inputs**: E.g., distinguishing `exec('malicious_code')` from `# Code execution: exec('malicious_code')` may be impossible.\n- **Attackers exploit hidden commands**: Adversarial inputs with novel phrasing or synonyms bypass LLM defenses.\n- **Current safeguards are inadequate**: Existing filters cannot reliably detect linguistic ambiguity attacks.\n\n"
}
