import re
import sys
from pathlib import Path

def validate_main_ts(file_path):
    if not Path(file_path).exists():
        return False, f"Error: File {file_path} not found."
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    errors = []
    
    # Extract all node declarations: f.node('id', 'Namespace' ...) or .then('id', 'Namespace' ...)
    node_pattern = re.compile(r"(?:f\.node|\.then)\s*\(\s*['\"]([^'\"]+)['\"]\s*,\s*['\"]([^'\"]+)['\"]")
    nodes = node_pattern.findall(content)
    
    node_map = {}
    for node_id, namespace in nodes:
        node_map[node_id] = namespace
        # 1. Hex-6 Check
        if not re.match(r"^[0-9a-f]{6}$", node_id):
            errors.append(f"[SDK Validation] Invalid node ID '{node_id}' for namespace '{namespace}'. Must be exactly 6 lowercase hex chars (e.g., '1a2b3c').")
            
    # 2. Label Check (.then)
    then_pattern = re.compile(r"\.then\s*\(\s*['\"]([^'\"]+)['\"]\s*,\s*['\"]([^'\"]+)['\"]")
    thens = then_pattern.findall(content)
    for node_id, namespace in thens:
        if namespace == "Core.Flow.Label":
            errors.append(f"[SDK Validation] Cannot chain to node '{node_id}' (Core.Flow.Label) using .then(). Labels have 0 inputs. Declare separately with f.node() and enter via GoTo.")
            
    # 3. Edge to Label check
    edge_pattern = re.compile(r"f\.edge\s*\(\s*['\"]([^'\"]+)['\"]\s*,\s*\d+\s*,\s*['\"]([^'\"]+)['\"]")
    edges = edge_pattern.findall(content)
    for source, target in edges:
        if node_map.get(target) == "Core.Flow.Label":
             errors.append(f"[SDK Validation] Cannot wire f.edge() to node '{target}' (Core.Flow.Label). Use GoTo.")

    if errors:
        return False, "\n".join(errors)
    return True, "Validation successful."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        success, msg = validate_main_ts(sys.argv[1])
        print(msg)
        sys.exit(0 if success else 1)
