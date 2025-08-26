# 🖥️ Agentic Framework CLI Usage Guide

## Command Line Interface Examples

### 1. **Basic Queries**

#### Math Queries
```bash
# Windows
python cli.py "Calculate 25 + 17"
python cli.py "What is the square root of 144?"
python cli.py "What is 8 factorial?"
python cli.py "Solve 3 * 4 + 2"

# Using batch script (Windows)
.\agent.bat "Calculate 25 + 17"
.\agent.bat "What is 6 factorial?"
```

#### English Queries
```bash
python cli.py "Hello, how are you today?"
python cli.py "What is artificial intelligence?"
python cli.py "Can you help me with something?"
python cli.py "Thank you for your assistance!"
```

#### Spanish Queries
```bash
python cli.py "Hola, ¿cómo estás?"
python cli.py "¿Qué es la programación?"
python cli.py "Muchas gracias por la ayuda"
python cli.py "¿Puedes ayudarme?"
```

### 2. **Alternative Query Syntax**
```bash
# Using --query flag
python cli.py --query "Calculate 15 + 25"
python cli.py -q "Hello there!"
```

### 3. **System Information Commands**
```bash
# Show system status
python cli.py --status
python cli.py -s

# List available agents
python cli.py --agents
python cli.py -a

# Show version
python cli.py --version
python cli.py -v
```

### 4. **Output Format Options**

#### JSON Output
```bash
python cli.py --json "Calculate 10 + 5"
# Output: {"agent": "Math Geek", "success": true, "result": "...", ...}
```

#### Quiet Mode (Results Only)
```bash
python cli.py --quiet "What is 6 factorial?"
# Output: The factorial of 6 is 720

python cli.py --quiet "Hello!"
# Output: Hello! I'm the English Agent. How can I help you today?
```

### 5. **Batch Script Usage (Windows)**
```cmd
# Make sure you're in the project directory
cd c:\Users\eryondon\source\repos\SHOPTALK

# Basic usage
.\agent.bat "Calculate 20 + 15"
.\agent.bat "Hello world!"
.\agent.bat "Hola mundo!"

# With flags
.\agent.bat --status
.\agent.bat --agents
.\agent.bat --quiet "What is 7 factorial?"
```

### 6. **Shell Script Usage (Linux/Mac)**
```bash
# Make executable first
chmod +x agent.sh

# Basic usage
./agent.sh "Calculate 20 + 15"
./agent.sh "Hello world!"
./agent.sh "Hola mundo!"

# With flags
./agent.sh --status
./agent.sh --agents
./agent.sh --quiet "What is 7 factorial?"
```

### 7. **Error Handling**
```bash
# Empty query
python cli.py
# Output: Error: No query provided

# Invalid or unrecognizable query
python cli.py --quiet "xyz123 gibberish"
# Routes to Primary Agent with explanation
```

### 8. **Combining with Other Tools**

#### Pipe to file
```bash
python cli.py --json "Calculate 15 + 25" > result.json
```

#### Use in scripts
```bash
#!/bin/bash
RESULT=$(python cli.py --quiet "Calculate 10 + 5")
echo "The calculation result is: $RESULT"
```

#### Batch processing
```bash
# Process multiple queries
python cli.py "Calculate 5 + 5"
python cli.py "What is 3 factorial?"
python cli.py "Hello there!"
```

## 🎯 **Quick Reference**

| Command | Description | Example |
|---------|-------------|---------|
| `python cli.py "query"` | Process a query | `python cli.py "Calculate 2+2"` |
| `--query`, `-q` | Alternative query syntax | `python cli.py -q "Hello"` |
| `--status`, `-s` | Show system status | `python cli.py --status` |
| `--agents`, `-a` | List available agents | `python cli.py --agents` |
| `--version`, `-v` | Show version info | `python cli.py --version` |
| `--json` | JSON output format | `python cli.py --json "Hi"` |
| `--quiet` | Results only | `python cli.py --quiet "2+2"` |
| `.\agent.bat` | Windows convenience script | `.\agent.bat "Hello"` |
| `./agent.sh` | Linux/Mac convenience script | `./agent.sh "Hello"` |

## 🚀 **Getting Started**

1. **Navigate to project directory:**
   ```bash
   cd c:\Users\eryondon\source\repos\SHOPTALK
   ```

2. **Try a simple query:**
   ```bash
   python cli.py "Hello, how are you?"
   ```

3. **Check available agents:**
   ```bash
   python cli.py --agents
   ```

4. **Test with different query types:**
   ```bash
   python cli.py "Calculate 15 + 25"    # Math
   python cli.py "What's the weather?"   # English
   python cli.py "¿Cómo estás?"         # Spanish
   ```
