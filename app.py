# Team Intelligence App
def get_productivity_score(tasks_completed, tasks_total):
    return (tasks_completed / tasks_total) * 100
```
3. Scroll down → **Commit new file** → click **Commit changes**
4. Repeat — create 2 more files like `utils.py`, `models.py` with any content
   - Each file creation = **1 commit** ✅

**Create a Pull Request:**
1. Click **Add file** → **Create new file**
2. Name it `burnout_detector.py`, add any content
3. Before committing, change the branch:
   - Under **Commit new file**, select **Create a new branch**
   - Name it `feature/burnout-detection`
   - Click **Propose new file**
4. On the next screen → Click **Create pull request**
5. Add a title like `Add burnout detection module`
6. Click **Create pull request**
7. Optionally click **Merge pull request** to close it ✅

Repeat to create **2–3 more PRs** on different branches for richer data.

---

### Step 4 — Generate Personal Access Token

1. Click your **profile picture** → **Settings**
2. Scroll left sidebar to the bottom → **Developer settings**
3. Click **Personal access tokens** → **Tokens (classic)**
4. Click **Generate new token** → **Generate new token (classic)**
5. Fill in:
   - **Note** → `team-intelligence-pipeline`
   - **Expiration** → 90 days
   - **Scopes** → check ✅ `repo`
6. Click **Generate token**
7. **Copy it immediately** — looks like `ghp_abc123xyz...`

---

### Step 5 — Fill in `.env`
```
GITHUB_TOKEN=ghp_your_token_here
GITHUB_OWNER=your-github-username
GITHUB_REPO=team-intelligence
