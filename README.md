# ASL Solo Bot Assistant

A Python-based solo opponent and assistant for **Advanced Squad Leader Starter Kit (ASLSK)**. This tool is designed to support solo play using logic inspired by the community "Play Both Sides" (PBS) rules, with long-term goals including AI decision-making, scenario tracking, and VASL save file parsing.

---

## 🔧 Project Goals

- Assist players in solo play of ASLSK scenarios
- Provide decision support for movement, firing, and morale-based actions
- Track game state, phases, units, and hex positions
- Simulate a bot opponent using tactical logic
- Optional GUI to visualize turns, logs, and decisions

---

## ✅ Current Features

- Virtual environment setup
- GitHub integration
- Placeholder classes: `Unit`, `Hex`, `GameState`
- Ready for iterative logic and AI development

---

## 🚧 Roadmap

- [ ] Model core ASLSK unit attributes and behavior
- [ ] Add phase/turn tracking system
- [ ] Implement PBS-style decision trees
- [ ] Parse `.vsav` (VASL save) files into internal game state
- [ ] GUI prototype using `tkinter` or `PyQt`
- [ ] Scenario loader / custom setup importer

---

## 🧠 Tech Stack

- **Language:** Python 3.10+
- **Environment:** VSCode + virtualenv
- **GitHub CLI:** for repo management and sync
- **(Future)**: `tkinter`, `shapely`, `xml.etree`, `pandas`

---

## 🤝 Contributions

This project may become open source in the future. For now, it is under solo development by [Zach Phillips](https://github.com/zach-phillips1).

---

## 📌 Notes

- This tool is focused on ASLSK, not full ASL.
- Designed for use with physical boards or VASL play, not as a replacement for VASL.

