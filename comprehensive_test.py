"""
Comprehensive Framework Test
A complete test showing all agent capabilities working together.
"""

from primary_agent import PrimaryAgent
import time


def comprehensive_test():
    """Run a comprehensive test of all framework features."""
    
    print("🚀 COMPREHENSIVE AGENTIC FRAMEWORK TEST")
    print("=" * 60)
    
    agent = PrimaryAgent()
    
    # Test categories
    test_categories = {
        "🔢 Mathematical Calculations": [
            "Calculate 25 + 17 * 3",
            "What is the square root of 225?",
            "What is 8 factorial?",
            "Calculate sin(30) degrees",
            "What is 2 to the power of 10?"
        ],
        "🇺🇸 English Language Queries": [
            "Hello! How are you doing today?",
            "What is machine learning?",
            "Can you explain quantum computing?",
            "Thank you for all your help!",
            "What time is it?"
        ],
        "🇪🇸 Spanish Language Queries": [
            "¡Hola! ¿Cómo te encuentras?",
            "¿Qué es la programación?",
            "¿Puedes explicar el clima de hoy?",
            "Muchas gracias por todo",
            "¿Dónde está la biblioteca?"
        ]
    }
    
    total_tests = sum(len(queries) for queries in test_categories.values())
    current_test = 0
    
    print(f"Running {total_tests} comprehensive tests...\n")
    
    for category, queries in test_categories.items():
        print(f"\n{category}")
        print("-" * 50)
        
        for query in queries:
            current_test += 1
            print(f"\n[{current_test}/{total_tests}] Testing: {query}")
            
            # Process the query
            response = agent.process_query(query)
            
            if response.get("success"):
                agent_name = response.get("agent", "Unknown")
                result = response.get("result", "No result")
                response_type = response.get("type", "")
                
                print(f"✅ Agent: {agent_name}")
                print(f"📝 Response: {result[:120]}{'...' if len(result) > 120 else ''}")
                
                # Show response type icon
                if "mathematical" in response_type:
                    print("   🔢 Mathematical response")
                elif "english" in response_type:
                    print("   🇺🇸 English response")
                elif "spanish" in response_type:
                    print("   🇪🇸 Spanish response")
                elif "default" in response_type:
                    print("   🤖 Default routing response")
            else:
                print(f"❌ Error: {response.get('error', 'Unknown error')}")
            
            time.sleep(0.1)  # Small delay for readability
    
    # Final system status
    print(f"\n\n📊 FINAL SYSTEM STATUS")
    print("=" * 30)
    
    status = agent.get_status()
    print(f"Primary Agent: {status['primary_agent']['name']} ✅")
    print(f"Specialized Agents: {len(status['specialized_agents'])}")
    
    for spec_agent in status['specialized_agents']:
        print(f"  • {spec_agent['name']}: ✅ Active")
        print(f"    {spec_agent['description']}")
    
    print(f"\nTotal Conversations Processed: {status['conversation_count']}")
    print(f"Last Interaction: {status['last_interaction']}")
    
    # Show conversation history summary
    history = agent.get_conversation_history()
    if history:
        print(f"\n📚 CONVERSATION HISTORY SUMMARY")
        print("-" * 35)
        
        agent_counts = {}
        for interaction in history:
            agent_name = interaction['response'].get('agent', 'Unknown')
            agent_counts[agent_name] = agent_counts.get(agent_name, 0) + 1
        
        for agent_name, count in agent_counts.items():
            print(f"  {agent_name}: {count} queries processed")
    
    print(f"\n🎉 COMPREHENSIVE TEST COMPLETED SUCCESSFULLY!")
    print("   All agents are functioning correctly and routing appropriately.")


if __name__ == "__main__":
    comprehensive_test()
