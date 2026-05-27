# 🚀 Local LLM to Robomotion Bridge (MCP Edition)

**What is this tool?**
The *Local LLM to Robomotion Bridge* is a 1-click open-source tool designed to seamlessly connect your local, free AI (like LM Studio, Ollama, or Anti Gravity) with the Robomotion RPA platform. 
Instead of relying on unstable prompts, this bridge uses a **Model Context Protocol (MCP) Server** as its core engine. The MCP Server acts as an infallible "brain extension" for your AI, allowing it to dynamically read Robomotion's official documentation, grammar, and node packages *before* generating any code. This guarantees a **Zero-Hallucination** environment.

## 🧠 Step 1: The Core Engine (MCP Server) - MANDATORY

The entire intelligence of this bridge relies on `mcp_robomotion.py`. You **MUST** configure this server in your AI Agent's IDE (Cursor, Claude Desktop, Anti-Gravity, etc.).

1. Locate the `mcp_config.example.json` file in this repository.
2. Create or update your AI's MCP configuration file (for example, `mcp_config.json` in your AI's configuration folder).
3. Add the `robomotion_expert` server pointing to the absolute path of `mcp_robomotion.py` using Python.

Example configuration:
```json
{
  "mcpServers": {
    "robomotion_expert": {
      "command": "python",
      "args": [
        "C:\\Absolute\\Path\\To\\Local-LLM-to-Robomotion-Bridge\\mcp_robomotion.py"
      ]
    }
  }
}
```
*Once this is loaded, your AI will have access to 4 powerful tools: `list_robomotion_documentation`, `read_robomotion_documentation`, `search_node_package`, and `get_cli_instructions`.*

## 📖 Step 2: Generate your GitHub PAT (Personal Access Token)
To allow your AI to automatically push flows to the Cloud:
1. Go to your GitHub account **Settings** > **Developer Settings** > **Personal access tokens** > **Tokens (classic)**.
2. Click **Generate new token (classic)** (Do NOT select "Fine-grained token").
3. Give it a name and **check the `repo` checkbox**.
4. Click Generate and copy the token (`ghp_...`).

## ⚙️ Step 3: Configure the Environment
To avoid passing your token in the command line history, create a `.env` file in the same folder as `LLB_cli.py` containing:
```env
GITHUB_USERNAME=YourUsername
GITHUB_PAT=ghp_xxxx...
```

## 🤖 Step 4: AI Workflow (Zero-Touch Automation)
With the MCP server running and your credentials saved, your AI Agent only needs a tiny instruction:

> *"Tu es un expert Robomotion RPA connecté à un Serveur MCP Robomotion. Utilise tes outils MCP pour lire la documentation, et crée le projet 'my_new_bot' via LLB_cli.py."*

The AI will automatically:
1. Run `python LLB_cli.py --project "my_new_bot"` to generate the Git Monorepo workspace.
2. Enter the new workspace.
3. Consult the Robomotion SDK documentation via its MCP tools.
4. Generate the `main.ts` and `main.designer.ts` files perfectly.
5. Auto-Push the files to GitHub (`git add .`, `git commit`, `git push`).

## 📥 Step 5: Import into Robomotion Designer
Finally, import the AI's work into the Robomotion Cloud interface:
1. Go to Robomotion Designer.
2. Click **'Import Flow'** -> **'From Git'**.

⚠️ **CRITICAL - Fill the popup EXACTLY like this:**
- **Git URL**: Your GitHub Repository link (`https://github.com/User/Repo.git`)
- **Branch**: `main`
- **Authentication Token**: Your GitHub PAT.
- **Auth Username**: (Leave Empty)
- **Flow Name**: Your project name.

Click **Import** and your autonomous robot is ready!

---

### Links
- 📺 [YouTube Channel](https://www.youtube.com/@xoxoPwn)
- 🐙 [GitHub Profile](https://github.com/Thexoxo)
