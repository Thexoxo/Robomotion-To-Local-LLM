# ==============================================================================
# Local LLM to Robomotion Bridge
# Copyright (C) 2026 Thexoxo (https://github.com/Thexoxo)
# YouTube: https://www.youtube.com/@xoxoPwn
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.
# ==============================================================================

import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import shutil
from pathlib import Path
import webbrowser

# --- PROMPT AGENT ---
AGENT_PROMPT = """# SYSTEM INSTRUCTIONS: EXPERT DEVELOPER ROBOMOTION RPA

[CONTEXT AND ROLE]
You are an elite development agent for Robomotion RPA. Your mission is to design from scratch, modify, and deploy a 100% autonomous automation flow in this local workspace. You will generate the required 'main.ts' and 'main.designer.ts' files, then push them to the remote Git repository so they appear on the online Designer.

[STEP 1: SIMULTANEOUS LEARNING (MANDATORY)]
Before writing any code, you must deeply analyze the official SDK documentation, grammar, and design patterns stored locally on this machine at the following exact path:
"./skills-fallback/skills/creating-flow/docs/"

[STEP 2: IRON LAWS OF SYNTAX (STRICT COMPLIANCE REQUIRED)]
For the code to be valid and accepted by Robomotion, you must apply these 5 laws:
1. COMPLETE LINE 1: The 'main.ts' file must strictly start with the following exact import:
import { flow, Message, Custom, JS, Global, Flow, Credential, AI } from '@robomotion/sdk';

2. HEX-6 NODE IDs: All node identifiers (node IDs) in the flow must be 6-character lowercase hexadecimal strings (e.g., '42ec21', '7dbafc'). It is strictly FORBIDDEN to use plain text (like 'begin', 'loop', 'label').

3. PROPERTY ENCAPSULATION: Never pass raw primitive values to node options. Always use the Custom('value') or Message('variable') helpers (Example: optTimeout: Custom('30')).

4. LOOP PATTERNS: Strictly apply the structure: Label (Hex-6 ID) -> ForEach -> [Code Body] -> GoTo (the GoTo must explicitly jump to the Hex-6 ID of the Label node).

5. DATA TABLE FORMAT: For any data manipulation (CSV, Excel), the msg.table property must strictly follow this JSON object structure: { columns: [...], rows: [...] }.

[STEP 3: DEPLOYMENT AND AUTO-PUSH PROCESS]
Once you have written the 'main.ts' and 'main.designer.ts' files without errors, you are authorized to open the system terminal to autonomously execute the following sequence of Git commands to publish the flow to the Cloud:
1. git add .
2. git commit -m "Automated workflow generation and sync by AI Agent"
3. git push origin main

[YOUR MISSION]
Design the complete 'main.ts' and 'main.designer.ts' files, validate them, then execute the Auto-Push process for the following action:
--> [WRITE YOUR SPECIFIC GOAL HERE, EX: A robot that logs into a site, scrapes a data table, and saves it as CSV] <--
"""

def setup_workspace():
    username = entry_user.get().strip()
    pat = entry_pat.get().strip()
    repo = entry_repo.get().strip()
    project_name = entry_proj.get().strip()
    
    if not username or not pat or not repo or not project_name:
        messagebox.showerror("Error", "All fields are required.")
        return
        
    # Paths definition
    desktop = Path(os.path.expanduser("~")) / "Desktop"
    workspace = desktop / project_name
    
    # 🌟 MODIFICATION : Fetch skills-fallback from the script's own folder for portability
    script_dir = Path(__file__).parent
    source_docs = script_dir / 'skills-fallback'
    
    try:
        workspace.mkdir(parents=True, exist_ok=True)
        
        dest_skills = workspace / "skills-fallback"
        if source_docs.exists() and not dest_skills.exists():
            shutil.copytree(source_docs, dest_skills)
        elif not source_docs.exists():
            messagebox.showwarning("Warning", "The 'skills-fallback' folder was not found next to the installer. The AI will lack documentation.")
            
        with open(workspace / "agent_rules.md", "w", encoding="utf-8") as f:
            f.write(AGENT_PROMPT)
            
        with open(workspace / "main.ts", "w", encoding="utf-8") as f:
            f.write("import { flow, Message, Custom, JS, Global, Flow, Credential, AI } from '@robomotion/sdk';\n\nconst myFlow = flow.create('main', 'New Flow', (f) => {});\nmyFlow.start();")
        with open(workspace / "main.designer.ts", "w", encoding="utf-8") as f:
            f.write("import { flow, Message, Custom, JS, Global, Flow, Credential, AI } from '@robomotion/sdk';\n\nconst myFlow = flow.create('main', 'New Flow', (f) => {});\nmyFlow.start();")
            
        with open(workspace / ".env", "w", encoding="utf-8") as f:
            f.write(f"GITHUB_USERNAME={username}\nGITHUB_PAT={pat}\nGITHUB_REPO={repo}\n")
            
        if repo.startswith("https://"):
            repo_clean = repo.replace("https://", "")
        else:
            repo_clean = repo
        auth_url = f"https://{username}:{pat}@{repo_clean}"
        
        cflags = subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
        if not (workspace / '.git').exists():
            subprocess.run(['git', 'init'], cwd=workspace, check=True, creationflags=cflags)
            
        subprocess.run(['git', 'add', '.'], cwd=workspace, check=True, creationflags=cflags)
        subprocess.run(['git', 'commit', '-m', 'Workspace initialization'], cwd=workspace, capture_output=True, creationflags=cflags)
        subprocess.run(['git', 'remote', 'remove', 'origin'], cwd=workspace, capture_output=True, creationflags=cflags)
        subprocess.run(['git', 'remote', 'add', 'origin', auth_url], cwd=workspace, check=True, creationflags=cflags)
        subprocess.run(['git', 'branch', '-M', 'main'], cwd=workspace, check=True, creationflags=cflags)
        subprocess.run(['git', 'push', '-u', 'origin', 'main'], cwd=workspace, check=True, creationflags=cflags)
        
        msg = (f"✅ Workspace '{project_name}' successfully created!\n"
               "Please read the README.md file to know how to pilot your AI.")
        messagebox.showinfo("Success", msg)
        root.destroy()
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

def open_youtube():
    webbrowser.open("https://www.youtube.com/@xoxoPwn")

def open_github():
    webbrowser.open("https://github.com/Thexoxo")

# --- UI ---
root = tk.Tk()
root.title("Local LLM to Robomotion Bridge")
root.geometry("500x320")
root.configure(padx=20, pady=20)
root.resizable(False, False)

tk.Label(root, text="Local LLM to Robomotion Bridge", font=("Helvetica", 14, "bold")).pack(pady=(0, 10))

frame = tk.Frame(root)
frame.pack(fill="x")

tk.Label(frame, text="Project Name (Folder):").grid(row=0, column=0, sticky="w", pady=5)
entry_proj = tk.Entry(frame, width=35)
entry_proj.grid(row=0, column=1, pady=5, padx=5)
entry_proj.insert(0, "my_rpa_workspace")

tk.Label(frame, text="GitHub Username:").grid(row=1, column=0, sticky="w", pady=5)
entry_user = tk.Entry(frame, width=35)
entry_user.grid(row=1, column=1, pady=5, padx=5)

tk.Label(frame, text="PAT Token (Key):").grid(row=2, column=0, sticky="w", pady=5)
entry_pat = tk.Entry(frame, width=35, show="*")
entry_pat.grid(row=2, column=1, pady=5, padx=5)

tk.Label(frame, text="GitHub Repo URL:").grid(row=3, column=0, sticky="w", pady=5)
entry_repo = tk.Entry(frame, width=35)
entry_repo.grid(row=3, column=1, pady=5, padx=5)

tk.Button(root, text="🔥 Generate Workspace & Push", bg="#2c3e50", fg="white", font=("Helvetica", 11, "bold"), command=setup_workspace).pack(pady=15)

links_frame = tk.Frame(root)
links_frame.pack(side="bottom")

tk.Button(links_frame, text="▶️ YouTube", command=open_youtube, cursor="hand2", bg="#ff0000", fg="white", font=("Helvetica", 9, "bold")).pack(side="left", padx=10)
tk.Button(links_frame, text="🐙 GitHub", command=open_github, cursor="hand2", bg="#333333", fg="white", font=("Helvetica", 9, "bold")).pack(side="left", padx=10)

root.mainloop()
