import sys
from client import FinePrintDetective
import json

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py <path_to_tos_file>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    try:
        with open(file_path, "r") as f:
            tos_text = f.read()
            
        print(f"🕵️ Scanning {file_path} via Agent.ai...")
        detective = FinePrintDetective()
        result = detective.scan_tos(tos_text)
        
        print("\n" + "="*50)
        print("📝 SUMMARY AND RISK REPORT")
        print("="*50)
        print(result.get("output", json.dumps(result, indent=2)))
        
    except Exception as e:
        print(f"Error: {e}")
