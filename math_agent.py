"""
Math Geek Agent
Specialized agent for handling mathematical queries and calculations.
"""

import re
import math
from typing import Dict, Any
from base_agent import BaseAgent

try:
    import sympy as sp
    SYMPY_AVAILABLE = True
except ImportError:
    SYMPY_AVAILABLE = False


class MathGeekAgent(BaseAgent):
    """Agent specialized in mathematical calculations and problem solving."""
    
    def __init__(self):
        super().__init__(
            name="Math Geek", 
            description="I solve mathematical problems, perform calculations, and work with equations."
        )
        
        # Mathematical keywords and patterns
        self.math_keywords = [
            'calculate', 'compute', 'solve', 'equation', 'integral', 'derivative',
            'factorial', 'square', 'sqrt', 'root', 'logarithm', 'log', 'sin', 'cos',
            'tan', 'trigonometry', 'algebra', 'geometry', 'calculus', 'matrix',
            'polynomial', 'function', 'limit', 'sum', 'product', 'mathematics',
            'math', 'arithmetic', 'power', 'exponent'
        ]
        
        # Math operators and symbols
        self.math_patterns = [
            r'\d+\s*[\+\-\*\/\^\%]\s*\d+',  # Basic arithmetic
            r'sin|cos|tan|log|ln|exp|sqrt',  # Functions
            r'\d+\s*[\+\-\*\/]\s*\d+',      # Simple operations
            r'x\s*[\+\-\*\/\^]\s*\d+',      # Algebraic expressions
            r'\d+\!',                        # Factorial
            r'\(\s*\d+.*\)',                 # Parentheses expressions
        ]
    
    def can_handle(self, query: str) -> bool:
        """Check if the query contains mathematical content."""
        query_lower = query.lower()
        
        # First check for explicit mathematical patterns
        for pattern in self.math_patterns:
            if re.search(pattern, query):
                return True
        
        # Check for numbers with operators
        if re.search(r'\d+.*[\+\-\*\/\^\%].*\d+', query):
            return True
        
        # More specific math keyword checking to avoid false positives
        math_context_patterns = [
            r'\b(calculate|compute|solve|equation)\b.*\d+',
            r'\d+.*\b(factorial|square|sqrt|root|power|exponent)\b',
            r'\b(sin|cos|tan|log|ln|exp)\s*\(',
            r'\b(integral|derivative|limit|sum|product)\b.*\w+',
            r'\bmathematics?\b|\bmath\b.*\b(problem|question|calculation)\b',
            r'\b(square\s+root|what\s+is.*factorial|calculate.*of)\b',
        ]
        
        for pattern in math_context_patterns:
            if re.search(pattern, query_lower):
                return True
        
        # Check for strong math keywords only in mathematical context
        strong_math_keywords = ['calculate', 'compute', 'factorial', 'sqrt', 'square root', 'logarithm']
        for keyword in strong_math_keywords:
            if keyword in query_lower and (re.search(r'\d+', query) or 'what is' in query_lower):
                return True
        
        # Check if it's purely mathematical expression
        cleaned_query = re.sub(r'[^\w\s\+\-\*\/\^\(\)\.]', '', query)
        if re.match(r'^[\s\w]*[\d\+\-\*\/\^\(\)\.]+[\s\w]*$', cleaned_query) and re.search(r'\d', query):
            # Make sure it's not just words containing numbers
            if re.search(r'\d+\s*[\+\-\*\/\^]\s*\d+', query):
                return True
            
        return False
    
    def process(self, query: str) -> Dict[str, Any]:
        """Process mathematical queries and return results."""
        try:
            result = self._solve_math_query(query)
            return {
                "agent": self.name,
                "success": True,
                "result": result,
                "query": query,
                "type": "mathematical_calculation"
            }
        except Exception as e:
            return {
                "agent": self.name,
                "success": False,
                "error": str(e),
                "query": query,
                "type": "mathematical_calculation"
            }
    
    def _solve_math_query(self, query: str) -> str:
        """Solve various types of mathematical queries."""
        query_lower = query.lower()
        
        # Handle basic arithmetic expressions
        if self._is_arithmetic_expression(query):
            return self._evaluate_arithmetic(query)
        
        # Handle specific mathematical functions
        if 'factorial' in query_lower:
            return self._handle_factorial(query)
        
        if any(func in query_lower for func in ['sin', 'cos', 'tan']):
            return self._handle_trigonometry(query)
        
        if 'sqrt' in query_lower or 'square root' in query_lower:
            return self._handle_square_root(query)
        
        if 'power' in query_lower or '^' in query or '**' in query:
            return self._handle_power(query)
        
        # Try to use sympy for more complex expressions
        if SYMPY_AVAILABLE:
            return self._handle_with_sympy(query)
        
        # Fallback to basic evaluation
        return self._evaluate_simple_expression(query)
    
    def _is_arithmetic_expression(self, query: str) -> bool:
        """Check if query is a simple arithmetic expression."""
        # Look for patterns like "25 + 17", "Calculate 5 * 3", etc.
        arithmetic_patterns = [
            r'\d+\s*[\+\-\*\/]\s*\d+',  # Simple arithmetic like "25 + 17"
            r'calculate\s+\d+\s*[\+\-\*\/]\s*\d+',  # "Calculate 25 + 17"
            r'\d+\s*[\+\-\*\/]\s*\d+\s*[\+\-\*\/]\s*\d+',  # Multiple operations
        ]
        
        for pattern in arithmetic_patterns:
            if re.search(pattern, query.lower()):
                return True
                
        return False
    
    def _evaluate_arithmetic(self, query: str) -> str:
        """Safely evaluate arithmetic expressions."""
        try:
            # Extract and clean the mathematical expression more carefully
            # Look for patterns like "Calculate 25 + 17" or "25 + 17"
            
            # First try to find a clear mathematical expression
            math_expression_match = re.search(r'(\d+(?:\.\d+)?)\s*([\+\-\*\/])\s*(\d+(?:\.\d+)?)', query)
            
            if math_expression_match:
                # Found a simple binary operation
                num1 = float(math_expression_match.group(1))
                operator = math_expression_match.group(2)
                num2 = float(math_expression_match.group(3))
                
                if operator == '+':
                    result = num1 + num2
                elif operator == '-':
                    result = num1 - num2
                elif operator == '*':
                    result = num1 * num2
                elif operator == '/':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        return "Cannot divide by zero"
                
                # Format result nicely
                if result == int(result):
                    result = int(result)
                
                return f"The result of {num1} {operator} {num2} is {result}"
            
            # Try to extract a more complex expression
            # Remove words but keep mathematical symbols and numbers
            expression = re.sub(r'\b(calculate|compute|solve|what is|the result of)\b', '', query.lower())
            expression = re.sub(r'[^\d\+\-\*\/\(\)\.\s]', '', expression)
            expression = expression.strip()
            
            if expression and re.search(r'\d', expression):
                # Safely evaluate the expression
                result = eval(expression)
                
                # Format result nicely
                if isinstance(result, float) and result == int(result):
                    result = int(result)
                
                return f"The result of {expression} is {result}"
            else:
                return f"Could not extract a mathematical expression from: {query}"
                
        except Exception as e:
            return f"Could not evaluate the arithmetic expression: {query}. Error: {str(e)}"
    
    def _handle_factorial(self, query: str) -> str:
        """Handle factorial calculations."""
        numbers = re.findall(r'\d+', query)
        if numbers:
            n = int(numbers[0])
            if n <= 20:  # Prevent huge calculations
                result = math.factorial(n)
                return f"The factorial of {n} is {result}"
            else:
                return f"Factorial of {n} is too large to calculate"
        return "Could not find a number for factorial calculation"
    
    def _handle_trigonometry(self, query: str) -> str:
        """Handle trigonometric functions."""
        numbers = re.findall(r'\d+(?:\.\d+)?', query)
        if not numbers:
            return "Please specify a number for trigonometric calculation"
        
        angle = float(numbers[0])
        query_lower = query.lower()
        
        # Convert to radians if it seems like degrees
        if 'degree' in query_lower or 'deg' in query_lower:
            angle_rad = math.radians(angle)
        else:
            angle_rad = angle
        
        if 'sin' in query_lower:
            result = math.sin(angle_rad)
            return f"sin({angle}) = {result:.6f}"
        elif 'cos' in query_lower:
            result = math.cos(angle_rad)
            return f"cos({angle}) = {result:.6f}"
        elif 'tan' in query_lower:
            result = math.tan(angle_rad)
            return f"tan({angle}) = {result:.6f}"
        
        return "Could not determine which trigonometric function to use"
    
    def _handle_square_root(self, query: str) -> str:
        """Handle square root calculations."""
        numbers = re.findall(r'\d+(?:\.\d+)?', query)
        if numbers:
            n = float(numbers[0])
            if n >= 0:
                result = math.sqrt(n)
                return f"The square root of {n} is {result:.6f}"
            else:
                return f"Cannot calculate square root of negative number {n}"
        return "Could not find a number for square root calculation"
    
    def _handle_power(self, query: str) -> str:
        """Handle power calculations."""
        # Look for patterns like "2 to the power of 3" or "2^3" or "2**3"
        power_match = re.search(r'(\d+(?:\.\d+)?)\s*(?:to the power of|\^|\*\*)\s*(\d+(?:\.\d+)?)', query)
        if power_match:
            base = float(power_match.group(1))
            exponent = float(power_match.group(2))
            result = base ** exponent
            return f"{base} to the power of {exponent} is {result}"
        
        return "Could not parse the power expression"
    
    def _handle_with_sympy(self, query: str) -> str:
        """Use sympy for more complex mathematical expressions."""
        try:
            # Try to extract mathematical expressions from the query
            # This is a simplified approach
            expression_match = re.search(r'[\d\+\-\*\/\^\(\)x]+', query)
            if expression_match:
                expr_str = expression_match.group()
                expr_str = expr_str.replace('^', '**')  # Convert to Python power notation
                
                if 'x' in expr_str:
                    x = sp.Symbol('x')
                    expr = sp.sympify(expr_str)
                    
                    if 'solve' in query.lower():
                        solution = sp.solve(expr, x)
                        return f"Solution(s) for {expr_str} = 0: {solution}"
                    elif 'derivative' in query.lower():
                        derivative = sp.diff(expr, x)
                        return f"Derivative of {expr_str} is: {derivative}"
                    elif 'integral' in query.lower():
                        integral = sp.integrate(expr, x)
                        return f"Integral of {expr_str} is: {integral}"
                    else:
                        return f"Expression: {expr_str} = {expr}"
                else:
                    expr = sp.sympify(expr_str)
                    result = expr.evalf()
                    return f"The result of {expr_str} is {result}"
        except Exception as e:
            return f"Could not process with sympy: {str(e)}"
        
        return "Could not parse the mathematical expression"
    
    def _evaluate_simple_expression(self, query: str) -> str:
        """Fallback method for simple evaluations."""
        # Extract numbers from the query
        numbers = re.findall(r'\d+(?:\.\d+)?', query)
        
        if len(numbers) >= 2:
            a, b = float(numbers[0]), float(numbers[1])
            query_lower = query.lower()
            
            if any(op in query_lower for op in ['add', 'plus', '+']):
                return f"{a} + {b} = {a + b}"
            elif any(op in query_lower for op in ['subtract', 'minus', '-']):
                return f"{a} - {b} = {a - b}"
            elif any(op in query_lower for op in ['multiply', 'times', '*']):
                return f"{a} * {b} = {a * b}"
            elif any(op in query_lower for op in ['divide', 'divided by', '/']):
                if b != 0:
                    return f"{a} / {b} = {a / b}"
                else:
                    return "Cannot divide by zero"
        
        return f"I understand this is a math question, but I need a clearer mathematical expression to solve. Could you rephrase? Original query: {query}"
