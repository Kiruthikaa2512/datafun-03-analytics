# datafun-03-analytics

## Overview
This project focuses on reading, processing, and writing different types of data files using the collection types. 

## Local Machine Setup

### Step 1: Install Python (if not installed)

- Download from: https://www.python.org/downloads/
- Verify installation:

```bash
python --version
````

---

##  Project Initialization & GitHub Setup

### Step 2: Create and Clone GitHub Repo

1. Navigate to [GitHub](https://github.com/)
2. Create a new repository named: `datafun-03-analytics`
3. Select:  **Add a README.md**
4. Clone the repo locally:

```bash
git clone https://github.com/YOUR-USERNAME/datafun-03-analytics.git
cd datafun-03/analytics
```

---

### Step 3: Set Up Version Control

#### Add `.gitignore`

```bash
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
```

#### Track Files with Git

```bash
git add .
git commit -m "Initial commit with project structure"
git push origin main
```

---

##  Virtual Environment & Dependency Setup

### Step 4: Set Up Python Environment

#### Create virtual environment:

```bash
python -m venv venv
```

#### Activate environment:

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```

* **Mac/Linux:**

  ```bash
  source venv/bin/activate
  ```

---

### Step 5: Manage Dependencies

#### Add Required Libraries

```bash
pip install pandas
```

#### Freeze dependencies

```bash
pip freeze > requirements.txt
```

#### Step 6: 
Create .gitignore, requirements.txt with external dependency
'requests' as the content by having all other comments commented out!
---