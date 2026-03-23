# 🎂 Happy Birthday Monika — Interactive Surprise Website

A magical, fully interactive birthday surprise experience built with **Streamlit + HTML/CSS/JS**.  
Three cinematic scenes unfold as she clicks through — ending in fireworks, floating hearts, and personalised love messages.

---

## ✨ Experience Overview

| Scene | What Happens |
|-------|-------------|
| 🚪 **Door** | A glowing arched door with a golden padlock floats in a starfield. She clicks it → the lock shakes open, hearts burst out, sparkles fly. |
| 💌 **Envelope** | A blush-pink envelope with a wax seal appears. She clicks it → the flap peels back, a love letter rises out. |
| 🎂 **Celebration** | Full birthday scene with animated title, fireworks, rose petals, floating hearts, 3 love message pills, and a cake to tap. |

---

## 🚀 Quick Start

### 1. Clone or Download
```bash
git clone https://github.com/yourusername/monika-birthday.git
cd monika-birthday
```

### 2. Install Dependencies
```bash
pip install streamlit
```
> No other packages needed — everything runs on Streamlit's built-in `components.html`.

### 3. Run Locally
```bash
streamlit run monika_birthday.py
```
Opens at → `http://localhost:8501`

---

## 🌐 Deploy Online (Send Her a Link!)

### Option A — Streamlit Community Cloud (Free & Easiest)

1. Push your code to a **GitHub repository**
2. Go to **[share.streamlit.io](https://share.streamlit.io)**
3. Click **"New app"** → connect your GitHub repo
4. Set **Main file path** to `monika_birthday.py`
5. Click **Deploy** 🚀
6. You'll get a shareable link like:
   ```
   https://your-app-name.streamlit.app
   ```
7. Send it to Monika 💗

### Option B — Run on Any Server
```bash
streamlit run monika_birthday.py --server.port 8080 --server.address 0.0.0.0
```

---

## 📁 Project Structure

```
monika-birthday/
│
├── monika_birthday.py      # Main Streamlit app (all-in-one)
└── README.md               # This file
```

> The entire experience — HTML, CSS, JavaScript, animations, fireworks — is self-contained inside `monika_birthday.py`. No external files needed.

---

## 🎮 Interactive Features

| Feature | How to Trigger |
|---------|---------------|
| 🔓 Unlock Door | Click the arched door on Scene 1 |
| 💌 Open Envelope | Click the envelope on Scene 2 |
| 💕 With Love | Click the pill button on Scene 3 |
| 🌟 My Wish | Click the pill button on Scene 3 |
| ✨ Forever | Click the pill button on Scene 3 |
| 🎂 Blow Candles | Tap the cake — fireworks + wish popup appears |
| ✦ Sparkles | Every click anywhere spawns sparkles |
| 💗 Hearts | Float up from every interaction |

---

## 🎨 Design Details

- **Fonts** — Playfair Display · Cormorant Garamond · Dancing Script (Google Fonts)
- **Color Palette** — Deep rose `#c0576e` · Blush `#f2a0b0` · Gold `#e8c97a` · Dark plum `#1a0a10`
- **Animations** — CSS keyframes · Canvas particle system · Canvas fireworks engine
- **Custom cursor** — Gold dot with rose ring trail that follows the mouse

---

## 💬 Personalisation

Want to change the messages? Open `monika_birthday.py` and find the `wishes` object in the JavaScript section:

```javascript
const wishes = {
  birthday: {
    emoji: '🎂',
    heading: 'Happy Birthday, My Love!',
    text: 'May this year bring you everything your heart desires...'
  },
  love: { ... },
  wish: { ... },
  forever: { ... },
  more: { ... }
};
```

Change any `heading` or `text` value to your own words. 💗

---

## 🛠 Requirements

| Package | Version |
|---------|---------|
| Python  | ≥ 3.8   |
| streamlit | ≥ 1.28 |

---

## 📜 License

Made with love. Free to use, share, and personalise for someone special. 🌹

---

> *"You are the most beautiful reason I smile a little brighter every single day."*
