# 🚀 Local LLM to Robomotion Bridge - How to Use

**What is this tool?**
The *Local LLM to Robomotion Bridge* is a 1-click open-source tool designed to seamlessly connect your local, free AI (like LM Studio, Ollama, or Anti Gravity) with the Robomotion RPA platform. It allows you to build powerful, autonomous automation robots (RPA) directly on your local machine without paying for expensive AI API tokens, and syncs the generated code directly to your Robomotion cloud workspace.

Welcome to the Local LLM to Robomotion Bridge! Follow the steps below to setup your factory.

## 📖 Step-by-Step Tutorial

### Step 1: Generate your GitHub PAT (Personal Access Token)
Before running the setup, you must generate a GitHub Token:
1. Go to your GitHub account **Settings** > **Developer Settings** > **Personal access tokens** > **Tokens (classic)**.
2. Click **Generate new token (classic)** (Do NOT select "Fine-grained token").
3. Give it a name and **check the `repo` checkbox** (this grants full control of private repositories).
4. Click Generate and copy the token (`ghp_...`).

### Step 2: Run the Setup
Launch `LLB_gui.py` (or use `LLB_cli.py` in the terminal). Fill out the fields:
- **Project Name**: The folder name that will be created on your Desktop. It will also be the name of your auto-created GitHub repository!
- **GitHub Username**: Your GitHub handle.
- **PAT Token**: The GitHub Personal Access Token you just created.

Click the "🔥 Auto-Create Repo & Generate Workspace" button. The software will use the GitHub API to magically create the private repository for you, create the local folder, copy the Robomotion documentation, create the rules for your AI (`agent_rules.md`), and securely sync everything to your GitHub.

### Step 3: Boot your Local AI
Open your local AI agent (like **LM Studio**, **Anti Gravity**, **Cursor**, etc.) and load the newly created project folder on your Desktop.

Give it the following instruction:
> *"Read the `agent_rules.md` file and build the automation flow."*

### Step 4: Let the AI Auto-Sync
The AI will generate the TypeScript code (`main.ts`).
As soon as the code is saved, our background Auto-Push logic automatically synchronizes and pushes the files straight to your GitHub repository! You don't have to type any git commands.

### Step 5: Import into Robomotion Designer
Finally, import the AI's work into the Robomotion Cloud interface:
1. Go to Robomotion Designer.
2. Click **'Import Flow'** -> **'From Git'**.

⚠️ **CRITICAL - Fill the popup EXACTLY like this:**
- **Git URL**: Your GitHub Repository link (`https://github.com/User/Repo.git`)
- **Branch**: `main` *(DO NOT put your email address here!)*
- **Authentication Token**: Your GitHub PAT (the same key used in step 1).
- **Auth Username**: (Leave Empty or Optional)
- **Flow Name**: Your project name.

Click **Import** and your flow will instantly appear!

---

### Links
- 📺 [YouTube Channel](https://www.youtube.com/@xoxoPwn)
- 🐙 [GitHub Profile](https://github.com/Thexoxo)
