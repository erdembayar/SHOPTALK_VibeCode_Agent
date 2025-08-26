"""
Primary Agent
The main agent that interfaces with users and routes requests to specialized agents.
"""

from typing import List, Dict, Any, Optional
from base_agent import BaseAgent
from math_agent import MathGeekAgent
from english_agent import EnglishAgent
from spanish_agent import SpanishAgent


class PrimaryAgent:
    """
    Primary agent that routes user queries to appropriate specialized agents.
    Acts as the main interface between users and the agent system.
    """
    
    def __init__(self):
        self.name = "Primary Agent"
        self.description = "Main routing agent that directs queries to specialized agents"
        
        # Initialize specialized agents
        self.agents: List[BaseAgent] = [
            MathGeekAgent(),
            SpanishAgent(),  # Spanish before English to catch Spanish first
            EnglishAgent(),
        ]
        
        # Track conversation history
        self.conversation_history: List[Dict[str, Any]] = []
    
    def process_query(self, query: str) -> Dict[str, Any]:
        """
        Process a user query by routing it to the appropriate specialized agent.
        
        Args:
            query (str): The user's input query
            
        Returns:
            Dict[str, Any]: Response from the appropriate agent or error message
        """
        if not query or not query.strip():
            return {
                "agent": self.name,
                "success": False,
                "error": "Empty query provided",
                "query": query
            }
        
        # Find the appropriate agent
        suitable_agent = self._find_suitable_agent(query)
        
        if suitable_agent:
            # Process with the found agent
            response = suitable_agent.process(query)
        else:
            # No suitable agent found, provide default response
            response = self._generate_default_response(query)
        
        # Add to conversation history
        self.conversation_history.append({
            "query": query,
            "response": response,
            "timestamp": self._get_timestamp()
        })
        
        return response
    
    def _find_suitable_agent(self, query: str) -> Optional[BaseAgent]:
        """
        Find the most suitable agent for the given query.
        
        Args:
            query (str): The user's input query
            
        Returns:
            Optional[BaseAgent]: The most suitable agent or None if no agent can handle it
        """
        # Check each agent in order of priority
        for agent in self.agents:
            if agent.can_handle(query):
                return agent
        
        return None
    
    def _generate_default_response(self, query: str) -> Dict[str, Any]:
        """
        Generate a default response when no specialized agent can handle the query.
        
        Args:
            query (str): The user's input query
            
        Returns:
            Dict[str, Any]: Default response
        """
        return {
            "agent": self.name,
            "success": True,
            "result": f"I received your query: '{query}', but I'm not sure which specialized agent should handle it. "
                     f"I have the following agents available:\n"
                     f"• Math Geek: For mathematical calculations and problems\n"
                     f"• English Agent: For general queries in English\n"
                     f"• Spanish Agent: For queries in Spanish\n\n"
                     f"Could you rephrase your query or specify what type of help you need?",
            "query": query,
            "type": "default_response",
            "available_agents": [agent.get_info() for agent in self.agents]
        }
    
    def get_agent_info(self) -> List[Dict[str, str]]:
        """Get information about all available agents."""
        return [agent.get_info() for agent in self.agents]
    
    def get_conversation_history(self) -> List[Dict[str, Any]]:
        """Get the conversation history."""
        return self.conversation_history.copy()
    
    def clear_history(self) -> None:
        """Clear the conversation history."""
        self.conversation_history.clear()
    
    def _get_timestamp(self) -> str:
        """Get current timestamp for logging."""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def get_status(self) -> Dict[str, Any]:
        """Get the current status of the primary agent and all specialized agents."""
        return {
            "primary_agent": {
                "name": self.name,
                "description": self.description,
                "active": True
            },
            "specialized_agents": [
                {
                    "name": agent.name,
                    "description": agent.description,
                    "active": True
                }
                for agent in self.agents
            ],
            "conversation_count": len(self.conversation_history),
            "last_interaction": self.conversation_history[-1]["timestamp"] if self.conversation_history else "None"
        }
