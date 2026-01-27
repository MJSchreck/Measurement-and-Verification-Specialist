# Step-by-Step Setup Guide

## What I Built For You

I created 3 files in your GitHub repo. Each one goes into a specific place in Claude.ai. Follow the steps below.

---

## STEP 1 — Open Your Files on GitHub

1. Open your browser
2. Go to: `https://github.com/MJSchreck/Measurement-and-Verification-Specialist`
3. You'll see these new files:
   - `claude-project-instructions.md`
   - `claude-project-knowledge.md`
   - `claude-memory-and-skills.md`
4. Click each file to view it — you'll copy from these

---

## STEP 2 — Create a Project in Claude.ai

1. Go to `https://claude.ai`
2. Log in to your account
3. On the left sidebar, click **"Projects"** (folder icon)
4. Click **"Create Project"**
5. Name it: **"GSA M&V Specialist"**
6. Click **Create**

---

## STEP 3 — Add Project Instructions

1. Inside your new project, click the **gear icon** (Settings) or **"Set custom instructions"**
2. Open `claude-project-instructions.md` from GitHub
3. Copy everything **below the line** (below the `---`)
4. Paste it into the **"Custom Instructions"** box
5. Click **Save**

---

## STEP 4 — Add Project Knowledge

1. In your project, find **"Project Knowledge"** section
2. Click **"Add content"** → **"Add text"**
3. Open `claude-project-knowledge.md` from GitHub
4. Copy everything **below the line** (below the `---`)
5. Paste it in
6. Click **Save**

**Bonus:** You can also upload files here. Upload any of these from your Notion/computer:
- Utility bill spreadsheets
- Past M&V reports (PDF)
- ECM lists
- Building info sheets
- Contractor proposals

---

## STEP 5 — Set Up Your Memory

1. Go to Claude.ai **Settings** (click your name → Settings)
2. Find **"Memory"** or **"Personalization"**
3. Open `claude-memory-and-skills.md` from GitHub
4. Copy the text inside the Memory code block
5. Tell Claude in a regular chat: "Remember this about me:" and paste the memory text
6. Claude will store it and use it in future conversations

---

## STEP 6 — Connect Your Notion Data (Optional but Powerful)

1. In your Claude.ai project, click **"Add content"** → **"Connect"**
2. If Notion integration is available, connect it
3. **Alternative (works today):** Export key Notion pages as PDF or Markdown, then upload them to your Project Knowledge

### What to export from Notion:
- Project tracking databases
- Building lists with addresses and SF
- ECM summaries
- Utility account info
- Any M&V templates you've built

---

## STEP 7 — Start Using It

Open your GSA M&V Specialist project in Claude.ai and try these prompts:

### Quick test:
> "Draft an M&V plan outline for an LED lighting retrofit in a 50,000 SF GSA office building in Washington DC using IPMVP Option A."

### Data analysis:
> Upload a utility bill spreadsheet, then say: "Analyze this utility data. Build a weather-normalized baseline model. Report R², CV(RMSE), and NMBE."

### Report writing:
> "Write an executive summary for an annual M&V report showing 15% energy savings across 3 ECMs in an ESPC project."

---

## How to Keep This Updated

Whenever you get new project data, templates, or standards:
1. Upload files to your Claude.ai Project Knowledge
2. For code/scripts, push them to this GitHub repo
3. Claude will use everything in the project context automatically

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Claude doesn't follow the M&V format | Re-paste the project instructions — they may not have saved |
| Claude doesn't know my buildings | Upload your building list to Project Knowledge |
| Can't find Projects in Claude.ai | You need Claude Pro ($20/mo) for Projects |
| GitHub looks confusing | Just use the green "Code" button → "Download ZIP" to get all files |
