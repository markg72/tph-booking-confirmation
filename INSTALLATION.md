# Installation Guide

## Prerequisites

- **Python 3.8+** installed ([download here](https://www.python.org/downloads/))
- **Anthropic API account** with credits ([sign up here](https://console.anthropic.com/))

## Installation Steps

### 1. Install Python Dependencies

Open your terminal/command prompt and run:

```bash
pip install anthropic pdf2image pillow python-dotenv
```

This installs:
- `anthropic` - Claude API SDK
- `pdf2image` - PDF to image conversion
- `pillow` - Image processing
- `python-dotenv` - Environment variable management

### 2. Set Up Poppler (PDF Processing)

Poppler is required for pdf2image to convert PDF pages to images.

#### Windows

**Option A: Automated (Recommended)**

Poppler is already downloaded and configured! Just use the batch file:
```bash
run_transform.bat --input "your_file.pdf"
```

**Option B: Manual Installation**

1. Download poppler from [GitHub releases](https://github.com/oschwartz10612/poppler-windows/releases)
2. Extract to a folder (e.g., `C:\poppler`)
3. Add `C:\poppler\Library\bin` to your PATH environment variable

#### macOS

```bash
brew install poppler
```

#### Linux (Ubuntu/Debian)

```bash
sudo apt-get install poppler-utils
```

### 3. Configure Claude API Key

1. **Get your API key:**
   - Go to https://console.anthropic.com/
   - Sign in or create an account
   - Navigate to "API Keys" section
   - Create a new key or copy existing key

2. **Create .env file:**
   ```bash
   cp .env.example .env
   ```

3. **Add your API key to .env:**
   ```
   ANTHROPIC_API_KEY=sk-ant-api03-YOUR_KEY_HERE
   ```

### 4. Add Credits to Your Account

**IMPORTANT:** You need credits to use the Claude API.

1. Go to https://console.anthropic.com/settings/plans
2. Choose one of these options:
   - **Pay-as-you-go**: Add credits (minimum $5 = ~250 PDF transformations)
   - **Subscription plan**: Monthly credits included

**Cost per transformation:** ~$0.01-0.03 per PDF

## Verify Installation

### Test 1: Check Python Packages

```bash
python -c "import anthropic, pdf2image, PIL, dotenv; print('✓ All packages installed')"
```

### Test 2: Check Poppler

**Windows:**
```bash
run_transform.bat --help
```

**Mac/Linux:**
```bash
pdftoppm -v
```

### Test 3: Check API Key

```bash
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('✓ API key loaded' if os.getenv('ANTHROPIC_API_KEY') else '✗ API key not found')"
```

### Test 4: Transform a Sample PDF

**Windows:**
```bash
run_transform.bat --input ".reference/Before/2025.11.25 - The Planters House - Accommodation Confirmation.pdf" --debug
```

**Mac/Linux:**
```bash
python claude_transform.py --input ".reference/Before/2025.11.25 - The Planters House - Accommodation Confirmation.pdf" --debug
```

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'pdf2image'"

**Solution:** Install Python dependencies:
```bash
pip install anthropic pdf2image pillow python-dotenv
```

### Error: "Unable to get page count. Is poppler installed?"

**Solution:**

**Windows:** Use `run_transform.bat` instead of `python claude_transform.py`

**Mac/Linux:** Install poppler:
- macOS: `brew install poppler`
- Linux: `sudo apt-get install poppler-utils`

### Error: "ANTHROPIC_API_KEY not found"

**Solution:**
1. Verify `.env` file exists in project root
2. Check it contains: `ANTHROPIC_API_KEY=your_key_here`
3. Make sure there are no quotes around the key
4. Restart your terminal/command prompt

### Error: "Your credit balance is too low"

**Solution:**
1. Go to https://console.anthropic.com/settings/plans
2. Add credits or upgrade plan
3. Minimum $5 purchase = ~250 PDF transformations

### Error: "Bad Request" or API errors

**Solution:**
1. Verify API key is correct in `.env`
2. Check you have credits in your account
3. Ensure you're using the correct model (claude-sonnet-4-5-20250929)

## Platform-Specific Notes

### Windows

- Use `run_transform.bat` for automatic poppler PATH configuration
- If using PowerShell, you may need to enable script execution:
  ```powershell
  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
  ```

### macOS

- Homebrew is required for easy poppler installation
- If you don't have Homebrew, install from https://brew.sh/

### Linux

- Requires `poppler-utils` package
- On some distributions, package name may be `poppler-bin`

## Next Steps

Once installation is complete:

1. **Read [QUICK_START.md](QUICK_START.md)** for usage examples
2. **Check [README.md](README.md)** for feature overview
3. **Review [CLAUDE.md](CLAUDE.md)** for technical details

## Getting Help

- **Installation issues:** Check this guide's Troubleshooting section
- **Usage questions:** See [QUICK_START.md](QUICK_START.md)
- **API errors:** Visit https://console.anthropic.com/
- **Technical details:** Review [CLAUDE.md](CLAUDE.md)

---

**Ready to transform your first PDF?**

**Windows:**
```bash
run_transform.bat --input "your_cloudbeds.pdf"
```

**Mac/Linux:**
```bash
python claude_transform.py --input "your_cloudbeds.pdf"
```

From Cloudbeds → To Beautiful in 5 seconds! 🎉
