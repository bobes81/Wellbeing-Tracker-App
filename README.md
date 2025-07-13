# FitLog

FitLog is a wellbeing tracking app designed to help users log their moods and workouts to support physical and emotional health. The live app can be accessed here: [Live Site - FitLog](https://fitlog-app-ivo-6b411ba5300f.herokuapp.com/)

---

## Table of Contents

* [User Experience Design](#user-experience-design)

  * [Strategy Plane](#strategy-plane)
  * [Agile Planning](#agile-planning)
  * [Epics](#epics)
  * [User Stories](#user-stories)
* [Scope Plane](#scope-plane)
* [Structure Plane](#structure-plane)
* [Skeleton Plane](#skeleton-plane)

  * [Wireframes](#wireframes)
* [Surface Plane](#surface-plane)

  * [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
* [Technologies](#technologies)
* [Testing](#testing)
* [Deployment](#deployment)

  * [Version Control](#version-control)
  * [Heroku Deployment](#heroku-deployment)
  * [Run Locally](#run-locally)
  * [Fork Project](#fork-project)
* [Credits](#credits)

---

## User Experience Design

### Strategy Plane

The goal of FitLog is to provide users with a simple and intuitive tool to track their wellbeing through mood logging and workout tracking. The platform promotes self-awareness and long-term health improvements.

### Agile Planning

The project was developed using agile methodology across 3 sprints. GitHub Projects was used to manage user stories and progress.

### Epics

1. **Base Setup**
2. **Authentication**
3. **Mood Logging**
4. **Workout Tracking**
5. **Homepage and Navigation**
6. **Deployment**
7. **Documentation**

### User Stories (Examples)

* As a user, I want to register and log in so I can track my progress.
* As a user, I want to log my current mood so I can reflect on my emotional state.
* As a user, I want to add, edit, and delete workouts to keep my exercise routine updated.
* As a user, I want to log out securely.

---

## Scope Plane

* Fully responsive design
* Secure user authentication
* CRUD functionality for moods and workouts
* Intuitive dashboard with visual hierarchy

---

## Structure Plane

### Features

* **Mood Logs:** Create, update, delete, and view daily mood entries
* **Workout Logs:** Track workouts with date, type, and duration
* **User Auth:** Custom login, register, and logout views with Django messages

### Features Left to Implement

* Data visualizations (e.g. mood trends over time)
* Profile pages with stats

---

## Skeleton Plane

### Wireframes

Wireframes were designed to prioritize clarity and mobile responsiveness. Key views:

* Homepage
* Mood Log List
* Workout Log List
* Mood & Workout Forms
* Login / Register

---

## Surface Plane

### Design

The interface was kept light and accessible with friendly language and icons.

### Colour Scheme

* Background: Vanilla (#fffbe6)
* Hero section: Soft yellow (#fff3cd)
* Buttons: Bootstrap primary and success variants

### Typography

* Main font: "Segoe UI", system sans-serif stack

### Imagery

* A custom hero illustration symbolizes wellbeing

---

## Technologies

* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Backend:** Python, Django
* **Database:** SQLite (development), PostgreSQL (production)
* **Deployment:** Heroku
* **Version Control:** Git & GitHub
* **Design tools:** Canva (illustration), TinyPNG (compression)

---

## Testing

### Manual Testing

All CRUD operations were manually tested across the following browsers:

* Chrome
* Safari (Mac & iOS)
* Firefox

### Test Cases

| Feature     | Expected Result                        | Outcome                                      |
| ----------- | -------------------------------------- | -------------------------------------------- |
| Register    | User is created and redirected         | Pass ✅                                       |
| Login       | Valid credentials redirect to homepage | Pass ✅                                       |
| Add Mood    | New mood is saved and shown            | Pass ✅                                       |
| Edit Mood   | Entry is updated correctly             | Pass ✅                                       |
| Delete Mood | Mood is removed                        | Pass ✅                                       |
| Add Workout | Workout appears in list                | Pass ✅                                       |
| Logout      | User is redirected and session ends    | Pass ✅ (after setting LOGOUT\_REDIRECT\_URL) |

### Lighthouse Audit

* Performance: ✅
* Accessibility: Minor improvements suggested (e.g., button naming)
* Best Practices: ✅
* SEO: Add meta description – planned

---

## Deployment

### Version Control

Git was used for local commits and GitHub for remote repository:

```bash
git add .
git commit -m "Meaningful message"
git push origin main
```

### Heroku Deployment

1. Create a Heroku app
2. Set environment variables (SECRET\_KEY, DEBUG, ALLOWED\_HOSTS, etc.)
3. Add PostgreSQL addon
4. Push from GitHub or connect via Heroku CLI
5. Deploy from `main` branch

### Run Locally

```bash
git clone https://github.com/your-username/fitlog.git
cd fitlog
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Fork Project

Go to the GitHub repository and click **Fork** to create your own copy.

---

## Credits

* **Mentor Support:** Code Institute
* **Illustrations:** Custom generated with AI
* **Hero Image Compression:** [TinyPNG](https://tinypng.com)
* **Design Reference:** Based on "Sizzle and Steak" by mentor

---

**Live App:** [https://fitlog-app-ivo-6b411ba5300f.herokuapp.com/](https://fitlog-app-ivo-6b411ba5300f.herokuapp.com/)
