# FINDEVIL-001 — Terry USB Drive Analysis Report
**Image:** `~/cases/FINDEVIL-001/terry-usb.E01`  
**Analyst:** Claude Code (SIFT Workstation)  
**Date:** 2026-05-26 UTC  
**MD5:** `e07f26954b23db1a44dfd28ecd717da9` ✓ Verified

---

## Executive Summary

Terry's USB drive contains a **commercial keylogger tool and its output logs**, **cover traffic automation scripts**, and **VNC remote access software** — a complete insider-threat toolkit. The keylogger ("XP Advanced Keylogger V2.1") captured five consecutive days of activity (2009-12-03 through 2009-12-07) on a Windows machine with local username **"Pat"**, recording credentials, clipboard contents, and 2,471 screenshots. The captured keystrokes include repeated brute-force credential attempts against the M57 company network share (`\\192.168.1.1\m57`) and a direct memory access attempt. Cover traffic scripts authored by "LCDR Kris Kearton" were designed to generate fake browsing patterns and mask surveillance activity.

---

## Image Metadata

| Field | Value |
|-------|-------|
| Format | EnCase 6 (EWF) |
| Acquisition date | 2011-01-19 17:09:54 UTC |
| Media type | Fixed disk (physical) |
| Size | 1.9 GiB (2,097,152,000 bytes) |
| Sector size | 512 bytes |
| Filesystem | FAT32, partition offset sector 63 |
| Set GUID | 4442dcc6-a2a6-8a42-9137-fbe3be4ae9a2 |
| MD5 (stored) | e07f26954b23db1a44dfd28ecd717da9 |
| MD5 (computed) | e07f26954b23db1a44dfd28ecd717da9 ✓ |

**Note:** macOS resource fork files (`._*`) and `.Spotlight-V100`/`.Trashes` directories confirm this USB was previously mounted on a Mac OS X system.

---

## Files on Drive (Allocated)

| File | Size | Date (UTC) | Significance |
|------|------|------------|--------------|
| `R54402.EXE` | 4.1 MB | 2009-11-20 | Self-extracting ZIP (Xceed), contains VNC — likely keylogger/RAT installer |
| `vnc-4_1_3-x86_win32.exe` | 741 KB | 2008-10-15 | VNC 4.1.3 Windows installer — remote access tool |
| `Log/2009-12-03.htm` | 432 KB | 2009-12-03 | Keylogger HTML report, Day 1 |
| `Log/2009-12-04.htm` | — | 2009-12-04 | Keylogger HTML report, Day 2 |
| `Log/2009-12-05.htm` | — | 2009-12-05 | Keylogger HTML report, Day 3 |
| `Log/2009-12-06.htm` | — | 2009-12-06 | Keylogger HTML report, Day 4 |
| `Log/2009-12-07.htm` | — | 2009-12-07 | Keylogger HTML report, Day 5 |
| `patentauto.py` | 3.7 KB | 2009-11-17 | Cover traffic generator (patent searches) |
| `webauto.py` | 2.2 KB | 2009-11-16 | Cover traffic generator (persona URLs) |
| `patentterms.txt` | 140 B | 2009-11-16 | Patent search seed terms |
| `urlspersona.txt` | 1.7 KB | 2009-11-14 | Persona URL list for fake browsing |
| `urlscopyright.txt` | 377 KB | 2009-11-17 | URL feed for cover traffic |
| `urlscryptography.txt` | 300 KB | 2009-11-16 | URL feed for cover traffic |
| `urlspatents.txt` | 5.4 MB | 2009-11-17 | URL feed for cover traffic |
| `urlstime_machine.txt` | 1.5 MB | 2009-11-16 | URL feed for cover traffic |
| `M57biz.jpg` | 380 KB | 2009-11-17 | M57 business image |

**Total Log directory:** 4,996 files (Dec 3–7 screenshots + HTML reports), ~61 MB

---

## Deleted Files

None. No file slack or deleted entries recovered from FAT32 partition.

---

## Malicious Artifacts — Detail

### 1. Keylogger: XP Advanced Keylogger V2.1

**Installed path on victim machine:** `C:\Program Files\XP Advanced\ToolKeylogger.exe`  
**Logged user:** Pat  
**Log format:** Daily HTML reports with screenshots, keystrokes, clipboard captures, and window titles  

#### Event counts per day:

| Date | Keystroke Events | Screenshot Events |
|------|-----------------|-------------------|
| 2009-12-03 | 2 | 334 |
| 2009-12-04 | 1 | 459 |
| 2009-12-05 | 0 | 720 |
| 2009-12-06 | 4 | 717 |
| 2009-12-07 | 3 | 241 |
| **Total** | **10** | **2,471** |

#### Captured Keystrokes (verbatim, with commentary):

**2009-12-03 10:21:41** — Password field entry:
```
admin[TAB]adminTerryhard drive[BACK]×6drivepolicestealingsteal
```
Parsed: username=`admin`, password attempt containing "Terry", then typed incriminating words "police", "stealing", "steal" — either into a password field or a visible text field.

**2009-12-03** — Outbound email text (Microsoft Outlook):
```
Thanks for stopping by...it is running quite a bit faster.
- Pat
```

**2009-12-04** — Email to Terry:
```
Terry, is the anti-virus working? I think there is something wrong with mine... Pat
```
Possible social engineering to get Terry to check/disable AV.

**2009-12-04 (×5 attempts)** — Repeated credential brute-force:
```
Incorrect password or unknown username for: \\192.168.1.1\m57
  Username: m57admin
  Password: admin01
```

**2009-12-06** — Direct memory access attempt:
```
\\.\PhysicalMemory
```
This is the Windows raw physical memory device path — used by malware, memory acquisition tools, and forensic tools to directly read RAM.

**2009-12-06** — Additional credential attempts + command execution:
```
cmd
\\192.168.1.1\m57
m57admin [TAB] admin01
```

**2009-12-07** — Log review:
```
logs  20091203
```
User accessed the keylogger logs from Dec 3.

#### Clipboard Capture (2009-12-03):
A large batch of U.S. government URLs was in the clipboard (`.gov`, `.loc.gov`, NASA, NIH, DOE, USDA, NSF) — consistent with the cover traffic URL lists also on the USB drive.

---

### 2. R54402.EXE — Suspicious Self-Extracting Archive

| Field | Value |
|-------|-------|
| MD5 | `55f9facaec8cf1d1bf1f8c04f3d287a4` |
| Type | PE32 executable, MS Windows 4.00 GUI, i386 |
| Packer | Xceed Absolute Packager v1.1 (SFX ZIP) |
| Signing | VeriSign Class 3 code signing certificate |

**Key strings extracted:**
- `?VnC` — embedded VNC reference
- `xcdGetPasswordClass` — Xceed password class for SFX protection
- `WinExec`, `ShellExecuteA` — execution capability
- `HKEY_*` registry access
- `DdeConnect` / `DdeDisconnect` — DDE interprocess communication
- `WNetGetConnectionA` — network share enumeration
- `Dos/e1000odi.com` — DOS network driver (Intel e1000)

**Assessment:** Self-extracting archive almost certainly wrapping VNC or the keylogger installer. The VeriSign signing may be spoofed or from a legitimate vendor whose tool was repurposed.

---

### 3. VNC Remote Access Tool

| Field | Value |
|-------|-------|
| File | `vnc-4_1_3-x86_win32.exe` |
| MD5 | `790856e8ae34f0ac3eb40e031cf7a47a` |
| Version | VNC 4.1.3 (RealVNC) for Windows x86 |

Standard VNC installer. Presence alongside the keylogger and cover traffic tools indicates this was part of the toolkit for maintaining persistent access to the target machine.

---

### 4. Cover Traffic Tools

Both scripts authored by **"LCDR Kris Kearton"** (class: CS4920 ADOMEX, OS X 10.6, Python 2.6.2):

**`patentauto.py`** — Automates Firefox via MozRepl (TCP port 4242) to visit USPTO patent search URLs for terms from `patentterms.txt`. Runs on a schedule (10:00–12:00, 13:00–16:00) to mimic legitimate work activity.

**`webauto.py`** — Same mechanism but visits `urlspersona.txt` URLs (ESPN, Slashdot, Wikipedia, Sci-Fi, etc.) at business hours to simulate normal user browsing.

**Purpose:** Generate plausible, time-correct web browsing traffic to defeat network monitoring and build a fake user persona for an account being used for surveillance.

**`patentterms.txt` search seeds:** time, quantum, mortality, cryptography, machine, immortality, cryogenics — consistent with a target whose work involves cryptography/patents.

---

## IOC Summary

| Indicator | Type | Detail |
|-----------|------|--------|
| `C:\Program Files\XP Advanced\ToolKeylogger.exe` | Keylogger binary | XP Advanced Keylogger V2.1 |
| `55f9facaec8cf1d1bf1f8c04f3d287a4` | MD5 | R54402.EXE (SFX containing VNC/keylogger) |
| `790856e8ae34f0ac3eb40e031cf7a47a` | MD5 | vnc-4_1_3-x86_win32.exe |
| `\\192.168.1.1\m57` | Target network share | M57 company network, repeated credential attacks |
| `m57admin` / `admin01` | Stolen/guessed credentials | Used in repeated failed auth against M57 share |
| `\\.\PhysicalMemory` | Memory access attempt | Raw physical memory access on victim host |
| `LCDR Kris Kearton` | Author attribution | Cover traffic scripts (CS4920 ADOMEX) |

---

## Timeline of Activity (UTC)

| Timestamp | Event |
|-----------|-------|
| 2009-11-14 | `urlspersona.txt` created/modified |
| 2009-11-16–17 | Cover traffic URL files and Python scripts staged on USB |
| 2009-11-20 | `R54402.EXE` (installer) written to USB |
| 2009-12-03 10:19 | Keylogger captures clipboard (gov URLs) on Pat's machine |
| 2009-12-03 10:21 | Keylogger captures credential attempt; "drivepolicestealingsteal" typed |
| 2009-12-03 | Outlook email: "it is running quite a bit faster" (AV disabled?) |
| 2009-12-04 | Email to Terry asking about anti-virus |
| 2009-12-04 | 5+ failed login attempts: `m57admin/admin01` → `\\192.168.1.1\m57` |
| 2009-12-06 | `cmd` executed, memory access via `\\.\PhysicalMemory` attempted |
| 2009-12-06 | Continued credential attacks against M57 share |
| 2009-12-07 08:18 | Last screenshot recorded (final keylogger log entry) |
| 2009-12-07 | User reviews Dec 3 logs (`logs 20091203`) |
| 2011-01-19 17:09 | USB image acquired by examiner (F-Response) |

---

## Conclusions

1. **Terry's USB drive is an insider-threat toolkit.** It contains a commercial keylogger, VNC remote access software, a packaged installer, and browser automation tools designed to defeat traffic monitoring.

2. **The keylogger was installed on a machine used by "Pat"** and ran from 2009-12-03 through at least 2009-12-07, capturing 2,471 screenshots and 10 keystroke events including credential attempts.

3. **Active credential attacks were conducted** against the M57 internal network (`\\192.168.1.1\m57`, credentials `m57admin/admin01`), with multiple failed attempts per day logged.

4. **Physical memory access was attempted** on 2009-12-06 via `\\.\PhysicalMemory`, indicating either memory forensics capability or malware staging.

5. **Cover traffic tools were used to create a fake browsing persona**, masking surveillance activity behind normal-appearing web traffic at business-hour intervals.

6. **The author attribution** ("LCDR Kris Kearton", class CS4920 ADOMEX) in the Python scripts ties the cover traffic methodology to a specific operator and training context.

---

## Extracted Artifacts

| Path | Contents |
|------|----------|
| `exports/files/keylog-2009-12-0[3-7].htm` | Keylogger daily reports |
| `exports/files/patentauto.py` | Cover traffic script |
| `exports/files/webauto.py` | Cover traffic script |
| `exports/files/hashes.txt` | MD5 hashes of executables |
| `exports/fs_timeline.csv` | Full FAT32 MAC timeline |
| `analysis/bodyfile.txt` | Sleuth Kit bodyfile (5,091 entries) |
