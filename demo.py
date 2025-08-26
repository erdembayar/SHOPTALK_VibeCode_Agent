"""
Agentic Framework Demo
Interactive demo of the multi-agent system with Primary Agent routing to specialized agents.
"""

import sys
from typing import Dict, Any
from colorama import init, Fore, Style, Back

# Initialize colorama for colored output
init(autoreset=True)

try:
    from primary_agent import PrimaryAgent
except ImportError as e:
    print(f"Error importing agents: {e}")
    print("Make sure all agent files are in the same directory.")
    sys.exit(1)


class AgenticFrameworkDemo:
    """Demo application for the agentic framework."""
    
    def __init__(self):
        self.primary_agent = PrimaryAgent()
        self.running = True
        
    def print_banner(self):
        """Print the demo banner."""
        banner = f"""
{Fore.CYAN}{Style.BRIGHT}╔══════════════════════════════════════════════════════════════╗
║                    AGENTIC FRAMEWORK DEMO                   ║
║                                                              ║
║  Primary Agent + Specialized Agents System                  ║
╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}

{Fore.YELLOW}Available Agents:{Style.RESET_ALL}
"""
        print(banner)
        
        # Display agent information
        for agent_info in self.primary_agent.get_agent_info():
            print(f"  {Fore.GREEN}•{Style.RESET_ALL} {Fore.BLUE}{agent_info['name']}{Style.RESET_ALL}: {agent_info['description']}")
        
        print(f"\n{Fore.MAGENTA}Commands:{Style.RESET_ALL}")
        print(f"  {Fore.GREEN}/help{Style.RESET_ALL}     - Show this help message")
        print(f"  {Fore.GREEN}/status{Style.RESET_ALL}   - Show system status")
        print(f"  {Fore.GREEN}/history{Style.RESET_ALL}  - Show conversation history")
        print(f"  {Fore.GREEN}/clear{Style.RESET_ALL}    - Clear conversation history")
        print(f"  {Fore.GREEN}/quit{Style.RESET_ALL}     - Exit the demo")
        print(f"\n{Fore.CYAN}Type your query and press Enter to interact with the agents!{Style.RESET_ALL}")
        print("=" * 60)
    
    def print_response(self, response: Dict[str, Any]):
        """Print agent response with formatting."""
        if response.get("success", False):
            agent_name = response.get("agent", "Unknown Agent")
            result = response.get("result", "No result")
            
            print(f"\n{Fore.BLUE}[{agent_name}]{Style.RESET_ALL} {result}")
            
            # Show additional info for certain response types
            response_type = response.get("type", "")
            if response_type == "mathematical_calculation":
                print(f"  {Fore.CYAN}📊 Mathematical calculation completed{Style.RESET_ALL}")
            elif response_type == "english_language_response":
                print(f"  {Fore.CYAN}🇺🇸 English language response{Style.RESET_ALL}")
            elif response_type == "spanish_language_response":
                print(f"  {Fore.CYAN}🇪🇸 Spanish language response{Style.RESET_ALL}")
        else:
            error = response.get("error", "Unknown error")
            agent_name = response.get("agent", "System")
            print(f"\n{Fore.RED}[{agent_name} Error]{Style.RESET_ALL} {error}")
    
    def handle_command(self, command: str) -> bool:
        """Handle system commands. Returns True if command was handled."""
        command = command.lower().strip()
        
        if command == "/help":
            self.print_banner()
            return True
            
        elif command == "/status":
            status = self.primary_agent.get_status()
            print(f"\n{Fore.CYAN}System Status:{Style.RESET_ALL}")
            print(f"  Primary Agent: {Fore.GREEN}Active{Style.RESET_ALL}")
            print(f"  Specialized Agents: {len(status['specialized_agents'])}")
            for agent in status['specialized_agents']:
                print(f"    • {agent['name']}: {Fore.GREEN}Active{Style.RESET_ALL}")
            print(f"  Conversations: {status['conversation_count']}")
            print(f"  Last Interaction: {status['last_interaction']}")
            return True
            
        elif command == "/history":
            history = self.primary_agent.get_conversation_history()
            if not history:
                print(f"\n{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
            else:
                print(f"\n{Fore.CYAN}Conversation History:{Style.RESET_ALL}")
                for i, interaction in enumerate(history[-5:], 1):  # Show last 5
                    query = interaction['query'][:50] + "..." if len(interaction['query']) > 50 else interaction['query']
                    agent = interaction['response'].get('agent', 'Unknown')
                    timestamp = interaction['timestamp']
                    print(f"  {i}. [{timestamp}] {Fore.YELLOW}{query}{Style.RESET_ALL} → {Fore.BLUE}{agent}{Style.RESET_ALL}")
            return True
            
        elif command == "/clear":
            self.primary_agent.clear_history()
            print(f"\n{Fore.GREEN}Conversation history cleared.{Style.RESET_ALL}")
            return True
            
        elif command == "/quit":
            print(f"\n{Fore.CYAN}Thanks for using the Agentic Framework Demo! Goodbye!{Style.RESET_ALL}")
            self.running = False
            return True
        
        return False
    
    def run_demo(self):
        """Run the interactive demo."""
        self.print_banner()
        
        while self.running:
            try:
                # Get user input
                user_input = input(f"\n{Fore.GREEN}You:{Style.RESET_ALL} ").strip()
                
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.startswith('/'):
                    self.handle_command(user_input)
                    continue
                
                # Process query through primary agent
                print(f"{Fore.YELLOW}Processing...{Style.RESET_ALL}", end="", flush=True)
                response = self.primary_agent.process_query(user_input)
                print(f"\r{' ' * 15}\r", end="")  # Clear "Processing..."
                
                # Display response
                self.print_response(response)
                
            except KeyboardInterrupt:
                print(f"\n\n{Fore.CYAN}Demo interrupted. Goodbye!{Style.RESET_ALL}")
                break
            except Exception as e:
                print(f"\n{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
    
    def run_test_suite(self):
        """Run automated tests to demonstrate functionality."""
        print(f"\n{Fore.CYAN}{Style.BRIGHT}Running Automated Test Suite{Style.RESET_ALL}")
        print("=" * 50)
        
        test_queries = [
            # Math tests
            ("Calculate 25 + 37", "Math Geek"),
            ("What is the square root of 144?", "Math Geek"),
            ("Solve 2 + 3 * 4", "Math Geek"),
            ("What is 5 factorial?", "Math Geek"),
            
            # English tests
            ("Hello, how are you today?", "English Agent"),
            ("What is the weather like?", "English Agent"),
            ("Can you help me understand this concept?", "English Agent"),
            ("Thank you for your assistance.", "English Agent"),
            
            # Spanish tests
            ("Hola, ¿cómo estás?", "Spanish Agent"),
            ("¿Qué es la inteligencia artificial?", "Spanish Agent"),
            ("Gracias por tu ayuda.", "Spanish Agent"),
            ("¿Dónde puedo encontrar información?", "Spanish Agent"),
            
            # Edge cases
            ("", "Primary Agent"),  # Empty query
            ("Random gibberish xyz123", "Primary Agent"),  # Unrecognizable
        ]
        
        for i, (query, expected_agent) in enumerate(test_queries, 1):
            print(f"\n{Fore.YELLOW}Test {i}: {query[:50]}{'...' if len(query) > 50 else ''}{Style.RESET_ALL}")
            
            if not query:
                print(f"  {Fore.CYAN}Testing empty query...{Style.RESET_ALL}")
            
            response = self.primary_agent.process_query(query)
            actual_agent = response.get("agent", "Unknown")
            
            if expected_agent in actual_agent or actual_agent in expected_agent:
                print(f"  {Fore.GREEN}✓ Routed to: {actual_agent}{Style.RESET_ALL}")
            else:
                print(f"  {Fore.YELLOW}⚠ Expected: {expected_agent}, Got: {actual_agent}{Style.RESET_ALL}")
            
            # Show brief response
            if response.get("success"):
                result = response.get("result", "")[:100]
                print(f"  {Fore.BLUE}Response: {result}{'...' if len(response.get('result', '')) > 100 else ''}{Style.RESET_ALL}")
            else:
                print(f"  {Fore.RED}Error: {response.get('error', 'Unknown error')}{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}Test suite completed!{Style.RESET_ALL}")


def main():
    """Main function to run the demo."""
    demo = AgenticFrameworkDemo()
    
    # Check if user wants to run tests or interactive demo
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        demo.run_test_suite()
    else:
        demo.run_demo()


if __name__ == "__main__":
    main()
