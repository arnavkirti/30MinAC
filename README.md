## 30MinAC - A CLI tool for DSA

> Sharpen your problem-solving skills — one problem at a time, under pressure.

**30MinAC** (30 Minute Accepted) is a Python-based CLI tool that turns LeetCode problem-solving into a timed challenge. It's perfect for developers preparing for coding interviews or simply wanting to stay sharp with a bit of adrenaline.

---

## 🚀 Features

* ⏱️ **Countdown Timer**: Start a timer to solve a LeetCode problem under time constraints.
* 🧠 **Smart Hint System**: Automatically fetch hints if you're stuck after the timer ends.
* ✅ **Submission Tracker**: Monitors your recent submissions via the LeetCode API.
* 🏆 **Gamified Scoring**: +10 points if you solve it in time, +5 points on a hint-based recovery.

---

## 🛠️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/arnavkirti/30MinAC.git
cd 30MinAC
```

### 2. Install dependencies

Make sure you have Python installed (`>=3.6` recommended). Then install:

```bash
pip install requests python-dotenv
```

### 3. Set up your `.env` file

```bash
cp .env.example .env
```

```env
API_URL=https://leetcode-api-url-goes-here.com/
USERNAME=your-leetcode-username
```

> 📝 Note: This tool assumes you're using a backend API that can access your LeetCode submissions and problem hints. You can use any free API that is present on the internet or just DM me.  

---

## 🧑‍💻 Usage

```bash
python main.py
```

Follow the prompts:

1. Paste a LeetCode problem URL (e.g., `https://leetcode.com/problems/two-sum`)
2. Solve the problem within the given time.
3. Let the script track your submission status.
4. If not accepted, get a hint and retry with extra time.

---

## 🏁 Game Rules

* 🕒 **Phase 1**: Solve within the first timer (default: 3 minutes here for testing — extend to 30 mins for real use).

  * ✅ Accepted: +10 points
* 🧠 **Phase 2**: Get a hint and 10 more minutes.

  * ✅ Accepted: +5 points
* ❌ Still stuck? No worries. Learn from the official solution and come back stronger!

---

## 🧪 Customization Ideas

* Make the initial countdown 30 minutes for full challenge mode.
* Add a leaderboard or local scoreboard.
* Integrate with Telegram/Slack bots for real-time challenge updates.
* Add daily challenge notifications.

---

## 📚 Technologies Used

* Python
* `requests` for API calls
* `dotenv` for environment variable management

---

## 🤝 Contributing

Want to improve this tool? Fork it, make changes, and submit a pull request!

---

## 💡 Inspiration

Practicing LeetCode is powerful — but time-boxed practice simulates real interview conditions. **30MinAC** is built for developers who love a challenge and want to grow fast.

---

Let me know if you want a badge section, GitHub Actions, or Docker support too!
