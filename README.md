# Agentic Framework

A multi-agent system with a Primary Agent that routes user queries to specialized agents based on the input type.

## Architecture

The framework consists of:

1. **Primary Agent**: Main routing agent that interfaces with users and directs queries to appropriate specialized agents
2. **Math Geek Agent**: Handles mathematical calculations and problem solving
3. **English Agent**: Processes general queries in English language
4. **Spanish Agent**: Handles queries in Spanish language

## Features

- **Intelligent Routing**: Primary agent automatically detects query type and routes to appropriate specialist
- **Mathematical Processing**: Advanced math capabilities including arithmetic, algebra, trigonometry, and calculus
- **Multi-language Support**: Native support for English and Spanish languages
- **Language Detection**: Automatic language detection with fallback to pattern matching
- **Interactive Demo**: Full-featured demo with colored output and conversation history
- **Test Suite**: Automated testing to validate agent routing and functionality

## Installation

1. Clone or download the project files
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Web User Interface (Web UI)

The framework includes a modern web-based interface with real-time communication:

#### Starting the Web UI
```bash
# Direct Python execution
python web_app.py

# Using convenience scripts
# Windows:
web.bat

# Linux/Mac:
./web.sh
```

#### Web UI Features
- **Modern Responsive Design**: Works on desktop, tablet, and mobile
- **Real-time Communication**: WebSocket-powered instant responses
- **Visual Chat Interface**: WhatsApp-style conversation view
- **Color-coded Agents**: Different colors for each agent type
- **Live System Status**: Real-time agent status and statistics
- **Quick Examples**: One-click example queries
- **Browser-based**: No installation needed, works in any modern browser

#### Accessing the Web Interface
Once started, access the web UI at:
- **Local**: http://localhost:5000
- **Network**: http://YOUR_IP:5000 (accessible from other devices)

### Graphical User Interface (GUI)

The framework includes a modern GUI for easy visual interaction:

#### Starting the GUI
```bash
# Direct Python execution
python gui.py

# Using convenience scripts
# Windows:
gui.bat

# Linux/Mac:
./gui.sh
```

#### GUI Features
- **Visual Query Input**: Easy-to-use text field with example buttons
- **Real-time Responses**: Agents respond in a threaded conversation view
- **Color-coded Responses**: Different colors for different agent types
- **System Status**: Live status of all agents and conversation count
- **Conversation History**: Scrollable history with timestamps
- **Quick Examples**: One-click example queries for each agent type
- **Error Handling**: Clear error messages and status updates

### Command Line Interface (CLI)

The framework includes a powerful CLI for easy command-line usage:

#### Basic Usage
```bash
# Direct query
python cli.py "Calculate 25 + 17"
python cli.py "Hello, how are you?"
python cli.py "Hola, ¿cómo estás?"

# Using query flag
python cli.py --query "What is 5 factorial?"
python cli.py -q "What is the square root of 144?"
```

#### CLI Options
```bash
# System information
python cli.py --status          # Show system status
python cli.py --agents          # List available agents  
python cli.py --version         # Show version info

# Output formats
python cli.py --json "Calculate 10 + 5"     # JSON output
python cli.py --quiet "What is 6 factorial?" # Only result
```

#### Convenience Scripts
For easier usage, use the provided batch/shell scripts:

**Windows:**
```cmd
agent.bat "Calculate 15 + 25"
agent.bat --status
```

**Linux/Mac:**
```bash
./agent.sh "Calculate 15 + 25"
./agent.sh --status
```

### Interactive Demo

Run the interactive demo to chat with the agents:

```bash
python demo.py
```

Available commands in the demo:
- `/help` - Show help message and available agents
- `/status` - Display system status
- `/history` - Show conversation history
- `/clear` - Clear conversation history  
- `/quit` - Exit the demo

### Automated Test Suite

Run the test suite to see automated demonstrations:

```bash
python demo.py --test
```

### Programmatic Usage

```python
from primary_agent import PrimaryAgent

# Initialize the primary agent
agent = PrimaryAgent()

# Process queries
response = agent.process_query("Calculate 2 + 2")
print(response['result'])

response = agent.process_query("Hello, how are you?")
print(response['result'])

response = agent.process_query("Hola, ¿cómo estás?")
print(response['result'])
```

## Agent Capabilities

### Math Geek Agent
- Basic arithmetic operations
- Algebraic expressions
- Trigonometric functions (sin, cos, tan)
- Square roots and powers
- Factorial calculations
- Advanced math using SymPy (when available)

### English Agent
- General conversation in English
- Question answering
- Information requests
- Greetings and social interaction

### Spanish Agent
- General conversation in Spanish
- Question answering in Spanish
- Information requests in Spanish
- Greetings and social interaction

## Example Interactions

```
You: Calculate the square root of 144
[Math Geek] The square root of 144.0 is 12.000000

You: Hello, how are you today?
[English Agent] Hello! I'm the English Agent. How can I help you today?

You: Hola, ¿cómo estás?
[Spanish Agent] ¡Hola! Soy el Agente Español. ¿Cómo puedo ayudarte hoy?

You: What is 5 factorial?
[Math Geek] The factorial of 5 is 120
```

## Project Structure

```
SHOPTALK/
├── 🤖 Core Agents
│   ├── base_agent.py          # Abstract base class
│   ├── primary_agent.py       # Main routing agent
│   ├── math_agent.py          # Math calculations (FIXED!)
│   ├── english_agent.py       # English language
│   └── spanish_agent.py       # Spanish language
│
├── 🖥️ User Interfaces  
│   ├── web_app.py             # Flask web application
│   ├── templates/
│   │   └── index.html         # Web UI template
│   ├── gui.py                 # Graphical interface
│   ├── cli.py                 # Command line interface
│   └── demo.py                # Interactive demo
│
├── 🚀 Launchers & Scripts
│   ├── web.bat/.sh            # Web UI launchers
│   ├── gui.bat/.sh            # GUI launchers
│   ├── agent.bat/.sh          # CLI launchers
│   ├── quick_demo.py          # Quick demonstration
│   ├── simple_example.py      # Usage examples
│   └── comprehensive_test.py  # Full testing
│
├── 📚 Documentation
│   ├── README.md              # Main documentation
│   ├── CLI_USAGE.md           # CLI usage guide
│   ├── GUI_USAGE.md           # GUI usage guide
│   └── requirements.txt       # Dependencies
│
└── ⚙️ Configuration
    ├── .gitignore             # Git ignore rules
    └── .git/                  # Git repository
```

## Dependencies

- `langdetect==1.0.9` - Language detection (optional, fallback available)
- `sympy==1.12` - Advanced mathematical operations (optional)
- `numpy==1.24.3` - Numerical computations (used by sympy)
- `colorama==0.4.6` - Colored terminal output for demo

## Extending the Framework

To add a new specialized agent:

1. Create a new agent class inheriting from `BaseAgent`
2. Implement the `can_handle()` and `process()` methods
3. Add the agent to the `agents` list in `PrimaryAgent.__init__()`

Example:

```python
from base_agent import BaseAgent

class NewAgent(BaseAgent):
    def __init__(self):
        super().__init__("New Agent", "Description of what this agent does")
    
    def can_handle(self, query: str) -> bool:
        # Logic to determine if this agent should handle the query
        return "keyword" in query.lower()
    
    def process(self, query: str) -> Dict[str, Any]:
        # Process the query and return response
        return {
            "agent": self.name,
            "success": True,
            "result": "Response from new agent",
            "query": query,
            "type": "new_agent_response"
        }
```

## License

This project is open source and available under the MIT License.
