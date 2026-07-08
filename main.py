import gifos
import os

t = gifos.Terminal(width=800, height=500, xpad=5, ypad=5)
t.toggle_show_cursor(False)

# Command 1: whoami
t.gen_prompt(row_num=1)
prompt_col = t.curr_col
t.toggle_show_cursor(True)
t.gen_typing_text("\x1b[92mwhoami\x1b[0m", row_num=1, contin=True)
t.toggle_show_cursor(False)
t.gen_text(text="\x1b[93mShreeharsha - CS Undergraduate @ BMSIT\x1b[0m", row_num=2, count=30)
t.gen_text(text="\x1b[96mLLM Orchestration | Multi-Agent Systems | Decentralised Web3\x1b[0m", row_num=3, count=45)
t.gen_text(text="", row_num=4)

# Command 2: cat ~/skills.json
t.gen_prompt(row_num=5)
prompt_col = t.curr_col
t.toggle_show_cursor(True)
t.gen_typing_text("\x1b[92mcat ~/skills.json\x1b[0m", row_num=5, contin=True)
t.toggle_show_cursor(False)
t.gen_text(text='\x1b[94m{\x1b[0m', row_num=6, count=5)
t.gen_text(text='  \x1b[93m"Languages"\x1b[0m: [\x1b[92m"C/C++", "Python", "TypeScript", "JavaScript", "SQL", "Solidity"\x1b[0m],', row_num=7, count=10)
t.gen_text(text='  \x1b[93m"AI_ML"\x1b[0m:     [\x1b[92m"MedGemma", "LLM Orchestration", "LangGraph", "Agentic AI", "RAG", "Groq"\x1b[0m],', row_num=8, count=10)
t.gen_text(text='  \x1b[93m"Web3"\x1b[0m:      [\x1b[92m"Solidity", "Hardhat", "Ethers.js", "WalletConnect", "EVM"\x1b[0m]', row_num=9, count=10)
t.gen_text(text='\x1b[94m}\x1b[0m', row_num=10, count=45)
t.gen_text(text="", row_num=11)

# Command 3: ./fetch_achievements.sh
t.gen_prompt(row_num=12)
prompt_col = t.curr_col
t.toggle_show_cursor(True)
t.gen_typing_text("\x1b[92m./fetch_achievements.sh\x1b[0m", row_num=12, contin=True)
t.toggle_show_cursor(False)
t.gen_text(text="[+] \x1b[93m6x Hackathon Winner\x1b[0m (across AI, Web3, Healthcare)", row_num=13, count=10)
t.gen_text(text="[+] \x1b[93m2nd Place\x1b[0m - Spectre Hackathon (National Level)", row_num=14, count=10)
t.gen_text(text="[+] \x1b[93m2x 1st Place\x1b[0m - InCSEption Hackathon (Department Level)", row_num=15, count=10)
t.gen_text(text="[+] \x1b[96mIEEE Research Intern\x1b[0m (Blockchain-based medical records)", row_num=16, count=10)
t.gen_text(text="[+] \x1b[96mTechnical Lead\x1b[0m - Generative AI Club, BMSIT", row_num=17, count=45)
t.gen_text(text="", row_num=18)

# Command 4: echo $GITHUB_STATS
try:
    github_stats = gifos.utils.fetch_github_stats(user_name="shree1071")
    t.gen_prompt(row_num=19)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[92mecho $GITHUB_STATS\x1b[0m", row_num=19, contin=True)
    t.toggle_show_cursor(False)
    t.gen_text(text=f"\x1b[94mTotal Commits (last year):\x1b[0m \x1b[93m{github_stats.total_commits}\x1b[0m", row_num=20, count=10)
    t.gen_text(text=f"\x1b[94mTotal PRs:\x1b[0m \x1b[93m{github_stats.total_prs}\x1b[0m", row_num=21, count=10)
    t.gen_text(text=f"\x1b[94mTotal Stars:\x1b[0m \x1b[93m{github_stats.total_stars}\x1b[0m", row_num=22, count=45)
    t.gen_text(text="", row_num=23)
except Exception:
    pass

t.gen_prompt(row_num=t.curr_row + 1)
t.toggle_show_cursor(True)
t.gen_typing_text("\x1b[92m# Have a nice day! Thanks for stopping by :)\x1b[0m", row_num=t.curr_row, contin=True)

t.gen_text("", t.curr_row, count=100, contin=True)

t.gen_gif()
