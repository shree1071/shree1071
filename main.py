import gifos
import os

t = gifos.Terminal(width=800, height=500, xpad=5, ypad=5)
t.gen_text(text="shree1071@bmsit:~$ whoami", row_num=1)
t.gen_text(text="Shreeharsha - CS Undergraduate @ BMSIT", row_num=2)
t.gen_text(text="LLM Orchestration | Multi-Agent Systems | Decentralised Web3", row_num=3)
t.gen_text(text="", row_num=4)

t.gen_text(text="shree1071@bmsit:~$ cat ~/skills.json", row_num=5)
t.gen_text(text='{ "Languages": ["C/C++", "Python", "TypeScript", "JavaScript", "SQL", "Solidity"],', row_num=6)
t.gen_text(text='  "AI_ML": ["MedGemma", "LLM Orchestration", "LangGraph", "Agentic AI", "RAG", "Groq"],', row_num=7)
t.gen_text(text='  "Web3": ["Solidity", "Hardhat", "Ethers.js", "WalletConnect", "EVM Smart Contracts"] }', row_num=8)
t.gen_text(text="", row_num=9)

t.gen_text(text="shree1071@bmsit:~$ ./fetch_achievements.sh", row_num=10)
t.gen_text(text="[+] 6x Hackathon Winner (across AI, Web3, Healthcare)", row_num=11)
t.gen_text(text="[+] 2nd Place - Spectre Hackathon (National Level)", row_num=12)
t.gen_text(text="[+] 2x 1st Place - InCSEption Hackathon (Department Level)", row_num=13)
t.gen_text(text="[+] IEEE Research Intern (Blockchain-based medical records)", row_num=14)
t.gen_text(text="[+] Technical Lead - Generative AI Club, BMSIT", row_num=15)
t.gen_text(text="", row_num=16)

try:
    github_stats = gifos.utils.fetch_github_stats(user_name="shree1071")
    t.gen_text(text=f"shree1071@bmsit:~$ echo $GITHUB_STATS", row_num=17)
    t.gen_text(text=f"Total Commits (last year): {github_stats.total_commits}", row_num=18)
    t.gen_text(text=f"Total PRs: {github_stats.total_prs}", row_num=19)
    t.gen_text(text=f"Total Stars: {github_stats.total_stars}", row_num=20)
except Exception:
    pass

t.gen_gif()
