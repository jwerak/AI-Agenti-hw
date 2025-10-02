# AI Agenti - HW 3

## Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package manager

## Installation

```bash
# Install dependencies using uv
uv sync

# Run the application
uv run python main.py
```

## Zadání

Navrhni a vytvoř agenta pomocí frameworku, který pracuje s nástroji (Tooly), a
odpovídá na dotazy přes LLM. Framework zvolte jeden dle listu níže, nástroje (tooly)
vyberte libolně, seznam níže slouží jen jako příklad. Zvažte použití MCP namísto
„framework-specific“ toolů.

Agent:
 ReAct
 Plan-Execute
 Vlastní workflow

Frameworky:
 Vlastní
 Langchain
 Langgraph
 Semantic Kernel
 Autogen

Nástroje:
 Databáze (SQL, NoSQL, Full-text, Vector, File)
 Vyhledáče (tavily, serapi)
 Wikipedia
 Gmail
 Wolfram Alpha

### Forma odevzdání

Vypracovaný úkol odevzdejte ve formě zdrojového kódu. Projekt ideálně nahrajte na
Github a odevzdejte link do Github repositáře. Link odevzdejte v Google Classroom.

## Flow agenta

Pouzit MCP server - https://github.com/langchain-ai/langchain-mcp-adapters

##
