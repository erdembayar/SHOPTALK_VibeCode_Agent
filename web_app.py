"""
Web UI for Agentic Framework
Flask-based web application with real-time communication using WebSockets.
"""

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import json
from datetime import datetime
from primary_agent import PrimaryAgent
import threading
import time

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'agentic_framework_secret_key_2025'
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize the primary agent
primary_agent = PrimaryAgent()

# Store active sessions
active_sessions = {}


@app.route('/')
def index():
    """Main page with the web interface."""
    return render_template('index.html')


@app.route('/api/status')
def get_status():
    """API endpoint to get system status."""
    try:
        status = primary_agent.get_status()
        return jsonify({
            'success': True,
            'status': status
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/agents')
def get_agents():
    """API endpoint to get available agents."""
    try:
        agents = primary_agent.get_agent_info()
        return jsonify({
            'success': True,
            'agents': agents
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/query', methods=['POST'])
def process_query():
    """API endpoint to process a query."""
    try:
        data = request.get_json()
        query = data.get('query', '').strip()
        
        if not query:
            return jsonify({
                'success': False,
                'error': 'Empty query provided'
            }), 400
        
        # Process the query
        response = primary_agent.process_query(query)
        
        return jsonify({
            'success': True,
            'response': response,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@socketio.on('connect')
def handle_connect():
    """Handle client connection."""
    session_id = request.sid
    active_sessions[session_id] = {
        'connected_at': datetime.now().isoformat(),
        'query_count': 0
    }
    
    emit('status', {
        'type': 'connected',
        'message': 'Connected to Agentic Framework!',
        'session_id': session_id,
        'timestamp': datetime.now().isoformat()
    })
    
    # Send initial system status
    status = primary_agent.get_status()
    emit('system_status', status)


@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnection."""
    session_id = request.sid
    if session_id in active_sessions:
        del active_sessions[session_id]


@socketio.on('send_query')
def handle_query(data):
    """Handle query from client via WebSocket."""
    session_id = request.sid
    query = data.get('query', '').strip()
    
    if not query:
        emit('error', {
            'message': 'Empty query provided',
            'timestamp': datetime.now().isoformat()
        })
        return
    
    # Update session stats
    if session_id in active_sessions:
        active_sessions[session_id]['query_count'] += 1
    
    # Emit processing status
    emit('processing', {
        'message': 'Processing your query...',
        'query': query,
        'timestamp': datetime.now().isoformat()
    })
    
    # Process query in background thread
    def process_query_background():
        try:
            response = primary_agent.process_query(query)
            
            # Emit response back to client
            socketio.emit('query_response', {
                'query': query,
                'response': response,
                'timestamp': datetime.now().isoformat(),
                'session_stats': active_sessions.get(session_id, {})
            }, room=session_id)
            
            # Update system status
            status = primary_agent.get_status()
            socketio.emit('system_status', status, room=session_id)
            
        except Exception as e:
            socketio.emit('error', {
                'message': str(e),
                'query': query,
                'timestamp': datetime.now().isoformat()
            }, room=session_id)
    
    # Start background processing
    threading.Thread(target=process_query_background, daemon=True).start()


@socketio.on('get_status')
def handle_get_status():
    """Handle status request from client."""
    try:
        status = primary_agent.get_status()
        emit('system_status', status)
    except Exception as e:
        emit('error', {
            'message': f'Failed to get status: {str(e)}',
            'timestamp': datetime.now().isoformat()
        })


@socketio.on('clear_history')
def handle_clear_history():
    """Handle clear history request."""
    try:
        primary_agent.clear_history()
        emit('history_cleared', {
            'message': 'Conversation history cleared',
            'timestamp': datetime.now().isoformat()
        })
        
        # Send updated status
        status = primary_agent.get_status()
        emit('system_status', status)
        
    except Exception as e:
        emit('error', {
            'message': f'Failed to clear history: {str(e)}',
            'timestamp': datetime.now().isoformat()
        })


if __name__ == '__main__':
    print("🌐 Starting Agentic Framework Web UI...")
    print("📍 Access the web interface at: http://localhost:5000")
    print("🔄 Real-time communication enabled with WebSockets")
    print("🤖 Multi-agent system ready!")
    print("\nPress Ctrl+C to stop the server")
    
    # Run the Flask-SocketIO app
    socketio.run(
        app, 
        host='0.0.0.0', 
        port=5000, 
        debug=True,
        allow_unsafe_werkzeug=True
    )
