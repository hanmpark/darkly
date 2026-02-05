# Darkly

<p align="center">
  <img src="https://img.shields.io/badge/42-Darkly-111111?style=for-the-badge" alt="42 Darkly">
  <img src="https://img.shields.io/badge/Status-14%2F14%20labs%20documented-2ea44f?style=for-the-badge" alt="Status 14/14">
  <img src="https://img.shields.io/badge/Focus-Web%20Application%20Security-0366d6?style=for-the-badge" alt="Web Application Security">
</p>

<p align="center">
  A practical security notebook for the 42 <code>Darkly</code> project.<br>
  Each lab captures how the flag was found and how the vulnerability should be fixed.
</p>

---

## Project overview

This repository contains **14 web security labs** (from `00` to `13`), each focused on one vulnerability class.

For every lab, you will find:
- a step-by-step write-up in `Resources/README.md`
- supporting artifacts (screenshots, scripts, payloads)
- the final `flag`

The documentation style is consistent: **how to exploit** and **how to prevent**.

---

## Lab index

| # | Vulnerability | Directory |
|---|---|---|
| 00 | Information disclosure | [`00-information-disclosure`](00-information-disclosure) |
| 01 | Client-side validation bypass | [`01-survey-client-side-validation`](01-survey-client-side-validation) |
| 02 | Cookie tampering | [`02-cookie-tampering`](02-cookie-tampering) |
| 03 | Stored XSS (feedback) | [`03-feedback-stored-xss`](03-feedback-stored-xss) |
| 04 | User-controlled parameter abuse | [`04-footer-user-controlled-parameter`](04-footer-user-controlled-parameter) |
| 05 | XSS via image/home page flow | [`05-home-image-xss`](05-home-image-xss) |
| 06 | Path traversal | [`06-path-traversal`](06-path-traversal) |
| 07 | Sensitive file disclosure | [`07-sensitive-file-disclosure`](07-sensitive-file-disclosure) |
| 08 | Brute-force login | [`08-brute-force-login`](08-brute-force-login) |
| 09 | Hidden directory disclosure | [`09-hidden-directory-disclosure`](09-hidden-directory-disclosure) |
| 10 | SQL injection (member search) | [`10-member-sql-injection`](10-member-sql-injection) |
| 11 | SQL injection (image endpoint) | [`11-image-sql-injection`](11-image-sql-injection) |
| 12 | Header-based access control flaw | [`12-copyright-header-based-access-control`](12-copyright-header-based-access-control) |
| 13 | Insecure file upload (MIME trust) | [`13-insecure-file-upload-MIME`](13-insecure-file-upload-MIME) |

---

## Repository layout

```text
darkly/
├── 00-information-disclosure/
│   ├── Resources/
│   │   ├── README.md
│   │   └── ...
│   └── flag
├── ...
└── 13-insecure-file-upload-MIME/
    ├── Resources/
    │   ├── README.md
    │   └── script.php
    └── flag
```

---

## How to use this repository

1. Start from lab `00` and progress in order.
2. Read `Resources/README.md` for exploitation steps and reasoning.
3. Review the **how to avoid** section to map each issue to defensive practices.
4. Reproduce only in authorized environments (CTF/lab setups).

---

## Security themes covered

- Trust boundaries (never trust client input)
- Access control weaknesses
- Injection vulnerabilities (XSS, SQLi)
- File system exposure (path traversal, hidden resources)
- Authentication hardening (brute-force resistance)
- Upload validation and execution safety

---

## Disclaimer

This repository is for **educational use** and defensive security training.
Do not apply these techniques against systems without explicit permission.
