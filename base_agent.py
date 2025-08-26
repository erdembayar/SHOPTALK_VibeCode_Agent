"""
Base Agent Class
This module contains the base agent class that all specialized agents inherit from.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseAgent(ABC):
    """Abstract base class for all agents in the framework."""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    @abstractmethod
    def can_handle(self, query: str) -> bool:
        """
        Determine if this agent can handle the given query.
        
        Args:
            query (str): The user's input query
            
        Returns:
            bool: True if the agent can handle the query, False otherwise
        """
        pass
    
    @abstractmethod
    def process(self, query: str) -> Dict[str, Any]:
        """
        Process the query and return a response.
        
        Args:
            query (str): The user's input query
            
        Returns:
            Dict[str, Any]: Response containing the result and metadata
        """
        pass
    
    def get_info(self) -> Dict[str, str]:
        """Get agent information."""
        return {
            "name": self.name,
            "description": self.description
        }
