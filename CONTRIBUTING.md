# Contributing to OpenCV MNKY

First off, thanks for taking the time to contribute! 🎉👍

## How Can I Contribute?

### Reporting Bugs 🐛

Before creating bug reports, please check existing issues. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if possible**
- **Include your environment details:**
  - OS (Windows/macOS/Linux)
  - Python version
  - Package versions (`pip list`)

### Suggesting Features 💡

Feature suggestions are welcome! Please include:

- **Clear description of the feature**
- **Why this feature would be useful**
- **Examples of how it would work**

### Pull Requests 🔧

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

#### Pull Request Guidelines:

- Update the README.md with details of changes if needed
- Update the CHANGELOG.md
- Ensure your code follows Python best practices (PEP 8)
- Test your changes thoroughly
- Comment your code when necessary

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small

## Development Setup

1. Clone your fork:
```bash
git clone https://github.com/YOUR_USERNAME/OpenCV_MNKY.git
cd OpenCV_MNKY
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Make your changes and test!

## Testing

Before submitting a PR, please test:

- [ ] Program starts without errors
- [ ] Camera detection works
- [ ] All gestures are detected correctly
- [ ] Keyboard controls work (ESC, F)
- [ ] No performance regression

## Questions?

Feel free to open an issue for any questions!

---

Thank you for contributing! 🐵✨
