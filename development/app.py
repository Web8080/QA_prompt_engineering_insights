"""
Main application - AI-powered text processing API
Production-ready with proper error handling and security
"""

import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import yaml

load_dotenv()

app = Flask(__name__)
CORS(app)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_config():
    """Load configuration from YAML file"""
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            if not config:
                raise ValueError("Configuration file is empty")
            return config
    except FileNotFoundError:
        logger.error(f"Configuration file not found: {config_path}")
        raise
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML configuration: {str(e)}")
        raise

config = load_config()

class AITextProcessor:
    """AI-powered text processing service"""
    
    def __init__(self):
        self.model = config['ai']['model']
        self.temperature = config['ai']['temperature']
        self.max_tokens = config['ai']['max_tokens']
    
    def process_text(self, text, instruction=None):
        """
        Process text using AI model
        
        Args:
            text: Input text to process
            instruction: Optional instruction for processing
        
        Returns:
            Processed text result
        """
        if not text or not isinstance(text, str):
            raise ValueError("Text must be a non-empty string")
        
        if len(text) > config['security']['max_request_size']:
            raise ValueError("Text exceeds maximum size limit")
        
        prompt = self._build_prompt(text, instruction)
        
        try:
            result = self._call_ai_model(prompt)
            return {
                'success': True,
                'result': result,
                'model': self.model
            }
        except Exception as e:
            logger.error(f"AI processing error: {str(e)}")
            raise
    
    def _build_prompt(self, text, instruction):
        """Build prompt from text and instruction"""
        if instruction:
            return f"{instruction}\n\nText: {text}"
        return f"Process the following text: {text}"
    
    def _call_ai_model(self, prompt):
        """
        Call AI model - placeholder for actual implementation
        In production, this would call OpenAI API or similar
        """
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            logger.warning("API key not found, using mock response")
            return f"[MOCK] Processed: {prompt[:100]}..."
        
        try:
            import openai
            client = openai.OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"OpenAI API error: {str(e)}")
            raise

processor = AITextProcessor()

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'version': config['app']['version']
    }), 200

@app.route('/api/v1/process', methods=['POST'])
def process_text():
    """
    Main text processing endpoint
    
    Expected JSON:
    {
        "text": "text to process",
        "instruction": "optional instruction"
    }
    """
    try:
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        data = request.get_json()
        
        if 'text' not in data:
            return jsonify({'error': 'Missing required field: text'}), 400
        
        text = data['text']
        instruction = data.get('instruction')
        
        result = processor.process_text(text, instruction)
        
        return jsonify(result), 200
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/v1/batch', methods=['POST'])
def batch_process():
    """
    Batch processing endpoint
    
    Expected JSON:
    {
        "texts": ["text1", "text2", ...],
        "instruction": "optional instruction"
    }
    """
    try:
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        data = request.get_json()
        
        if 'texts' not in data or not isinstance(data['texts'], list):
            return jsonify({'error': 'Missing or invalid field: texts (must be array)'}), 400
        
        texts = data['texts']
        if len(texts) == 0:
            return jsonify({'error': 'Texts array cannot be empty'}), 400
        if len(texts) > 100:
            return jsonify({'error': 'Maximum 100 texts per batch'}), 400
        
        instruction = data.get('instruction')
        results = []
        
        for text in texts:
            try:
                result = processor.process_text(text, instruction)
                results.append(result)
            except Exception as e:
                results.append({
                    'success': False,
                    'error': str(e)
                })
        
        return jsonify({
            'success': True,
            'results': results,
            'total': len(results)
        }), 200
    
    except Exception as e:
        logger.error(f"Batch processing error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(
        host=config['app']['host'],
        port=config['app']['port'],
        debug=config['app']['debug']
    )

