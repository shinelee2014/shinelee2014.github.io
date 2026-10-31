import os
import sys
import json
import ssl
import subprocess
import urllib.request
from pathlib import Path

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT_DIR / "data" / "projects.json"
BUILD_SCRIPT = ROOT_DIR / "scripts" / "build.py"
GITHUB_USER = "shinelee2014"

def fetch_repos():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    headers = {"User-Agent": "Mozilla/5.0"}
    if token:
        headers["Authorization"] = f"token {token}"
        
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    url = f"https://api.github.com/users/{GITHUB_USER}/repos?per_page=100"
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"[ERROR] Failed to fetch repositories from GitHub: {e}", file=sys.stderr)
        return []

def sync_tools(auto_push=False):
    if not DATA_FILE.exists():
        print(f"[ERROR] Data file not found: {DATA_FILE}", file=sys.stderr)
        return False
        
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        projects = json.load(f)
        
    existing_repos = {p.get("name", "").lower() for p in projects}
    
    repos = fetch_repos()
    if not repos:
        print("[WARN] No repositories fetched or API rate limit hit.")
        return False
        
    added = []
    for r in repos:
        name = r.get("name", "")
        has_pages = r.get("has_pages", False)
        
        # Skip self and repos without pages
        if name.lower() == f"{GITHUB_USER}.github.io".lower():
            continue
        if not has_pages:
            continue
            
        if name.lower() not in existing_repos:
            desc = r.get("description") or f"{name} 在线工具及开源项目"
            entry = {
                "name": name,
                "description": desc,
                "url": f"https://{GITHUB_USER}.github.io/{name}/",
                "repo": r.get("html_url", f"https://github.com/{GITHUB_USER}/{name}")
            }
            projects.append(entry)
            existing_repos.add(name.lower())
            added.append(entry)
            print(f"[+] 发现新开启 Pages 项目: {name}")
            
    if added:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(projects, f, ensure_ascii=False, indent=2)
            
        print(f"[*] 已追加 {len(added)} 个项目到 data/projects.json")
        
        # Rebuild pages
        subprocess.run([sys.executable, str(BUILD_SCRIPT)], check=True, cwd=str(ROOT_DIR))
        print("[*] 重新构建 tools.html 完成！")
        
        if auto_push:
            print("[*] 执行 Git 提交并推送...")
            try:
                subprocess.run(["git", "add", "data/projects.json", "tools.html", "index.html", "overview.html"], cwd=str(ROOT_DIR), check=True)
                msg = f"auto: 收录 {', '.join([x['name'] for x in added])} 至在线工具箱"
                subprocess.run(["git", "commit", "-m", msg], cwd=str(ROOT_DIR), check=True)
                subprocess.run(["git", "push", "origin", "main"], cwd=str(ROOT_DIR), check=True)
                print("[*] Git 推送成功！")
            except subprocess.CalledProcessError as e:
                print(f"[ERROR] Git 操作失败: {e}", file=sys.stderr)
        return True
    else:
        print("[*] 工具箱清单已是最新，无新 Pages 仓库需要收录。")
        return False

if __name__ == "__main__":
    do_push = "--push" in sys.argv
    sync_tools(auto_push=do_push)
