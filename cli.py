"""
Command Line Interface for Agentic Framework
Simple CLI to interact with the agentic framework from terminal.
"""

import sys
import argparse
from primary_agent import PrimaryAgent


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Agentic Framework CLI - Route queries to specialized agents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py "Calculate 25 + 17"
  python cli.py "Hello, how are you?"
  python cli.py "¿Hola, cómo estás?"
  python cli.py --query "What is 5 factorial?"
  python cli.py --status
  python cli.py --agents
        """
    )
    
    # Main query argument
    parser.add_argument(
        'query', 
        nargs='?', 
        help='The query to process (can be math, English, or Spanish)'
    )
    
    # Alternative query flag
    parser.add_argument(
        '--query', '-q',
        dest='query_flag',
        help='Alternative way to specify the query'
    )
    
    # System information flags
    parser.add_argument(
        '--status', '-s',
        action='store_true',
        help='Show system status'
    )
    
    parser.add_argument(
        '--agents', '-a',
        action='store_true',
        help='List available agents'
    )
    
    parser.add_argument(
        '--version', '-v',
        action='store_true',
        help='Show version information'
    )
    
    # Output format options
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output response in JSON format'
    )
    
    parser.add_argument(
        '--quiet', '-quiet',
        action='store_true',
        help='Only show the result, no metadata'
    )
    
    args = parser.parse_args()
    
    # Initialize the primary agent
    agent = PrimaryAgent()
    
    # Handle version
    if args.version:
        print("Agentic Framework CLI v1.0")
        print("Multi-agent system with intelligent routing")
        return
    
    # Handle status
    if args.status:
        show_status(agent)
        return
    
    # Handle agents list
    if args.agents:
        show_agents(agent)
        return
    
    # Get the query from either positional argument or flag
    query = args.query or args.query_flag
    
    if not query:
        print("Error: No query provided")
        print("Use 'python cli.py --help' for usage information")
        sys.exit(1)
    
    # Process the query
    try:
        response = agent.process_query(query)
        
        if args.json:
            import json
            print(json.dumps(response, indent=2))
        elif args.quiet:
            if response.get("success"):
                print(response.get("result", "No result"))
            else:
                print(f"Error: {response.get('error', 'Unknown error')}")
        else:
            show_response(query, response)
            
    except Exception as e:
        if args.json:
            import json
            print(json.dumps({"success": False, "error": str(e)}, indent=2))
        else:
            print(f"Error processing query: {e}")
        sys.exit(1)


def show_status(agent):
    """Show system status."""
    status = agent.get_status()
    
    print("🤖 Agentic Framework Status")
    print("=" * 30)
    print(f"Primary Agent: {status['primary_agent']['name']} ✅")
    print(f"Specialized Agents: {len(status['specialized_agents'])}")
    
    for spec_agent in status['specialized_agents']:
        print(f"  • {spec_agent['name']}: Active")
    
    print(f"Total Conversations: {status['conversation_count']}")
    if status['last_interaction'] != "None":
        print(f"Last Interaction: {status['last_interaction']}")


def show_agents(agent):
    """Show available agents."""
    agents = agent.get_agent_info()
    
    print("🤖 Available Agents")
    print("=" * 20)
    
    for i, agent_info in enumerate(agents, 1):
        print(f"{i}. {agent_info['name']}")
        print(f"   Description: {agent_info['description']}")
        print()


def show_response(query, response):
    """Show formatted response."""
    print(f"Query: {query}")
    print("-" * (len(query) + 7))
    
    if response.get("success"):
        agent_name = response.get("agent", "Unknown Agent")
        result = response.get("result", "No result")
        response_type = response.get("type", "")
        
        print(f"Agent: {agent_name}")
        
        # Add type indicator
        if "mathematical" in response_type:
            print("Type: 🔢 Mathematical")
        elif "english" in response_type:
            print("Type: 🇺🇸 English")
        elif "spanish" in response_type:
            print("Type: 🇪🇸 Spanish")
        elif "default" in response_type:
            print("Type: 🤖 Default")
        
        print(f"\nResult:\n{result}")
    else:
        error = response.get("error", "Unknown error")
        print(f"❌ Error: {error}")


if __name__ == "__main__":
    main()
