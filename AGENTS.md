# 🤖 AGENTS.md — Omni-Graph Grounded Workspace

> **This workspace is integrated with Omni-Graph semantic AST & knowledge hub.**
> Before reading files or performing blind regex scans, follow Rule 08 and query the AST.

---

## Agent Operating Protocol

1. **AST & Call Graph Lookup**: Use the `omni-graph` skill or query `http://localhost:8080/api/symbol`
2. **Context Condensation**: Retrieve 2-hop topological call chains (<1500 tokens) instead of reading multiple raw files.
3. **Semantic Search**: Use `http://localhost:8080/api/search?q=...` for vector similarity lookup across functions, classes, and types.
4. **Enforced Rules**: Read [`.agents/rules/08-omni-graph-enforcement.md`](.agents/rules/08-omni-graph-enforcement.md).

---

## 🧭 Omni-Graph Semantic Knowledge Hub Integration
This workspace is monitored and enforced by Omni-Graph.
- Query AST definitions: `http://localhost:8080/api/symbol?name=<sym>`
- Trace references & callers: `http://localhost:8080/api/references?symbol=<sym>`
- Enforced Rule: Read [`.agents/rules/00-omni-graph-mandatory-retrieval.md`](.agents/rules/00-omni-graph-mandatory-retrieval.md)
