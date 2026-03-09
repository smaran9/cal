from flask import Flask, render_template, request, jsonify
from functools import lru_cache
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

class NumberConverter:
    """Efficient number system converter with caching"""
    
    @staticmethod
    @lru_cache(maxsize=256)
    def decimal_to_binary(n):
        """Convert decimal to binary efficiently"""
        if n == 0:
            return "0"
        if n < 0:
            raise ValueError("Negative numbers not supported")
        
        binary = bin(n)[2:]  # Use Python's built-in bin() for efficiency
        return binary
    
    @staticmethod
    @lru_cache(maxsize=256)
    def binary_to_decimal(b):
        """Convert binary to decimal efficiently"""
        if not b or not all(c in '01' for c in b):
            raise ValueError("Invalid binary number")
        return str(int(b, 2))
    
    @staticmethod
    @lru_cache(maxsize=256)
    def decimal_to_hex(n):
        """Convert decimal to hexadecimal"""
        if n < 0:
            raise ValueError("Negative numbers not supported")
        return hex(n)[2:].upper()
    
    @staticmethod
    @lru_cache(maxsize=256)
    def hex_to_decimal(h):
        """Convert hexadecimal to decimal"""
        try:
            return str(int(h, 16))
        except ValueError:
            raise ValueError("Invalid hexadecimal number")
    
    @staticmethod
    def get_binary_info(n):
        """Get detailed binary information"""
        if n < 0:
            raise ValueError("Negative numbers not supported")
        
        binary = bin(n)[2:]
        return {
            'decimal': n,
            'binary': binary,
            'hex': hex(n)[2:].upper(),
            'octal': oct(n)[2:],
            'bits': len(binary),
            'ones': binary.count('1'),
            'zeros': binary.count('0')
        }

converter = NumberConverter()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    """Main conversion endpoint"""
    try:
        data = request.json
        conversion_type = data.get('type')
        value = data.get('value', '').strip()
        
        if not value:
            return jsonify({'error': 'Input cannot be empty'}), 400
        
        result = None
        output_type = None
        
        if conversion_type == 'dec_to_bin':
            number = int(value)
            result = converter.decimal_to_binary(number)
            output_type = 'Binary'
            
        elif conversion_type == 'bin_to_dec':
            result = converter.binary_to_decimal(value)
            output_type = 'Decimal'
            
        elif conversion_type == 'dec_to_hex':
            number = int(value)
            result = converter.decimal_to_hex(number)
            output_type = 'Hexadecimal'
            
        elif conversion_type == 'hex_to_dec':
            result = converter.hex_to_decimal(value)
            output_type = 'Decimal'
            
        elif conversion_type == 'binary_info':
            number = int(value)
            info = converter.get_binary_info(number)
            return jsonify({
                'input': value,
                'info': info,
                'type': 'Binary Information'
            })
        
        else:
            return jsonify({'error': 'Invalid conversion type'}), 400
        
        return jsonify({
            'input': value,
            'output': result,
            'type': output_type
        })
    
    except ValueError as e:
        return jsonify({'error': str(e) or 'Invalid input'}), 400
    except Exception as e:
        return jsonify({'error': 'Conversion failed: ' + str(e)}), 500

@app.route('/cache-info', methods=['GET'])
def cache_info():
    """Get cache statistics"""
    return jsonify({
        'cache_info': {
            'dec_to_bin': converter.decimal_to_binary.cache_info()._asdict(),
            'bin_to_dec': converter.binary_to_decimal.cache_info()._asdict(),
        }
    })

@app.route('/clear-cache', methods=['POST'])
def clear_cache():
    """Clear conversion cache"""
    converter.decimal_to_binary.cache_clear()
    converter.binary_to_decimal.cache_clear()
    converter.decimal_to_hex.cache_clear()
    converter.hex_to_decimal.cache_clear()
    return jsonify({'message': 'Cache cleared successfully'})

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Decimal ↔ Binary ↔ Hex Converter")
    print("="*60)
    print("✅ Server running on: http://localhost:5000")
    print("📚 Visit the app to see the beautiful interface!")
    print("⏰ Press Ctrl+C to stop the server")
    print("="*60 + "\n")
    app.run(debug=True, port=5000, use_reloader=True)
