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
The aim of FitLog is to offer a simple and intuitive tool to track wellbeing through mood logs and workout entries.

### 🗂 Agile Planning
The project was planned using GitHub Projects with epics, user stories, and iterative development.

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
- User authentication  
- Mood CRUD  
- Workout CRUD  
- Navigation  
- Responsive layout  

---

## 🏗 Structure Plane

### 🔧 Features
- Mood & Workout logs  
- Form validation  
- User-specific querysets  
- Authentication redirects  

### 🧪 Features Left to Implement
- Mood graphs  
- Profile statistics  
- Motivational reminders  

---

## 📐 Skeleton Plane

### 📲 Wireframes
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
- Bootstrap palette  

### 🔤 Typography
Segoe UI + sans-serif

### 🖌 Imagery
- AI illustration  
- FontAwesome icons  
- Canva favicon  

---

## 🛠 Technologies

- **Frontend:** HTML, Bootstrap  
- **Backend:** Django  
- **Database:** SQLite (development), PostgreSQL (production)  
- **Deployment:** Heroku  
- **Version Control:** Git & GitHub  
- **Extras:** dotenv, widget-tweaks  

---

# ✅ Testing

A full set of manual tests was completed to ensure functionality, stability, and reliability across devices.

---

# 🔍 1. Testing Overview
Tested areas include:
- Authentication  
- CRUD for moods & workouts  
- Validation  
- Redirects  
- Responsive layout  
- User permissions  
- Template rendering  
- Code validation  

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
<img src="static/readme_images/Manual Test Cases.jpg" alt="Manual Test Cases" style="max-width: 250px;" />

---

# 👤 3. User Story Testing
<img src="static/readme_images/User Story Testing.jpg" alt="User Story Testing" style="max-width: 250px;" />

---

# 📝 4. Form Validation Testing
<img src="static/readme_images/Form Validation Testing.jpg" alt="Form Validation Testing" style="max-width: 250px;" />

---

# 🔐 5. Authentication & Authorization Testing

| Scenario | Expected | Result |
|----------|----------|--------|
| Access `/moods/` without login | Redirect to login | ✔ |
| Edit/Delete another user’s data | Blocked (404) | ✔ |
| Logout ends session | Works | ✔ |
| Restricted pages protected | ✔ |

---

# 🔄 6. CRUD Testing

### Create  
✔ Works for both Mood and Workout

### Read  
✔ Only user-owned entries displayed

### Update  
✔ Forms prefill correctly and save

### Delete  
✔ Fully functional with confirmation pages:  
- `tracker/mood_confirm_delete.html`  
- `tracker/workout_confirm_delete.html`

---

# 🧱 7. Custom Error Pages

FitLog includes a fully implemented **custom 404 error page**, required by the project.

- Works with `DEBUG=False`  
- Registered in `fitlog_project/urls.py` via `handler404`  
- Template located at `templates/404.html`  
- Tested by navigating to a non-existent URL (returns custom page instead of Django error)

This ensures a polished user experience even when pages do not exist.

---

# 📱 8. Responsive Design Testing

| Device | Browser | Result |
|--------|---------|--------|
| iPhone 14 | Safari | ✔ |
| Galaxy S21 | Chrome | ✔ |
| iPad Air | Safari | ✔ |
| MacBook | Chrome/Safari | ✔ |

---

# ✔ 9. Validator Testing

### HTML/CSS  
✔ Passed W3C validators (minor warnings only)

### Python  
✔ Clean according to PEP8 online validator  
<img src="static/readme_images/Validator Testing.jpg" alt="Validator Testing" style="max-width: 250px;" />

---

# 📊 10. Lighthouse Audit

FitLog was tested using Lighthouse in Chrome DevTools.  
Heroku applications experience **dyno cold-start delays**, which can temporarily lower performance scores; this is expected behaviour and not related to code issues.

### Desktop Results:
- **Performance:** Variable (affected by Heroku cold start)  
- **Accessibility:** 21 / 22  
- **Best Practices:** 5 / 6  
- **SEO:** 4 / 6  

Mobile scores follow the same pattern, with minor variations from throttling.

No critical issues were identified.

---

# 🐞 11. Bugs & Fixes

### Fixed:
- Workout delete crash  
- Missing delete templates  
- Navbar duplication  
- PEP8 inconsistencies  
- Removed old `.env`  
- Added `.gitignore`  
- Improved form spacing  

### Known:
- Minor Bootstrap contrast warnings  

---

# 💯 Conclusion

FitLog functions as intended.  
All testing has been completed.  
All project requirements are met.  

---

## 🚀 Deployment

### 🔁 Version Control
```bash
git add .
git commit -m "Updated README and added full testing section"
git push origin main
```

### 🌐 Heroku Deployment
- PostgreSQL add-on  
- Config Vars set  
- WhiteNoise for static files  
- Deployment via GitHub  

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
