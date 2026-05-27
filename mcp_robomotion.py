from mcp.server.fastmcp import FastMCP
import os
from pathlib import Path

# Initialisation du serveur MCP pour Robomotion
mcp = FastMCP("Robomotion_Expert_SDK")

SKILLS_PATH = Path(__file__).parent / "skills-fallback"

@mcp.tool()
def list_robomotion_documentation() -> str:
    """
    Retourne la liste de TOUS les fichiers de documentation officiels disponibles pour Robomotion
    (browser, data-tables, loops, exceptions, etc.).
    A appeler pour découvrir quels manuels sont disponibles.
    """
    results = []
    for root_dir, _, files in os.walk(SKILLS_PATH):
        for file in files:
            if file.endswith(".md"):
                # Calcul du chemin relatif pour l'affichage
                rel_path = os.path.relpath(os.path.join(root_dir, file), SKILLS_PATH)
                results.append(f"- {file} (Chemin: {rel_path})")
    
    if not results:
        return "Aucune documentation trouvée."
    
    header = "📚 MANUELS ROBOMOTION DISPONIBLES:\nUtilisez 'read_robomotion_documentation(filename)' pour lire l'un de ces fichiers.\n\n"
    return header + "\n".join(sorted(results))

@mcp.tool()
def read_robomotion_documentation(filename: str) -> str:
    """
    Lit l'intégralité d'un fichier de documentation spécifique (ex: 'browser.md', 'loops.md', 'sdk-grammar.md').
    """
    for root_dir, _, files in os.walk(SKILLS_PATH):
        for file in files:
            if file.lower() == filename.lower():
                file_path = os.path.join(root_dir, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        return f"--- CONTENU DE {file} ---\n\n" + f.read()
                except Exception as e:
                    return f"Erreur lors de la lecture de {file}: {str(e)}"
    
    return f"Erreur: Le fichier '{filename}' est introuvable. Utilisez list_robomotion_documentation() pour voir la liste exacte."

@mcp.tool()
def search_node_package(query: str) -> str:
    """
    Recherche un noeud spécifique (ex: 'Http', 'File') dans la documentation locale
    pour obtenir son namespace exact (ex: 'Core.Net.HttpRequest').
    """
    results = []
    for root_dir, _, files in os.walk(SKILLS_PATH):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root_dir, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        if query.lower() in content.lower():
                            idx = content.lower().find(query.lower())
                            start = max(0, idx - 100)
                            end = min(len(content), idx + 200)
                            results.append(f"--- Extrait de {file} ---\n{content[start:end]}\n")
                except:
                    pass
    
    if not results:
        return f"Aucune information trouvée pour le noeud: {query}"
    return "\n".join(results[:5])

@mcp.tool()
def get_cli_instructions() -> str:
    """
    Retourne le manuel complet des commandes CLI Robomotion (robomotion search, get, describe, docs)
    pour trouver des packages, noeuds et templates directement via le terminal.
    """
    cli_path = SKILLS_PATH / "skills" / "searching-packages" / "SKILL.md"
    if not cli_path.exists():
        return "Erreur: Fichier SKILL.md de la CLI introuvable."
    with open(cli_path, "r", encoding="utf-8") as f:
        return f.read()

@mcp.tool()
def create_robomotion_project(project_name: str) -> str:
    """
    Crée un NOUVEAU projet Robomotion (ou synchronise un existant) via LLB_cli.py.
    Prépare l'espace de travail local et le dépôt GitHub automatiquement.
    """
    import subprocess
    bridge_dir = SKILLS_PATH.parent
    try:
        # Exécute LLB_cli.py qui s'occupe de lire le .env et de créer/pusher le projet
        result = subprocess.run(
            ['python', 'LLB_cli.py', '--project', project_name],
            cwd=str(bridge_dir),
            capture_output=True,
            text=True,
            check=True
        )
        return f"Succès ! Projet '{project_name}' préparé.\nLogs:\n{result.stdout}"
    except subprocess.CalledProcessError as e:
        return f"Erreur lors de la création du projet.\nLogs d'erreur:\n{e.output}\n{e.stderr}"
    except Exception as e:
        return f"Erreur fatale: {str(e)}"

if __name__ == "__main__":
    print("Démarrage du Serveur MCP Robomotion Expert...")
    mcp.run()
