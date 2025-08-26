"""
Spanish Agent
Specialized agent for handling queries in Spanish language.
"""

import re
from typing import Dict, Any
from base_agent import BaseAgent

try:
    from langdetect import detect
    LANGDETECT_AVAILABLE = True
except ImportError:
    LANGDETECT_AVAILABLE = False


class SpanishAgent(BaseAgent):
    """Agent specialized in responding to Spanish language queries."""
    
    def __init__(self):
        super().__init__(
            name="Spanish Agent", 
            description="Manejo consultas generales y conversaciones en español."
        )
        
        # Common Spanish words and indicators
        self.spanish_indicators = [
            # Articles and determiners
            'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas',
            
            # Common prepositions
            'de', 'en', 'a', 'por', 'para', 'con', 'sin', 'sobre', 'bajo',
            'ante', 'tras', 'desde', 'hasta', 'hacia', 'contra',
            
            # Common verbs
            'es', 'son', 'está', 'están', 'era', 'eran', 'estaba', 'estaban',
            'ser', 'estar', 'tener', 'haber', 'hacer', 'ir', 'ver', 'dar',
            'saber', 'querer', 'poder', 'decir', 'venir', 'llevar', 'poner',
            'salir', 'llegar', 'pasar', 'seguir', 'quedar', 'creer',
            
            # Pronouns
            'yo', 'tú', 'él', 'ella', 'nosotros', 'nosotras', 'vosotros',
            'vosotras', 'ellos', 'ellas', 'me', 'te', 'se', 'nos', 'os',
            'le', 'les', 'lo', 'la', 'los', 'las',
            
            # Question words
            'qué', 'quién', 'quiénes', 'cuál', 'cuáles', 'cuándo', 'dónde',
            'cómo', 'por qué', 'para qué', 'cuánto', 'cuánta', 'cuántos', 'cuántas',
            
            # Common adjectives and adverbs
            'muy', 'más', 'menos', 'tan', 'tanto', 'mucho', 'poco', 'bien', 'mal',
            'grande', 'pequeño', 'bueno', 'malo', 'nuevo', 'viejo', 'todo', 'cada',
            
            # Greetings and common phrases
            'hola', 'adiós', 'gracias', 'por favor', 'perdón', 'disculpe',
            'señor', 'señora', 'señorita', 'sí', 'no', 'tal vez', 'quizás',
            
            # Conjunctions
            'y', 'e', 'o', 'u', 'pero', 'sino', 'aunque', 'mientras', 'cuando',
            'si', 'porque', 'como', 'que'
        ]
        
        # Spanish-specific patterns
        self.spanish_patterns = [
            r'\b(el|la|los|las)\s+\w+',  # Articles
            r'\b(es|son|está|están)\s+',  # To be verbs
            r'\b(qué|cómo|dónde|cuándo|por qué)\s+',  # Question words
            r'\w+ción\b',  # Words ending in -ción
            r'\w+mente\b',  # Adverbs ending in -mente
            r'\w+ando\b',  # Gerunds ending in -ando
            r'\w+iendo\b',  # Gerunds ending in -iendo
            r'¿.*\?',  # Questions with Spanish question marks
        ]
        
        # Spanish characters
        self.spanish_chars = 'ñáéíóúü¿¡'
    
    def can_handle(self, query: str) -> bool:
        """Check if the query is in Spanish."""
        
        # First, use language detection if available
        if LANGDETECT_AVAILABLE:
            try:
                detected_lang = detect(query)
                if detected_lang == 'es':
                    return True
            except:
                pass  # Fall back to manual detection
        
        # Check for Spanish-specific characters
        if any(char in query for char in self.spanish_chars):
            return True
        
        # Manual Spanish detection
        query_lower = query.lower()
        words = query_lower.split()
        
        # Check for Spanish indicators
        spanish_word_count = 0
        for word in words:
            if word in self.spanish_indicators:
                spanish_word_count += 1
        
        # If more than 30% of words are common Spanish words
        if len(words) > 0 and (spanish_word_count / len(words)) > 0.3:
            return True
        
        # Check for Spanish patterns
        for pattern in self.spanish_patterns:
            if re.search(pattern, query_lower):
                return True
        
        return False
    
    def process(self, query: str) -> Dict[str, Any]:
        """Process Spanish language queries and provide appropriate responses."""
        try:
            response = self._generate_spanish_response(query)
            return {
                "agent": self.name,
                "success": True,
                "result": response,
                "query": query,
                "type": "spanish_language_response"
            }
        except Exception as e:
            return {
                "agent": self.name,
                "success": False,
                "error": str(e),
                "query": query,
                "type": "spanish_language_response"
            }
    
    def _generate_spanish_response(self, query: str) -> str:
        """Generate appropriate responses for Spanish queries."""
        query_lower = query.lower().strip()
        
        # Greeting responses
        if any(greeting in query_lower for greeting in ['hola', 'buenos días', 'buenas tardes', 'buenas noches', 'saludos']):
            return "¡Hola! Soy el Agente Español. ¿Cómo puedo ayudarte hoy? Puedo asistirte con preguntas generales, proporcionar información o tener una conversación en español."
        
        # Farewell responses
        if any(farewell in query_lower for farewell in ['adiós', 'hasta luego', 'nos vemos', 'chao', 'hasta pronto']):
            return "¡Adiós! Fue un placer hablar contigo. ¡Vuelve cuando necesites ayuda con consultas en español!"
        
        # Thank you responses
        if any(thanks in query_lower for thanks in ['gracias', 'muchas gracias', 'te agradezco']):
            return "¡De nada! Me alegra poder ayudarte. ¿Hay algo más que te gustaría saber o discutir?"
        
        # Help requests
        if any(help_word in query_lower for help_word in ['ayuda', 'ayúdame', 'puedes ayudar', 'necesito ayuda']):
            return "¡Estoy aquí para ayudarte! Puedo asistirte con preguntas generales, proporcionar explicaciones, discutir temas o ayudarte con consultas en español. ¿Qué te gustaría saber?"
        
        # Question identification and responses
        if '?' in query or query.strip().startswith('¿'):
            return self._handle_spanish_question(query)
        
        # Information requests
        if any(word in query_lower for word in ['qué es', 'qué son', 'dime sobre', 'explícame', 'describe']):
            return self._handle_spanish_information_request(query)
        
        # Opinion or preference queries
        if any(word in query_lower for word in ['qué piensas', 'tu opinión', 'prefieres', 'te gusta']):
            return self._handle_spanish_opinion_request(query)
        
        # General conversation
        return self._handle_spanish_general_conversation(query)
    
    def _handle_spanish_question(self, query: str) -> str:
        """Handle questions in Spanish."""
        query_lower = query.lower()
        
        if query_lower.startswith('¿qué') or 'qué' in query_lower[:10]:
            return f"Es una pregunta interesante sobre 'qué': '{query}'. Aunque puedo entender y responder en español, puede que no tenga conocimiento específico sobre todos los temas. ¿Podrías proporcionar más contexto o reformular tu pregunta?"
        
        elif query_lower.startswith('¿cómo') or 'cómo' in query_lower[:10]:
            return f"Estás preguntando 'cómo' sobre algo: '{query}'. Me encantaría ayudarte a explicar procesos o métodos si puedes ser más específico sobre lo que te gustaría saber."
        
        elif query_lower.startswith('¿por qué') or 'por qué' in query_lower[:15]:
            return f"Es una pregunta reflexiva sobre 'por qué': '{query}'. Entender las razones detrás de las cosas es importante. ¿Podrías elaborar sobre qué aspecto específico te interesa?"
        
        elif query_lower.startswith('¿dónde') or 'dónde' in query_lower[:10]:
            return f"Estás preguntando sobre un lugar o ubicación: '{query}'. Aunque puedo discutir temas generales, puede que no tenga información específica sobre ubicaciones actuales. ¿Qué te gustaría saber?"
        
        elif query_lower.startswith('¿cuándo') or 'cuándo' in query_lower[:10]:
            return f"Es una pregunta relacionada con el tiempo: '{query}'. Puedo discutir marcos temporales generales, pero puede que no tenga acceso a información de fechas actuales o específicas."
        
        elif query_lower.startswith('¿quién') or 'quién' in query_lower[:10]:
            return f"Estás preguntando sobre una persona o personas: '{query}'. Puedo discutir información general sobre personas y roles, pero puede que no tenga detalles específicos sobre individuos."
        
        else:
            return f"Veo que tienes una pregunta: '{query}'. ¡Estoy listo para ayudar! ¿Podrías proporcionar un poco más de detalle para poder darte la respuesta más útil?"
    
    def _handle_spanish_information_request(self, query: str) -> str:
        """Handle information requests in Spanish."""
        return f"Estás pidiendo información sobre: '{query}'. Aunque puedo participar en conversaciones en español y proporcionar respuestas generales, estoy diseñado principalmente como un agente de enrutamiento de idiomas. Para información factual detallada, podrías consultar recursos especializados o ser más específico sobre lo que te gustaría saber."
    
    def _handle_spanish_opinion_request(self, query: str) -> str:
        """Handle opinion requests in Spanish."""
        return f"Estás pidiendo mi perspectiva sobre: '{query}'. Como agente de idioma español, puedo discutir temas en español, pero no tengo opiniones personales o preferencias. Puedo ayudarte a explorar diferentes puntos de vista sobre un tema o discutir varios aspectos de lo que te interesa."
    
    def _handle_spanish_general_conversation(self, query: str) -> str:
        """Handle general conversational inputs in Spanish."""
        return f"Entiendo que te estás comunicando en español: '{query}'. ¡Estoy aquí para participar en conversaciones en español! Siéntete libre de hacer preguntas, compartir pensamientos o discutir temas que te interesen. ¿De qué te gustaría hablar?"
