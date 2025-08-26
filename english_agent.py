"""
English Agent
Specialized agent for handling queries in English language.
"""

import re
from typing import Dict, Any
from base_agent import BaseAgent

try:
    from langdetect import detect
    LANGDETECT_AVAILABLE = True
except ImportError:
    LANGDETECT_AVAILABLE = False


class EnglishAgent(BaseAgent):
    """Agent specialized in responding to English language queries."""
    
    def __init__(self):
        super().__init__(
            name="English Agent", 
            description="I handle general queries and conversations in English."
        )
        
        # Common English patterns and indicators
        self.english_indicators = [
            # Common English words
            'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with',
            'by', 'from', 'up', 'about', 'into', 'through', 'during', 'before',
            'after', 'above', 'below', 'between', 'among', 'this', 'that', 'these',
            'those', 'what', 'when', 'where', 'why', 'how', 'who', 'which',
            
            # Common verbs
            'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
            'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might',
            'can', 'get', 'got', 'go', 'went', 'come', 'came', 'see', 'saw', 'know',
            'think', 'tell', 'say', 'said', 'take', 'took', 'make', 'made',
            
            # Question words
            'what', 'where', 'when', 'why', 'how', 'who', 'which', 'whose',
            
            # Common phrases
            'hello', 'hi', 'goodbye', 'bye', 'please', 'thank', 'thanks', 'sorry',
            'excuse', 'help', 'question', 'answer', 'explain', 'describe'
        ]
        
        # English sentence patterns
        self.english_patterns = [
            r'\b(the|a|an)\s+\w+',  # Articles
            r'\b(is|are|was|were)\s+',  # To be verbs
            r'\b(I|you|he|she|it|we|they)\s+',  # Pronouns
            r'\?\s*$',  # Questions ending with ?
            r'\b(what|where|when|why|how|who)\s+',  # Question words
        ]
    
    def can_handle(self, query: str) -> bool:
        """Check if the query is in English and should be handled by this agent."""
        
        # Skip very short or low-quality queries that might not be real English
        if len(query.strip()) < 3:
            return False
        
        # First, use language detection if available
        if LANGDETECT_AVAILABLE:
            try:
                detected_lang = detect(query)
                if detected_lang == 'en':
                    # Additional check to ensure it's actually meaningful English
                    return self._is_meaningful_english(query)
            except:
                pass  # Fall back to manual detection
        
        # Manual English detection
        query_lower = query.lower()
        words = query_lower.split()
        
        # Don't handle if it looks like gibberish (too many non-dictionary-like words)
        if self._looks_like_gibberish(query):
            return False
        
        # Check for English indicators with better threshold
        english_word_count = 0
        total_meaningful_words = 0
        
        for word in words:
            if len(word) > 1:  # Only count meaningful words
                total_meaningful_words += 1
                if word in self.english_indicators:
                    english_word_count += 1
        
        # If more than 30% of meaningful words are common English words
        if total_meaningful_words > 0 and (english_word_count / total_meaningful_words) > 0.3:
            return True
        
        # Check for English patterns
        for pattern in self.english_patterns:
            if re.search(pattern, query_lower):
                return True
        
        # Check if it's likely English based on character patterns
        if self._is_likely_english(query):
            return True
        
        return False
    
    def _is_meaningful_english(self, query: str) -> bool:
        """Check if the detected English text is meaningful."""
        # Check for complete sentences or meaningful phrases
        return (
            any(word in query.lower() for word in ['what', 'how', 'when', 'where', 'why', 'can', 'could', 'would', 'should']) or
            '?' in query or
            any(word in query.lower() for word in ['hello', 'hi', 'thank', 'please', 'help'])
        )
    
    def _looks_like_gibberish(self, query: str) -> bool:
        """Check if query looks like random gibberish."""
        words = query.lower().split()
        if not words:
            return True
        
        # Check for patterns that suggest gibberish
        gibberish_patterns = [
            r'^[a-z]*\d+[a-z]*$',  # Mixed letters and numbers
            r'^[xyz]+\d+$',        # Common placeholder patterns
            r'^.{1,3}$',           # Too short
        ]
        
        gibberish_count = 0
        for word in words:
            for pattern in gibberish_patterns:
                if re.match(pattern, word):
                    gibberish_count += 1
                    break
        
        # If more than half the words look like gibberish
        return gibberish_count > len(words) / 2
    
    def _is_likely_english(self, query: str) -> bool:
        """Additional heuristics to determine if text is likely English."""
        
        # Check for common English letter patterns
        english_patterns = [
            r'\bth(e|is|at|ere|ey|ink)\b',  # Common 'th' patterns
            r'\b(ing|tion|ed)\b',          # Common endings
            r'\s(a|an|the)\s',             # Articles with spaces
        ]
        
        for pattern in english_patterns:
            if re.search(pattern, query.lower()):
                return True
        
        # Check character distribution (English uses certain letters more frequently)
        text_length = len(query.replace(' ', ''))
        if text_length > 0:
            # Count common English letters
            common_letters = 'etaoinshrdlu'
            common_count = sum(query.lower().count(letter) for letter in common_letters)
            if (common_count / text_length) > 0.4:
                return True
        
        return False
    
    def process(self, query: str) -> Dict[str, Any]:
        """Process English language queries and provide appropriate responses."""
        try:
            response = self._generate_english_response(query)
            return {
                "agent": self.name,
                "success": True,
                "result": response,
                "query": query,
                "type": "english_language_response"
            }
        except Exception as e:
            return {
                "agent": self.name,
                "success": False,
                "error": str(e),
                "query": query,
                "type": "english_language_response"
            }
    
    def _generate_english_response(self, query: str) -> str:
        """Generate appropriate responses for English queries."""
        query_lower = query.lower().strip()
        
        # Greeting responses
        if any(greeting in query_lower for greeting in ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening']):
            return "Hello! I'm the English Agent. How can I help you today? I can assist with general questions, provide information, or have a conversation in English."
        
        # Farewell responses
        if any(farewell in query_lower for farewell in ['goodbye', 'bye', 'see you', 'farewell']):
            return "Goodbye! It was nice talking with you. Feel free to come back anytime if you need help with English language queries!"
        
        # Thank you responses
        if any(thanks in query_lower for thanks in ['thank you', 'thanks', 'thank']):
            return "You're welcome! I'm glad I could help. Is there anything else you'd like to know or discuss?"
        
        # Help requests
        if any(help_word in query_lower for help_word in ['help', 'assist', 'support']):
            return "I'm here to help! I can assist with general questions, provide explanations, discuss topics, or help with English language queries. What would you like to know about?"
        
        # Question identification and responses
        if query.strip().endswith('?'):
            return self._handle_question(query)
        
        # Information requests
        if any(word in query_lower for word in ['what is', 'what are', 'tell me about', 'explain', 'describe']):
            return self._handle_information_request(query)
        
        # Opinion or preference queries
        if any(word in query_lower for word in ['do you think', 'what do you', 'your opinion', 'prefer']):
            return self._handle_opinion_request(query)
        
        # General conversation
        return self._handle_general_conversation(query)
    
    def _handle_question(self, query: str) -> str:
        """Handle questions ending with question marks."""
        query_lower = query.lower()
        
        if query_lower.startswith('what'):
            return f"That's an interesting 'what' question: '{query}'. While I can understand and respond in English, I might not have specific knowledge about every topic. Could you provide more context or rephrase your question?"
        
        elif query_lower.startswith('how'):
            return f"You're asking 'how' about something: '{query}'. I'd be happy to help explain processes or methods if you can be more specific about what you'd like to know."
        
        elif query_lower.startswith('why'):
            return f"That's a thoughtful 'why' question: '{query}'. Understanding the reasoning behind things is important. Could you elaborate on what specific aspect you're curious about?"
        
        elif query_lower.startswith('where'):
            return f"You're asking about a location or place: '{query}'. While I can discuss general topics, I might not have current location-specific information. What would you like to know?"
        
        elif query_lower.startswith('when'):
            return f"That's a timing-related question: '{query}'. I can discuss general timeframes and schedules, but I might not have access to current or specific date information."
        
        elif query_lower.startswith('who'):
            return f"You're asking about a person or people: '{query}'. I can discuss general information about people and roles, but I might not have specific details about individuals."
        
        else:
            return f"I see you have a question: '{query}'. I'm ready to help! Could you provide a bit more detail so I can give you the most helpful response?"
    
    def _handle_information_request(self, query: str) -> str:
        """Handle requests for information or explanations."""
        return f"You're asking for information about: '{query}'. While I can engage in English conversation and provide general responses, I'm designed primarily as a language routing agent. For detailed factual information, you might want to consult specialized resources or be more specific about what you'd like to know."
    
    def _handle_opinion_request(self, query: str) -> str:
        """Handle requests for opinions or preferences."""
        return f"You're asking for my perspective on: '{query}'. As an English language agent, I can discuss topics in English, but I don't have personal opinions or preferences. I can help you explore different viewpoints on a topic or discuss various aspects of what you're interested in."
    
    def _handle_general_conversation(self, query: str) -> str:
        """Handle general conversational inputs."""
        return f"I understand you're communicating in English: '{query}'. I'm here to engage in English language conversation! Feel free to ask questions, share thoughts, or discuss topics you're interested in. What would you like to talk about?"
