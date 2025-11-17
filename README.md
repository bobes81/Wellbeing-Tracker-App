# FitLog

<!-- Main screenshot - larger display -->
<h3>🏁 Welcome Screen</h3>
<img src="static/readme_images/main-page.jpg" alt="Main Page" style="max-width: 500px; border: 1px solid #ccc; border-radius: 8px; margin-bottom: 20px;" />

FitLog is a wellbeing tracking app designed to help users log their moods and workouts to support physical and emotional health.  
👉 [Live Site - FitLog](https://fitlog-app-ivo-6b411ba5300f.herokuapp.com/)

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

### 📱 Responsive Views
*(screenshots omitted here for brevity — same as before)*

---

## 🛠 Technologies

- **Frontend:** HTML, Bootstrap  
- **Backend:** Django  
- **DB:** SQLite / PostgreSQL  
- **Deployment:** Heroku  
- **Version Control:** Git & GitHub  
- **Extras:** dotenv, widget-tweaks  

---

# ✅ Testing

The following extensive testing confirms the stability, security, and reliability of FitLog.

---

# 🔍 1. Testing Overview
All critical areas were tested:
- Authentication  
- CRUD for moods & workouts  
- Template rendering  
- Form validation  
- API logic  
- Responsive design  
- Permissions & security  

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

| Feature | Test Steps | Expected | Actual | Result |
|--------|------------|----------|--------|--------|
| Register | Fill form → submit | Redirect to home | Works | ✅ |
| Login | Enter credentials | Logged in | Works | ✅ |
| Logout | Click logout | Session cleared | Works | ✅ |
| Add Mood | Submit valid form | Mood added | Works | ✅ |
| Edit Mood | Change fields | Saved | Works | ✅ |
| Delete Mood | Confirm deletion | Removed | Works | ✅ |
| Add Workout | Submit form | Workout added | Works | ✅ |
| Edit Workout | Modify entry | Updated | Works | ✅ |
| Delete Workout | Confirm | Removed | Works after fix | ✅ |
| 404 Page | Wrong URL | Custom page | Works | ✅ |

---

# 👤 3. User Story Testing

### US1 – Register
✔ Works

### US2 – Log In
✔ Works

### US3 – CRUD Moods
✔ All operations functional

### US4 – CRUD Workouts
✔ All operations functional after delete template fix

### US5 – Responsive UI
✔ Verified on all tested devices

---

# 📝 4. Form Validation Testing

### Mood Form
- Empty fields → Errors (✔)
- Valid input → Saved (✔)

### Workout Form
- Valid input → Saved (✔)
- Bad/missing data → Errors (✔)

### Security
- CSRF tokens present on all forms (✔)

---

# 🔐 5. Authentication & Authorization Testing

| Scenario | Expected | Result |
|----------|----------|--------|
| Access /moods/ without login | Redirect to login | ✔ |
| Edit/Delete other user’s data | Blocked (404) | ✔ |
| Logout destroys session | Works | ✔ |

---

# 🔄 6. CRUD Testing

### Create
✔ Works for both models

### Read
✔ Only user’s own entries shown

### Update
✔ Saves correctly

### Delete  
✔ Fixed with correct templates:  
- `tracker/mood_confirm_delete.html`  
- `tracker/workout_confirm_delete.html`

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

### HTML
No major errors

### CSS
Valid

### Python (PEP8)
Minor spacing resolved

### JSHint
No issues

---

# 📊 9. Lighthouse Audit

- **Performance:** High  
- **Accessibility:** Minor contrast warnings  
- **Best Practices:** 100  
- **SEO:** 100  

---

# 🐞 10. Bugs & Fixes

### Fixed:
- Workout delete → crash (missing template)  
- Mood delete template added  
- Navbar duplication removed  
- Code cleaned for PEP8  
- Old `.env` removed; `.gitignore` added  

### Known:
- Bootstrap contrast warnings (non-critical)

---

# 💯 Conclusion

All required tests have been documented and performed.  
FitLog now meets LO4 Testing requirements in full.

---

## 🚀 Deployment

### 🔁 Version Control
```bash
git add .
git commit -m "Updated README with full testing section and fixes"
git push origin main
```

### 🌐 Heroku Deployment
- Uses PostgreSQL  
- Config Vars set  
- Static files handled via WhiteNoise

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
