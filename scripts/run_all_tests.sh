#!/bin/bash

# Run all test suites
# Executes both QA and penetration testing

set -e

echo "=========================================="
echo "Running Complete Test Suite"
echo "=========================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -q -r requirements.txt

# Start development server in background
echo "Starting development server..."
python development/app.py > /dev/null 2>&1 &
SERVER_PID=$!

# Wait for server to start
sleep 3

# Check if server is running
if ! kill -0 $SERVER_PID 2>/dev/null; then
    echo "Error: Server failed to start"
    exit 1
fi

echo "Server started (PID: $SERVER_PID)"
echo ""

# Run QA tests
echo "=========================================="
echo "Running QA Test Suite"
echo "=========================================="
python testing/run_qa_suite.py
QA_EXIT_CODE=$?

echo ""
echo ""

# Run penetration tests
echo "=========================================="
echo "Running Penetration Tests"
echo "=========================================="
python testing/run_pentest.py
PENTEST_EXIT_CODE=$?

# Stop server
echo ""
echo "Stopping server..."
kill $SERVER_PID 2>/dev/null || true
wait $SERVER_PID 2>/dev/null || true

echo ""
echo "=========================================="
echo "Test Suite Complete"
echo "=========================================="
echo "QA Tests: $([ $QA_EXIT_CODE -eq 0 ] && echo 'PASSED' || echo 'FAILED')"
echo "Penetration Tests: $([ $PENTEST_EXIT_CODE -eq 0 ] && echo 'PASSED' || echo 'FAILED')"
echo ""

# Exit with error if any tests failed
if [ $QA_EXIT_CODE -ne 0 ] || [ $PENTEST_EXIT_CODE -ne 0 ]; then
    exit 1
fi

exit 0

