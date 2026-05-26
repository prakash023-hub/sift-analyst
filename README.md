# SIFT-Analyst 🔍
### Autonomous IR Agent for FIND EVIL! Hackathon (SANS Institute)

An autonomous incident response agent built on Protocol SIFT + Claude Code that finds evil in forensic disk images — without human intervention.

## What It Does
- Mounts E01 forensic disk images automatically
- Verifies image integrity (MD5)
- Enumerates all files and deleted artifacts
- Detects malicious tools (keyloggers, RATs, backdoors)
- Extracts IOCs, credentials, and timelines
- Self-corrects when tool errors occur
- Generates professional IR reports

## Demo Result
Against the M57 Patents forensic dataset, the agent autonomously discovered:
- XP Advanced Keylogger V2.1 with 5 days of logs
- 2,471 screenshots of victim activity
- Stolen credentials (m57admin/admin01)
- VNC remote access tool
- Cover traffic automation scripts
- Physical memory access attempt

## Architecture

