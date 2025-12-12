# Quick Start Guide

## Getting Started

### 1. Setup Environment

```bash
# Clone or extract the project
cd AI_QA

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Copy environment template
cp config/.env.example .env

# Edit .env and add your API keys
# OPENAI_API_KEY=your_key_here
```

### 3. Run Development Server

```bash
# Start the Flask application
python development/app.py

# Server runs on http://localhost:5001
```

### 4. Run Tests

#### QA Tests
```bash
# Run comprehensive QA test suite
python testing/run_qa_suite.py
```

#### Penetration Tests
```bash
# Run OWASP Top 10 penetration tests
python testing/run_pentest.py
```

#### All Tests
```bash
# Run complete test suite (starts server automatically)
./scripts/run_all_tests.sh
```

### 5. Package Project

```bash
# Create zip archive of entire project
./scripts/package.sh

# Output: packages/qa-prompt-engineering_TIMESTAMP.zip
```

## Project Structure

- `development/` - Main application code
- `testing/` - QA and penetration testing frameworks
- `production/` - Production deployment configs (placeholders)
- `config/` - Configuration files
- `scripts/` - Utility scripts
- `docs/` - Documentation

## Key Features

### QA Framework (8 Edge Cases)
1. Consistency Testing
2. Adversarial Testing
3. Context Engineering
4. Evaluation Metrics
5. Regression Testing
6. Variant Testing
7. Security Testing
8. Production Readiness

### OWASP Top 10 Coverage
All 10 OWASP categories tested:
- A01-A10: Complete security testing suite

## API Endpoints

- `GET /health` - Health check
- `POST /api/v1/process` - Process text
- `POST /api/v1/batch` - Batch processing

## Example Usage

```bash
# Process text
curl -X POST http://localhost:5001/api/v1/process \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello world", "instruction": "Summarize"}'

# Health check
curl http://localhost:5001/health
```

## Next Steps

1. Review `docs/ARCHITECTURE.md` for architecture details
2. Read `docs/TESTING.md` for testing documentation
3. Check `docs/DEPLOYMENT.md` for production deployment
4. Update production placeholders in `production/` directory

## Troubleshooting

- **Import errors**: Ensure virtual environment is activated
- **Server won't start**: Check port 5000 is available
- **API errors**: Verify OPENAI_API_KEY in .env file
- **Test failures**: Ensure server is running before tests

