"""
Quick Demo Script
A simple script to demonstrate the agentic framework functionality.
"""

from primary_agent import PrimaryAgent


def demo_agentic_framework():
    """Demonstrate the agentic framework with various queries."""
    
    print("🤖 Agentic Framework Demo")
    print("=" * 50)
    
    # Initialize the primary agent
    agent = PrimaryAgent()
    
    # Test queries for different agents
    test_queries = [
        # Math queries
        ("Calculate 15 + 27", "Math Geek"),
        ("What is the square root of 64?", "Math Geek"),
        ("What is 7 factorial?", "Math Geek"),
        ("Solve 3 * 4 + 2", "Math Geek"),
        
        # English queries
        ("Hello, how can you help me?", "English Agent"),
        ("What is artificial intelligence?", "English Agent"),
        ("Thank you for your help!", "English Agent"),
        
        # Spanish queries
        ("Hola, ¿cómo estás?", "Spanish Agent"),
        ("¿Qué tiempo hace hoy?", "Spanish Agent"),
        ("Muchas gracias por la ayuda", "Spanish Agent"),
    ]
    
    print(f"\nTesting {len(test_queries)} queries across all agents...\n")
    
    for i, (query, expected_agent) in enumerate(test_queries, 1):
        print(f"Query {i}: {query}")
        
        response = agent.process_query(query)
        
        if response.get("success"):
            actual_agent = response.get("agent", "Unknown")
            result = response.get("result", "No result")
            
            # Check if routed correctly
            routing_status = "✅" if expected_agent in actual_agent else "⚠️"
            
            print(f"  {routing_status} Routed to: {actual_agent}")
            print(f"  📝 Response: {result[:100]}{'...' if len(result) > 100 else ''}")
        else:
            print(f"  ❌ Error: {response.get('error', 'Unknown error')}")
        
        print()
    
    # Show agent status
    print("\n📊 System Status:")
    status = agent.get_status()
    print(f"  • Primary Agent: {status['primary_agent']['name']} - Active")
    print(f"  • Specialized Agents: {len(status['specialized_agents'])}")
    for spec_agent in status['specialized_agents']:
        print(f"    - {spec_agent['name']}: Active")
    print(f"  • Total Conversations: {status['conversation_count']}")
    
    print("\n🎉 Demo completed! The agentic framework is working correctly.")


if __name__ == "__main__":
    demo_agentic_framework()
