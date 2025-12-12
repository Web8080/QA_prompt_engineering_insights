# Testing Documentation

## QA Test Framework

The QA framework implements comprehensive testing for AI/LLM prompt engineering.

### Running QA Tests

```bash
# Run QA test suite
python testing/run_qa_suite.py

# With custom API URL
API_BASE_URL=http://localhost:5000 python testing/run_qa_suite.py
```

### Test Coverage

#### 1. Consistency Testing
Tests the same prompt across multiple runs to ensure consistent outputs.

#### 2. Adversarial Testing
Tests various attack vectors:
- Instruction injection
- XSS attempts
- Buffer overflow
- SQL injection
- Path traversal
- Template injection

#### 3. Context Engineering
Tests context handling:
- Short context
- Long context
- Context ordering
- Context overflow

#### 4. Evaluation Metrics
Multi-dimensional evaluation:
- Accuracy
- Latency
- Consistency
- Safety

#### 5. Regression Testing
Tests prompt versioning and compatibility across versions.

#### 6. Variant Testing
Tests same intent with different phrasings to ensure robustness.

#### 7. Security Testing
- Rate limiting
- Input validation
- Data leakage prevention
- Authentication (placeholder)

#### 8. Production Readiness
- Health checks
- Error handling
- Performance metrics
- Logging (placeholder)

## Penetration Testing

### Running Penetration Tests

```bash
# Run OWASP Top 10 tests
python testing/run_pentest.py

# With custom API URL
API_BASE_URL=http://localhost:5000 python testing/run_pentest.py
```

### OWASP Top 10 Coverage

Each category includes multiple test cases:

- **A01: Broken Access Control** - Unauthorized access, privilege escalation
- **A02: Cryptographic Failures** - Insecure transmission, weak encryption
- **A03: Injection** - SQL, NoSQL, command, template injection
- **A04: Insecure Design** - Missing controls, weak logic
- **A05: Security Misconfiguration** - Defaults, debug mode, CORS
- **A06: Vulnerable Components** - Dependency scanning (placeholder)
- **A07: Authentication Failures** - Password policy, sessions (placeholder)
- **A08: Integrity Failures** - Code/data integrity (placeholder)
- **A09: Logging Failures** - Sensitive logging, log injection
- **A10: SSRF** - Server-side request forgery

## Running All Tests

```bash
# Run complete test suite (QA + Penetration)
./scripts/run_all_tests.sh
```

This script:
1. Sets up virtual environment
2. Installs dependencies
3. Starts development server
4. Runs QA tests
5. Runs penetration tests
6. Generates reports
7. Cleans up

## Test Reports

Test reports are generated as JSON files:
- QA reports: `qa_report_YYYYMMDD_HHMMSS.json`
- Penetration reports: `pentest_report_YYYYMMDD_HHMMSS.json`

## Interpreting Results

### QA Test Status
- **PASS**: Test passed successfully
- **FAIL**: Test failed, requires attention
- **WARN**: Test passed but with warnings
- **SKIP**: Test skipped (not applicable)

### Penetration Test Status
- **VULNERABLE**: Security vulnerability found
- **SECURE**: No vulnerability detected
- **INCONCLUSIVE**: Unable to determine (requires manual review)
- **NOT_APPLICABLE**: Test not applicable to this system

### Severity Levels
- **CRITICAL**: Immediate action required
- **HIGH**: Address as soon as possible
- **MEDIUM**: Address in next release
- **INFO**: Informational only

