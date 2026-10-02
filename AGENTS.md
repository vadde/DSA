# 🤖 AGENTS.md — Omni-Graph Grounded Workspace

> **This workspace is integrated with Omni-Graph semantic AST & knowledge hub.**
> Before reading files or performing blind regex scans, follow Rule 08 and query the AST.

---

## Agent Operating Protocol

1. **AST & Call Graph Lookup**: Use the `omni-graph` skill or query `http://localhost:8080/api/symbol`
2. **Context Condensation**: Retrieve 2-hop topological call chains (<1500 tokens) instead of reading multiple raw files.
3. **Semantic Search**: Use `http://localhost:8080/api/search?q=...` for vector similarity lookup across functions, classes, and types.
4. **Enforced Rules**: Read [`.agents/rules/08-omni-graph-enforcement.md`](.agents/rules/08-omni-graph-enforcement.md).
