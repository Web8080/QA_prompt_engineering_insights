"""
QA Test Suite Runner
Executes comprehensive QA framework tests
"""

import sys
import os
import json
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from testing.qa_framework import QAFramework

def main():
    """Run QA test suite"""
    print("=" * 80)
    print("QA Prompt Engineering Test Suite")
    print("=" * 80)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    base_url = os.getenv('API_BASE_URL', 'http://localhost:5001')
    print(f"Testing API at: {base_url}\n")
    
    framework = QAFramework(base_url=base_url)
    report = framework.run_all_tests()
    
    print("\n" + "=" * 80)
    print("TEST RESULTS SUMMARY")
    print("=" * 80)
    print(f"Total Tests: {report['summary']['total']}")
    print(f"Passed: {report['summary']['passed']}")
    print(f"Failed: {report['summary']['failed']}")
    print(f"Warnings: {report['summary']['warned']}")
    print(f"Skipped: {report['summary']['skipped']}")
    print(f"Pass Rate: {report['summary']['pass_rate']:.2f}%")
    print("=" * 80)
    
    print("\nDetailed Results:")
    print("-" * 80)
    for result in report['results']:
        status_symbol = {
            'PASS': '✓',
            'FAIL': '✗',
            'WARN': '⚠',
            'SKIP': '-'
        }.get(result['status'], '?')
        
        print(f"{status_symbol} {result['test_name']}")
        print(f"  Status: {result['status']}")
        print(f"  Message: {result['message']}")
        print(f"  Execution Time: {result['execution_time']:.2f}s")
        print()
    
    output_file = f"qa_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\nFull report saved to: {output_file}")
    print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    return 0 if report['summary']['failed'] == 0 else 1

if __name__ == '__main__':
    sys.exit(main())

