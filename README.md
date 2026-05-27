# 🚀 RPA Workspace Generator - How to Use

Welcome to the RPA Workspace Generator! This tool connects your Local LLM AI with Robomotion and GitHub.

## 📖 Step-by-Step Tutorial

### Step 1: Run the Setup
Launch the `gui_installer.py` (or the `.exe` if provided). Fill out the fields:
- **Project Name**: The folder name that will be created on your Desktop.
- **GitHub Username**: Your GitHub handle.
- **PAT Token**: Your GitHub Personal Access Token (with 'repo' scopes).
- **GitHub Repo URL**: Link to your repository (e.g. `https://github.com/User/Repo.git`).

Click the "🔥 Generate Workspace" button. The software will create the folder, copy the Robomotion documentation, create the rules for your AI (`agent_rules.md`), and securely sync everything to your GitHub.

### Step 2: Boot your Local AI
Open your local AI agent (like **LM Studio**, **Anti Gravity**, **Cursor**, etc.) and load the newly created project folder on your Desktop.

Give it the following instruction:
> *"Read the `agent_rules.md` file and build the automation flow."*

### Step 3: Let the AI Auto-Sync
The AI will generate the TypeScript code (`main.ts`).
As soon as the code is saved, our background Auto-Push logic automatically synchronizes and pushes the files straight to your GitHub repository! You don't have to type any git commands.

### Step 4: Import into Robomotion Designer
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
