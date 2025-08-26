"""
GUI Interface for Agentic Framework
A user-friendly graphical interface for interacting with the multi-agent system.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import queue
from datetime import datetime
from primary_agent import PrimaryAgent


class AgenticFrameworkGUI:
    """GUI application for the agentic framework."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 Agentic Framework - Multi-Agent System")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)
        
        # Initialize the primary agent
        self.agent = PrimaryAgent()
        
        # Queue for thread communication
        self.response_queue = queue.Queue()
        
        # Create the GUI
        self.create_widgets()
        
        # Start checking for responses
        self.check_response_queue()
        
        # Bind Enter key to send message
        self.root.bind('<Return>', lambda event: self.send_query())
    
    def create_widgets(self):
        """Create and arrange all GUI widgets."""
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for resizing
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Title and status area
        self.create_header(main_frame)
        
        # Input area
        self.create_input_area(main_frame)
        
        # Chat/conversation area
        self.create_conversation_area(main_frame)
        
        # Control buttons and agent info
        self.create_control_area(main_frame)
    
    def create_header(self, parent):
        """Create the header with title and status."""
        
        # Title
        title_label = ttk.Label(
            parent, 
            text="🤖 Agentic Framework", 
            font=("Arial", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))
        
        # Status frame
        status_frame = ttk.LabelFrame(parent, text="System Status", padding="5")
        status_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        status_frame.columnconfigure(1, weight=1)
        
        # Agent status indicators
        ttk.Label(status_frame, text="Active Agents:").grid(row=0, column=0, sticky=tk.W)
        
        self.status_text = tk.StringVar()
        self.update_status()
        status_label = ttk.Label(status_frame, textvariable=self.status_text)
        status_label.grid(row=0, column=1, sticky=tk.W, padx=(10, 0))
        
        # Refresh status button
        ttk.Button(
            status_frame, 
            text="🔄 Refresh", 
            command=self.update_status,
            width=10
        ).grid(row=0, column=2, padx=(10, 0))
    
    def create_input_area(self, parent):
        """Create the input area for queries."""
        
        input_frame = ttk.LabelFrame(parent, text="Enter Your Query", padding="5")
        input_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        input_frame.columnconfigure(0, weight=1)
        
        # Input text field
        self.query_var = tk.StringVar()
        self.query_entry = ttk.Entry(
            input_frame, 
            textvariable=self.query_var,
            font=("Arial", 11),
            width=60
        )
        self.query_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        
        # Send button
        self.send_button = ttk.Button(
            input_frame, 
            text="Send 📤", 
            command=self.send_query,
            width=12
        )
        self.send_button.grid(row=0, column=1)
        
        # Example queries
        examples_frame = ttk.Frame(input_frame)
        examples_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(5, 0))
        
        ttk.Label(examples_frame, text="Quick Examples:", font=("Arial", 9)).grid(row=0, column=0, sticky=tk.W)
        
        example_buttons_frame = ttk.Frame(examples_frame)
        example_buttons_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(2, 0))
        
        examples = [
            ("Calculate 25 + 17", "🔢"),
            ("Hello, how are you?", "🇺🇸"),
            ("¿Hola, cómo estás?", "🇪🇸"),
            ("What is 5 factorial?", "🔢")
        ]
        
        for i, (example, icon) in enumerate(examples):
            btn = ttk.Button(
                example_buttons_frame,
                text=f"{icon} {example}",
                command=lambda ex=example: self.set_example_query(ex),
                width=20
            )
            btn.grid(row=0, column=i, padx=(0, 5))
    
    def create_conversation_area(self, parent):
        """Create the conversation display area."""
        
        conv_frame = ttk.LabelFrame(parent, text="Conversation History", padding="5")
        conv_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        conv_frame.columnconfigure(0, weight=1)
        conv_frame.rowconfigure(0, weight=1)
        
        # Scrolled text widget for conversation
        self.conversation_text = scrolledtext.ScrolledText(
            conv_frame,
            wrap=tk.WORD,
            width=80,
            height=20,
            font=("Consolas", 10),
            state=tk.DISABLED
        )
        self.conversation_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure text tags for styling
        self.conversation_text.tag_configure("user", foreground="blue", font=("Consolas", 10, "bold"))
        self.conversation_text.tag_configure("agent", foreground="green", font=("Consolas", 10, "bold"))
        self.conversation_text.tag_configure("error", foreground="red")
        self.conversation_text.tag_configure("timestamp", foreground="gray", font=("Consolas", 8))
        self.conversation_text.tag_configure("math", foreground="purple")
        self.conversation_text.tag_configure("english", foreground="darkblue")
        self.conversation_text.tag_configure("spanish", foreground="darkgreen")
        
        # Welcome message
        self.add_to_conversation(
            "Welcome to the Agentic Framework! 🤖\n"
            "You can ask math questions, chat in English, or hablar en español.\n"
            "Type your query above and press Enter or click Send.\n",
            "agent"
        )
    
    def create_control_area(self, parent):
        """Create the control buttons and agent information."""
        
        control_frame = ttk.Frame(parent)
        control_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E))
        control_frame.columnconfigure(1, weight=1)
        
        # Left side - control buttons
        buttons_frame = ttk.Frame(control_frame)
        buttons_frame.grid(row=0, column=0, sticky=tk.W)
        
        ttk.Button(
            buttons_frame, 
            text="🗑️ Clear History", 
            command=self.clear_conversation,
            width=15
        ).grid(row=0, column=0, padx=(0, 5))
        
        ttk.Button(
            buttons_frame, 
            text="📊 Show Status", 
            command=self.show_detailed_status,
            width=15
        ).grid(row=0, column=1, padx=(0, 5))
        
        ttk.Button(
            buttons_frame, 
            text="ℹ️ About", 
            command=self.show_about,
            width=15
        ).grid(row=0, column=2)
        
        # Right side - agent info
        agent_info_frame = ttk.LabelFrame(control_frame, text="Available Agents", padding="5")
        agent_info_frame.grid(row=0, column=2, sticky=(tk.E), padx=(20, 0))
        
        agents = self.agent.get_agent_info()
        for i, agent_info in enumerate(agents):
            icon = "🔢" if "Math" in agent_info['name'] else "🇪🇸" if "Spanish" in agent_info['name'] else "🇺🇸"
            agent_label = ttk.Label(
                agent_info_frame, 
                text=f"{icon} {agent_info['name']}"
            )
            agent_label.grid(row=i, column=0, sticky=tk.W)
    
    def set_example_query(self, example):
        """Set an example query in the input field."""
        self.query_var.set(example)
        self.query_entry.focus()
    
    def update_status(self):
        """Update the status display."""
        status = self.agent.get_status()
        agent_count = len(status['specialized_agents'])
        conv_count = status['conversation_count']
        self.status_text.set(f"{agent_count} agents active • {conv_count} conversations processed")
    
    def send_query(self):
        """Send the query to the agent system."""
        query = self.query_var.get().strip()
        
        if not query:
            messagebox.showwarning("Empty Query", "Please enter a query before sending.")
            return
        
        # Disable send button and show processing
        self.send_button.config(state="disabled", text="Processing...")
        self.query_entry.config(state="disabled")
        
        # Add user query to conversation
        self.add_to_conversation(f"You: {query}", "user")
        
        # Clear input
        self.query_var.set("")
        
        # Process query in background thread
        threading.Thread(
            target=self.process_query_thread, 
            args=(query,), 
            daemon=True
        ).start()
    
    def process_query_thread(self, query):
        """Process the query in a background thread."""
        try:
            response = self.agent.process_query(query)
            self.response_queue.put(('success', query, response))
        except Exception as e:
            self.response_queue.put(('error', query, str(e)))
    
    def check_response_queue(self):
        """Check for responses from background threads."""
        try:
            while True:
                result_type, query, response = self.response_queue.get_nowait()
                
                if result_type == 'success':
                    self.handle_successful_response(response)
                else:
                    self.handle_error_response(response)
                
                # Re-enable controls
                self.send_button.config(state="normal", text="Send 📤")
                self.query_entry.config(state="normal")
                self.query_entry.focus()
                
                # Update status
                self.update_status()
                
        except queue.Empty:
            pass
        
        # Schedule next check
        self.root.after(100, self.check_response_queue)
    
    def handle_successful_response(self, response):
        """Handle a successful response from an agent."""
        agent_name = response.get("agent", "Unknown Agent")
        result = response.get("result", "No result")
        response_type = response.get("type", "")
        
        # Determine agent tag for styling
        agent_tag = "agent"
        if "mathematical" in response_type:
            agent_tag = "math"
        elif "english" in response_type:
            agent_tag = "english"
        elif "spanish" in response_type:
            agent_tag = "spanish"
        
        # Add response to conversation
        agent_icon = self.get_agent_icon(agent_name)
        self.add_to_conversation(f"{agent_icon} {agent_name}: {result}", agent_tag)
    
    def handle_error_response(self, error_msg):
        """Handle an error response."""
        self.add_to_conversation(f"❌ Error: {error_msg}", "error")
    
    def get_agent_icon(self, agent_name):
        """Get the appropriate icon for an agent."""
        if "Math" in agent_name:
            return "🔢"
        elif "Spanish" in agent_name:
            return "🇪🇸"
        elif "English" in agent_name:
            return "🇺🇸"
        else:
            return "🤖"
    
    def add_to_conversation(self, text, tag=""):
        """Add text to the conversation area."""
        self.conversation_text.config(state=tk.NORMAL)
        
        # Add timestamp
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.conversation_text.insert(tk.END, f"[{timestamp}] ", "timestamp")
        
        # Add main text
        self.conversation_text.insert(tk.END, text + "\n\n", tag)
        
        # Scroll to bottom
        self.conversation_text.see(tk.END)
        self.conversation_text.config(state=tk.DISABLED)
    
    def clear_conversation(self):
        """Clear the conversation history."""
        if messagebox.askyesno("Clear History", "Are you sure you want to clear the conversation history?"):
            self.conversation_text.config(state=tk.NORMAL)
            self.conversation_text.delete(1.0, tk.END)
            self.conversation_text.config(state=tk.DISABLED)
            
            # Clear agent history too
            self.agent.clear_history()
            
            # Add welcome message
            self.add_to_conversation(
                "Conversation history cleared. Ready for new queries! 🤖",
                "agent"
            )
            
            # Update status
            self.update_status()
    
    def show_detailed_status(self):
        """Show detailed system status in a popup."""
        status = self.agent.get_status()
        
        status_window = tk.Toplevel(self.root)
        status_window.title("System Status")
        status_window.geometry("400x300")
        status_window.resizable(False, False)
        
        # Center the window
        status_window.transient(self.root)
        status_window.grab_set()
        
        main_frame = ttk.Frame(status_window, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Status information
        ttk.Label(main_frame, text="🤖 System Status", font=("Arial", 14, "bold")).pack(pady=(0, 10))
        
        status_text = scrolledtext.ScrolledText(main_frame, width=45, height=15, wrap=tk.WORD)
        status_text.pack(fill=tk.BOTH, expand=True)
        
        # Primary agent info
        status_text.insert(tk.END, f"Primary Agent: {status['primary_agent']['name']}\n")
        status_text.insert(tk.END, f"Status: Active ✅\n\n")
        
        # Specialized agents
        status_text.insert(tk.END, f"Specialized Agents ({len(status['specialized_agents'])}):\n")
        for agent in status['specialized_agents']:
            icon = self.get_agent_icon(agent['name'])
            status_text.insert(tk.END, f"  {icon} {agent['name']}: Active ✅\n")
            status_text.insert(tk.END, f"     {agent['description']}\n\n")
        
        # Statistics
        status_text.insert(tk.END, f"Statistics:\n")
        status_text.insert(tk.END, f"  Total Conversations: {status['conversation_count']}\n")
        status_text.insert(tk.END, f"  Last Interaction: {status['last_interaction']}\n")
        
        status_text.config(state=tk.DISABLED)
        
        ttk.Button(main_frame, text="Close", command=status_window.destroy).pack(pady=(10, 0))
    
    def show_about(self):
        """Show about dialog."""
        about_text = """
🤖 Agentic Framework v1.0

A multi-agent system with intelligent routing:

• Primary Agent: Routes queries to specialists
• Math Geek: Mathematical calculations
• English Agent: English conversations  
• Spanish Agent: Spanish conversations

Features:
✓ Intelligent query routing
✓ Multi-language support
✓ Advanced mathematics
✓ Conversation history
✓ Multiple interfaces (GUI, CLI, Interactive)

Created with Python and tkinter
        """
        
        messagebox.showinfo("About Agentic Framework", about_text.strip())


def main():
    """Main function to run the GUI application."""
    root = tk.Tk()
    app = AgenticFrameworkGUI(root)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nGUI application terminated.")


if __name__ == "__main__":
    main()
