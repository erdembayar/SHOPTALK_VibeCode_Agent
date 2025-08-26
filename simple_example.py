"""
Simple Usage Example
Shows how to use the agentic framework in your own code.
"""

from primary_agent import PrimaryAgent


def simple_example():
    """Simple example of using the agentic framework."""
    
    # Create the primary agent
    agent = PrimaryAgent()
    
    print("Simple Agentic Framework Usage Example")
    print("=" * 40)
    
    # Example 1: Math calculation
    print("\n1. Math Calculation:")
    response = agent.process_query("What is 12 * 8?")
    print(f"   Query: What is 12 * 8?")
    print(f"   Agent: {response['agent']}")
    print(f"   Result: {response['result']}")
    
    # Example 2: English conversation
    print("\n2. English Conversation:")
    response = agent.process_query("Hello! Can you help me?")
    print(f"   Query: Hello! Can you help me?")
    print(f"   Agent: {response['agent']}")
    print(f"   Result: {response['result'][:80]}...")
    
    # Example 3: Spanish conversation
    print("\n3. Spanish Conversation:")
    response = agent.process_query("¡Hola! ¿Puedes ayudarme?")
    print(f"   Query: ¡Hola! ¿Puedes ayudarme?")
    print(f"   Agent: {response['agent']}")
    print(f"   Result: {response['result'][:80]}...")
    
    # Show available agents
    print("\n4. Available Agents:")
    agents = agent.get_agent_info()
    for i, agent_info in enumerate(agents, 1):
        print(f"   {i}. {agent_info['name']}: {agent_info['description']}")


if __name__ == "__main__":
    simple_example()
