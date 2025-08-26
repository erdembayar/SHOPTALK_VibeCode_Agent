# 🌐 Agentic Framework Web UI Usage Guide

## Overview

The Web UI provides a modern, browser-based interface for interacting with the multi-agent system. Built with Flask and WebSockets, it offers real-time communication and a responsive design that works on all devices.

## 🚀 **Getting Started**

### **Starting the Web Server**

#### Method 1: Direct Python Execution
```bash
python web_app.py
```

#### Method 2: Convenience Scripts
```bash
# Windows
web.bat

# Linux/Mac
./web.sh
```

### **Accessing the Interface**
Once the server starts, you'll see:
```
🌐 Starting Agentic Framework Web UI...
📍 Access the web interface at: http://localhost:5000
🔄 Real-time communication enabled with WebSockets
🤖 Multi-agent system ready!
```

Open your browser and navigate to:
- **Local access**: http://localhost:5000
- **Network access**: http://YOUR_IP:5000 (for other devices)

## 🎨 **Interface Features**

### **1. Modern Design Elements**

#### **Header Section**
- **Gradient Background**: Eye-catching blue gradient design
- **System Title**: "🤖 Agentic Framework"
- **Subtitle**: "Multi-Agent System with Intelligent Routing"

#### **Connection Status**
- **Top-right indicator**: Shows real-time connection status
- **Green**: 🟢 Connected - Ready to use
- **Red**: 🔴 Disconnected - Connection issues

#### **System Status Bar**
- **Active Agents Count**: Shows number of running agents
- **Conversation Counter**: Total queries processed
- **Refresh Button**: Update status manually
- **Clear Button**: Clear conversation history

### **2. Chat Interface**

#### **Message Types**
- **Your Messages**: Blue gradient background, right-aligned
- **Agent Responses**: White background with colored left borders:
  - 🟣 **Purple border**: Math Geek Agent
  - 🔵 **Blue border**: English Agent
  - 🟢 **Green border**: Spanish Agent
  - 🔴 **Red border**: Error messages

#### **Real-time Features**
- **Typing Indicator**: Shows when agents are processing
- **Timestamps**: All messages show exact time
- **Auto-scroll**: Automatically scrolls to newest messages
- **WebSocket Communication**: Instant responses without page refresh

### **3. Input Section**

#### **Quick Example Buttons**
Click any button to instantly try:
- 🔢 **"Calculate 25 + 17"** - Math calculation
- 🇺🇸 **"Hello, how are you?"** - English conversation
- 🇪🇸 **"¿Hola, cómo estás?"** - Spanish conversation
- 🔢 **"What is 5 factorial?"** - Math factorial

#### **Text Input**
- **Large input field**: Type up to 500 characters
- **Send button**: Click or press Enter to send
- **Input validation**: Prevents empty queries
- **Auto-focus**: Input field automatically focused

### **4. Agent Information Panel**

#### **Live Agent Cards**
- **Agent Icons**: Visual representation of each agent
- **Agent Names**: Clear identification
- **Descriptions**: What each agent does
- **Status Indicators**: Real-time active status

## 💬 **How to Use**

### **Basic Interaction Flow**

1. **Open Browser** → Navigate to http://localhost:5000
2. **Check Connection** → Green indicator in top-right
3. **Try Examples** → Click any quick example button
4. **Watch Response** → See agent respond in real-time
5. **Type Your Own** → Enter any query and press Enter

### **Example Interactions**

#### **Math Queries**
```
You: Calculate 45 + 67
🔢 Math Geek: The result of 45.0 + 67.0 is 112

You: What is 8 factorial?
🔢 Math Geek: The factorial of 8 is 40320
```

#### **English Conversations**
```
You: Hello, how are you today?
🇺🇸 English Agent: Hello! I'm the English Agent. How can I help you today?

You: What is artificial intelligence?
🇺🇸 English Agent: That's an interesting question about AI...
```

#### **Spanish Conversations**
```
You: Hola, ¿cómo estás?
🇪🇸 Spanish Agent: ¡Hola! Soy el Agente Español. ¿Cómo puedo ayudarte hoy?

You: ¿Qué tiempo hace?
🇪🇸 Spanish Agent: Es una pregunta sobre el tiempo...
```

## 🔧 **Advanced Features**

### **WebSocket Communication**
- **Real-time updates**: No page refreshing needed
- **Background processing**: Server processes queries asynchronously
- **Connection recovery**: Automatically reconnects if connection drops
- **Session management**: Each browser tab has its own session

### **Responsive Design**
- **Desktop**: Full-width layout with side panels
- **Tablet**: Stacked layout with collapsible sections
- **Mobile**: Single-column layout optimized for touch

### **Browser Compatibility**
- ✅ **Chrome/Chromium**: Full support
- ✅ **Firefox**: Full support
- ✅ **Safari**: Full support
- ✅ **Edge**: Full support
- ⚠️ **Internet Explorer**: Limited support (WebSocket issues)

## 🎛️ **Control Features**

### **System Management**
- **Refresh Status**: Update agent status and statistics
- **Clear History**: Remove all conversation messages
- **Connection Monitor**: Real-time connection status display

### **Session Features**
- **Multi-user Support**: Multiple browsers can connect simultaneously
- **Session Statistics**: Track queries per session
- **Conversation Persistence**: History maintained during session

## 📱 **Mobile Experience**

### **Touch-Optimized**
- **Large buttons**: Easy to tap on mobile devices
- **Responsive text**: Readable on small screens
- **Touch scrolling**: Smooth conversation scrolling
- **Mobile keyboard**: Optimized input experience

### **Offline Handling**
- **Connection loss detection**: Shows disconnected status
- **Retry mechanism**: Automatically attempts to reconnect
- **Error messages**: Clear feedback for connection issues

## 🔍 **API Endpoints**

The web app also provides REST API endpoints:

### **GET /api/status**
```json
{
  "success": true,
  "status": {
    "primary_agent": {...},
    "specialized_agents": [...],
    "conversation_count": 5
  }
}
```

### **GET /api/agents**
```json
{
  "success": true,
  "agents": [
    {
      "name": "Math Geek",
      "description": "Mathematical calculations..."
    }
  ]
}
```

### **POST /api/query**
```json
// Request
{
  "query": "Calculate 10 + 5"
}

// Response
{
  "success": true,
  "response": {
    "agent": "Math Geek",
    "result": "The result of 10.0 + 5.0 is 15"
  },
  "timestamp": "2025-08-26T10:30:25"
}
```

## 🛠️ **Technical Details**

### **Technology Stack**
- **Backend**: Flask + Flask-SocketIO
- **Frontend**: HTML5, CSS3, JavaScript
- **Communication**: WebSockets for real-time updates
- **Styling**: Bootstrap 5 + Custom CSS
- **Icons**: Font Awesome

### **Performance**
- **Lightweight**: Minimal resource usage
- **Fast**: Sub-second response times
- **Scalable**: Can handle multiple concurrent users
- **Efficient**: WebSocket reduces server load

## 🚨 **Troubleshooting**

### **Common Issues**

#### **Can't Access Web Interface**
- Ensure Flask server is running
- Check firewall settings
- Verify port 5000 is available
- Try http://127.0.0.1:5000 instead

#### **WebSocket Connection Failed**
- Refresh the page
- Check browser WebSocket support
- Disable browser extensions
- Try incognito/private mode

#### **Slow Responses**
- Check server terminal for errors
- Verify all agents are active
- Clear browser cache
- Restart the web server

### **Debug Mode**
The server runs in debug mode by default:
- **Auto-reload**: Server restarts on code changes
- **Error details**: Detailed error messages in terminal
- **Debug PIN**: Use debugger PIN if needed

## 💡 **Tips & Best Practices**

### **For Best Experience**
- **Use Chrome/Firefox**: Best WebSocket support
- **Keep tab active**: Some browsers throttle background tabs
- **Clear cache**: If you see old interface after updates
- **Check network**: Ensure stable internet connection

### **For Development**
- **Monitor terminal**: Watch for errors and debug info
- **Use browser dev tools**: Inspect WebSocket communication
- **Test mobile**: Use browser mobile simulation
- **Check console**: JavaScript errors appear in browser console

The Web UI provides the most modern and accessible way to interact with the agentic framework! 🌐✨
