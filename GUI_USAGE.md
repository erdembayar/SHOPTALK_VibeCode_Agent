# 🖥️ Agentic Framework GUI Usage Guide

## Overview

The GUI provides a user-friendly graphical interface for interacting with the multi-agent system. It features a modern design with real-time responses, conversation history, and visual status indicators.

## 🚀 **Starting the GUI**

### Method 1: Direct Python Execution
```bash
python gui.py
```

### Method 2: Convenience Scripts
```bash
# Windows
gui.bat

# Linux/Mac  
./gui.sh
```

## 🎨 **GUI Features**

### **1. Main Interface Components**

#### **Header Section**
- **Title**: "🤖 Agentic Framework"
- **System Status**: Shows active agents and conversation count
- **Refresh Button**: Updates status display

#### **Input Area**
- **Query Field**: Large text input for your questions
- **Send Button**: Submit your query (or press Enter)
- **Quick Examples**: One-click buttons for sample queries
  - 🔢 Calculate 25 + 17 (Math)
  - 🇺🇸 Hello, how are you? (English)
  - 🇪🇸 ¿Hola, cómo estás? (Spanish)
  - 🔢 What is 5 factorial? (Math)

#### **Conversation Area**
- **Scrollable History**: All conversations with timestamps
- **Color-coded Responses**: 
  - 🔵 Blue: Your queries
  - 🟢 Green: General agent responses
  - 🟣 Purple: Math agent responses
  - 🔵 Dark Blue: English agent responses
  - 🟢 Dark Green: Spanish agent responses
  - 🔴 Red: Error messages
  - ⚫ Gray: Timestamps

#### **Control Panel**
- **Clear History**: Remove all conversations
- **Show Status**: Detailed system information popup
- **About**: Information about the framework
- **Available Agents**: Quick reference of active agents

### **2. How to Use**

#### **Basic Query Process**
1. **Type your query** in the input field
2. **Press Enter** or click "Send 📤"
3. **Watch the response** appear in the conversation area
4. **See which agent** handled your query with colored responses

#### **Example Interactions**

**Math Queries:**
```
You: Calculate 45 + 67
🔢 Math Geek: The result of 45.0 + 67.0 is 112

You: What is 8 factorial?
🔢 Math Geek: The factorial of 8 is 40320
```

**English Conversations:**
```
You: Hello, how are you today?
🇺🇸 English Agent: Hello! I'm the English Agent. How can I help you today?

You: What is artificial intelligence?
🇺🇸 English Agent: That's an interesting 'what' question about AI...
```

**Spanish Conversations:**
```
You: Hola, ¿cómo estás?
🇪🇸 Spanish Agent: ¡Hola! Soy el Agente Español. ¿Cómo puedo ayudarte hoy?

You: ¿Qué tiempo hace?
🇪🇸 Spanish Agent: Es una pregunta interesante sobre el tiempo...
```

### **3. Advanced Features**

#### **System Status Window**
Click "📊 Show Status" to see:
- Primary agent status
- All specialized agents with descriptions
- Conversation statistics
- Last interaction time

#### **Conversation Management**
- **Auto-scroll**: Automatically scrolls to newest messages
- **Timestamps**: Every message shows the time sent
- **Clear History**: Remove all conversations and reset counters
- **Threading**: Responses processed in background (no UI freezing)

#### **Error Handling**
- **Empty Queries**: Warning dialog for empty inputs
- **Processing Errors**: Red error messages in conversation
- **Status Updates**: Real-time status of processing

#### **Keyboard Shortcuts**
- **Enter**: Send query (anywhere in the window)
- **Tab**: Navigate between input elements

### **4. Visual Indicators**

#### **Agent Icons**
- 🔢 Math Geek Agent
- 🇺🇸 English Agent  
- 🇪🇸 Spanish Agent
- 🤖 Primary Agent (fallback)

#### **Button States**
- **Normal**: "Send 📤" - Ready to send
- **Processing**: "Processing..." - Query being handled
- **Disabled**: Grayed out during processing

#### **Status Colors**
- ✅ Green checkmarks: Active/successful
- 🔄 Blue arrows: Refresh/update actions
- ❌ Red X: Errors or problems

### **5. Technical Details**

#### **Threading**
- GUI remains responsive during query processing
- Background threads handle agent communication
- Queue-based message passing between threads

#### **Memory Management**
- Conversation history stored in memory
- Clear history to free up memory for long sessions
- Status updates refresh agent statistics

#### **Window Properties**
- **Resizable**: Minimum 800x600, expands as needed
- **Responsive**: All elements scale with window size
- **Modern UI**: Uses ttk widgets for native look

## 🎯 **Quick Start Guide**

1. **Launch**: Run `python gui.py` or use launcher scripts
2. **Try Examples**: Click any quick example button
3. **Watch Response**: See the agent respond with colored text
4. **Type Your Own**: Enter any math, English, or Spanish query
5. **Explore**: Use status, clear, and about buttons

## 🔧 **Troubleshooting**

### **GUI Won't Start**
- Ensure Python has tkinter: `python -m tkinter`
- Check all agent files are present
- Verify requirements are installed

### **No Responses**
- Check agent status with "📊 Show Status"
- Clear history and try again
- Restart the GUI application

### **Slow Responses**
- Normal for complex math calculations
- Processing indicator shows work in progress
- Wait for completion before sending new queries

## 💡 **Tips & Best Practices**

- **Use Examples**: Start with quick example buttons to learn
- **Clear Regularly**: Clear history for better performance in long sessions  
- **Check Status**: Use status window to verify all agents are active
- **Try Different Types**: Test math, English, and Spanish queries
- **Read Timestamps**: Check when responses were received
- **Resize Window**: Make it larger for better conversation viewing

The GUI provides the most user-friendly way to interact with the agentic framework! 🎉
