# FitLog

<!-- Main screenshot - larger display -->
<h3>🏁 Welcome Screen</h3>
<img src="static/readme_images/main-page.jpg" alt="Main Page" style="max-width: 500px; border: 1px solid #ccc; border-radius: 8px; margin-bottom: 20px;" />

FitLog is a wellbeing tracking app designed to help users log their moods and workouts to support physical and emotional health.  
👉 **Live Site:** https://fitlog-app-ivo-6b411ba5300f.herokuapp.com/

---

## 📑 Table of Contents

- [🧠 User Experience Design](#-user-experience-design)
- [📌 Scope Plane](#-scope-plane)
- [🏗 Structure Plane](#-structure-plane)
- [📐 Skeleton Plane](#-skeleton-plane)
- [🎨 Surface Plane](#-surface-plane)
- [🛠 Technologies](#-technologies)
- [✅ Testing](#-testing)
- [🚀 Deployment](#-deployment)
- [💬 Credits](#-credits)

---

## 🧠 User Experience Design

### 🎯 Strategy Plane
The goal of FitLog is to provide users with a simple and intuitive tool to track their wellbeing through mood logging and workout tracking.

### 🗂 Agile Planning
The project followed Agile methodology using GitHub Projects with epics, sprints, and user stories.

### 🧩 Epics
1. Base Setup  
2. Authentication  
3. Mood Logging  
4. Workout Logging  
5. UI / Navigation  
6. Deployment  
7. Documentation  

### 👤 User Stories
- Register and log in  
- Add/edit/delete moods  
- Add/edit/delete workouts  
- Navigate the app  
- Log out securely  

---

## 📌 Scope Plane
MVP includes:
- Authentication  
- Mood CRUD  
- Workout CRUD  
- Responsive layout  
- Navigation  

---

## 🏗 Structure Plane

### 🔧 Features
- Mood & Workout logs  
- Form validation  
- User-specific querysets  
- Authentication redirects  

### 🧪 Features Left to Implement
- Mood graphs  
- Profile stats  
- Motivational reminders  

---

## 📐 Skeleton Plane

### 📲 Wireframes
Mobile-first layout for all major pages:
- Homepage  
- Mood pages  
- Workout pages  
- Login/Register  

---

## 🎨 Surface Plane

### 🖼 Design
Light, uplifting layout.

### 🌈 Colour Scheme
- #fffbe6  
- #fff3cd  
- Bootstrap defaults  

### 🔤 Typography
Segoe UI + sans-serif fallback

### 🖌 Imagery
- AI illustration  
- FontAwesome icons  
- Canva favicon  

---

## 🛠 Technologies

- **Frontend:** HTML, Bootstrap  
- **Backend:** Django  
- **Database:** SQLite (dev), PostgreSQL (production)  
- **Deployment:** Heroku  
- **Version Control:** Git & GitHub  
- **Extras:** dotenv, widget-tweaks  

---

# ✅ Testing

The following extensive testing confirms the stability, security, and reliability of FitLog.

---

# 🔍 1. Testing Overview
All critical areas were tested manually across multiple devices and browsers:

- Authentication & permissions  
- CRUD for moods & workouts  
- Template rendering  
- Form validation  
- Redirects & user flow  
- Responsive design  
- Security (user data isolation)  
- Validators (HTML, CSS, Python)  

---

# 👀 2. Manual Testing (Multi-Browser)

Tested on:
- Chrome  
- Safari (macOS & iOS)  
- Firefox  
- Edge  
- iPhone  
- iPad  
- Android  

---

# 🧪 2.1 Manual Test Cases
*(Screenshots included in repository)*
<img src="static/readme_images/Manual Test Cases.jpg" alt="Manual Test Cases" style="max-width: 250px; border: 1px solid #ccc; border-radius: 8px; margin-bottom: 20px;" />

---

# 👤 3. User Story Testing
<img src="static/readme_images/User Story Testing.jpg" alt="User Story Testing" style="max-width: 250px; border: 1px solid #ccc; border-radius: 8px; margin-bottom: 20px;" />

---

# 📝 4. Form Validation Testing
<img src="static/readme_images/Form Validation Testing.jpg" alt="Form Validation Testing" style="max-width: 250px; border: 1px solid #ccc; border-radius: 8px; margin-bottom: 20px;" />

---

# 🔐 5. Authentication & Authorization Testing

| Scenario | Expected | Result |
|----------|----------|--------|
| Access `/moods/` without login | Redirect to login | ✔ |
| Edit/Delete other user’s data | Blocked (404) | ✔ |
| Logout ends session | Works | ✔ |
| Restricted pages protected | Works | ✔ |

---

# 🔄 6. CRUD Testing

### Create
✔ Works for both Mood and Workout entries

### Read  
✔ Users only see their own entries

### Update  
✔ All forms prepopulate and save correctly

### Delete  
✔ Fully fixed — both templates implemented:  
- `tracker/mood_confirm_delete.html`  
- `tracker/workout_confirm_delete.html`

No more server errors.

---

# 📱 7. Responsive Design Testing

| Device | Browser | Result |
|--------|---------|--------|
| iPhone 14 | Safari | ✔ |
| Galaxy S21 | Chrome | ✔ |
| iPad Air | Safari | ✔ |
| MacBook | Chrome/Safari | ✔ |

---

# ✔ 8. Validator Testing

### HTML / CSS  
✔ Passed W3C validators (minor warnings only)

### Python  
✔ Checked with PEP8 online and CI Python Linter  
✔ No errors (minor spacing warnings resolved)

<img src="static/readme_images/Validator Testing.jpg" alt="Validator Testing" style="max-width: 250px; border: 1px solid #ccc; border-radius: 8px; margin-bottom: 20px;" />

---

# 📊 9. Lighthouse Audit

FitLog was evaluated using Lighthouse (Chrome DevTools). Performance metrics on Heroku-based applications can fluctuate due to the platform’s dyno wake-up time, which adds a brief initial delay after periods of inactivity. This behaviour is expected and unrelated to the application’s code quality.

**Desktop results (Chrome):**
- **Performance:** Variable (due to Heroku cold-start behaviour)
- **Accessibility:** 21 / 22  
- **Best Practices:** 5 / 6  
- **SEO:** 4 / 6  

Mobile results follow the same pattern, with natural variation caused by Lighthouse’s mobile throttling. 
No critical issues were identified across categories.
---

# 🐞 10. Bugs & Fixes

### Fixed:
- Workout delete → crash (missing template)  
- Mood delete confirmation page added  
- Navbar duplication removed  
- PEP8 cleanup  
- Removed old `.env` and added `.gitignore`  
- Improved form styling and spacing  

### Known:
- Minor Bootstrap contrast warnings (non-critical)

---

# 💯 Conclusion

All features work as intended.  
All required tests have been completed and documented.  
FitLog now meets the project requirements in full.

---

## 🚀 Deployment

### 🔁 Version Control
```bash
git add .
git commit -m "Updated README with full testing section and fixes"
git push origin main
```

### 🌐 Heroku Deployment
- PostgreSQL via Heroku add-on  
- Config Vars set  
- Static files via WhiteNoise  
- Automatic deploy from GitHub  

### 💻 Run Locally
```bash
git clone https://github.com/your-username/fitlog.git
cd fitlog
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 💬 Credits

- Code Institute “Sizzle & Steak”  
- FontAwesome  
- Canva  
- TinyPNG  
- W3 Validators  
- OpenAI GPT (technical guidance)

---

### 🔗 Live Project  
https://fitlog-app-ivo-6b411ba5300f.herokuapp.com/
