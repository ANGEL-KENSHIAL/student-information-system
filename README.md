# STUDENT INFORMATION SYSTEM

---

## PROJECT SUMMARY

| Item     | Details                                                                                                                                        |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Project  | Student Information System                                                                                                                     |
| Purpose  | Collect student details, generate username & email (using string concatenation), display a professional table, and optionally save the profile |
| Language | Python 3.7+                                                                                                                                    |
| Author   | KENSHIAL SAMUEL                                                                                                                                |
| GitHub   | ANGEL-KENSHIAL                                                                                                                                 |

---

## KEY FEATURES

| Feature             | Description                                                                |
| ------------------- | -------------------------------------------------------------------------- |
| Console UI          | Clean table-style console output with programmatically built borders       |
| Input Validation    | Prevents empty entries; sanitizes names (capitalizes parts)                |
| Username Generation | First 3 letters of compacted name (lowercase) + Student ID (concatenation) |
| Email Generation    | username + `@st.ug.edu.gh` (concatenation)                                 |
| Save to File        | Optionally saves the profile to `<username>_profile.txt`                   |

---

## HOW USERNAME & E-MAIL ARE BUILT (Concatenation)

| Step | Operation                                        | Example                                                         |
| ---: | ------------------------------------------------ | --------------------------------------------------------------- |
|    1 | Compact name: remove spaces and lowercase prefix | "Kenshial Samuel" → "KenshialSamuel" → prefix "ken"             |
|    2 | Username: prefix + Student ID (using `+`)        | "ken" + "22414971" = `ken22414971`                              |
|    3 | Email: username + domain (using `+`)             | `ken22414971` + `"@st.ug.edu.gh"` = `ken224149715@st.ug.edu.gh` |

---

## INSTALLATION & RUNNING (Quick)

| Step | Command / Action                                  |
| ---: | ------------------------------------------------- |
|    1 | Clone repo: `git clone <repo-url>`                |
|    2 | Enter dir: `cd student-information-system`        |
|    3 | Run script: `python student_information.py`       |
|    4 | Follow prompts; choose to save profile when asked |

---

## SAMPLE PROFILE

| FIELD                | VALUE                       |
| -------------------- | --------------------------- |
| Full Name            | Kenshial Samuel             |
| Student ID           | 22414971                    |
| Programme            | BSc. Information Technology |
| Level                | 200                         |
| Age                  | 24                          |
| Hall of Residence    | Akuafo                      |
| Favourite Language   | Python                      |
| Generated Username   | ken22414971                 |
| Generated Email      | ken22414971@st.ug.edu.gh    |
| Profile generated at | 2026-08-25 00:49:07         |

---

## PROJECT FILES

| File                   | Purpose                                                       |
| ---------------------- | ------------------------------------------------------------- |
| student_information.py | Main program (input, processing, table output, optional save) |
| README.md              | Project documentation (this file)                             |
| .gitignore             | Ignore Python artifacts (e.g., **pycache**)                   |

---

## GIT WORKFLOW

| Action              | Example Message                                               |
| ------------------- | ------------------------------------------------------------- |
| Initial commit      | "Initial project setup"                                       |
| Add inputs          | "Add input collection"                                        |
| Concatenation logic | "Add generated username and email using string concatenation" |
| UI & save feature   | "Add formatted table output and save-to-file option"          |

---
