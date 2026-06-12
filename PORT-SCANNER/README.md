# 🔍 Port Scanner
<img width="2006" height="981" alt="download (23)" src="https://github.com/user-attachments/assets/dd4e1292-0daa-4b5c-9b91-d25fd84c3575" />

A simple network port scanner built in Python on Kali Linux.  
Scans a target IP for open ports and identifies the service running on each one.

---

## 📌 About
This was my first hands-on cybersecurity project, built from scratch on Kali Linux using nothing but Python's built-in `socket` library. No external dependencies, no frameworks. Just few lines that knock on 1,024 doors and report back what answers.

Full writeup: [Your Computer Has 65,535 Doors. I Wrote Code to Check Which Ones Are Open](https://rain-dolls.hashnode.dev/)

---

## ⚙️ Tech Used

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| `socket` | Built-in networking library |
| Kali Linux | Environment |

---

## 🚀 How to Run

```bash
python3 portscanner.py
```

No installation needed. `socket` ships with Python.

---

## 📤 Sample Output

**Clean machine (no services running):**
```
scanning 127.0.0.1...
scan complete
```

**With a service running:**
```
scanning 127.0.0.1...
port 8080 is OPEN (http-alt)
scan complete
```

---

## 🧠 What I Learned

- How ports map to services (HTTP, SSH, SMB, and more)
- How socket connections work under the hood
- The difference between scanning localhost vs a live machine
- Why open ports matter in a security context
- That port 445 has a history worth knowing about

---

## ⚠️ Legal Note

Only scan systems you own or have explicit permission to test.  
This tool is for educational and authorized use only.

---

## 📖 Part of

**Journals of a Novice - Tier 0**  
A documented journey into cybersecurity from the ground up.

<img width="900" height="540" alt="Your Computer Has 65,535 Doors  I Wrote Code to Check Which Ones Are Open" src="https://github.com/user-attachments/assets/ae17fbb8-14fb-42ed-aeab-42f49a6caf31" />

Blog: [rain-dolls on Hashnode](https://rain-dolls.hashnode.dev/)
