# Contributing to International Plebeian Academy

Thank you for your interest in contributing to the International Plebeian Academy project! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## Getting Started

### Prerequisites

- Node.js (version 18.0.0 or higher)
- Python (version 3.11.0 or higher)
- Docker and Docker Compose
- PostgreSQL (version 15.0 or higher)
- Git

### Setting Up Development Environment

1. Clone the repository:
```bash
git clone https://github.com/nbbulk-dotcom/Int_Plebeian_Tribunal_Academy.git
cd Int_Plebeian_Tribunal_Academy
```

2. Install dependencies:
```bash
python tools/setup.py install-dependencies
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Setup database:
```bash
python tools/setup.py setup-database
```

5. Start development servers:
```bash
docker-compose -f infrastructure/docker-compose.yml up
```

## Development Workflow

### Branch Naming Convention

- Feature branches: `feature/description-of-feature`
- Bug fixes: `bugfix/description-of-bug`
- Hotfixes: `hotfix/description-of-hotfix`
- Documentation: `docs/description-of-changes`

### Commit Message Format

Follow the conventional commits specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Pull Request Process

1. Create a feature branch from `main`
2. Make your changes following our coding standards
3. Write or update tests as needed
4. Ensure all tests pass
5. Update documentation if necessary
6. Submit a pull request with a clear description

## Coding Standards

### Python (Backend)

- Follow PEP 8 style guide
- Use type hints
- Maximum line length: 100 characters
- Use docstrings for all functions and classes
- Run `black` for code formatting
- Run `flake8` for linting

### TypeScript (Frontend)

- Follow ESLint configuration
- Use functional components with hooks
- Use TypeScript strict mode
- Maximum line length: 100 characters
- Use Prettier for code formatting

### Solidity (Smart Contracts)

- Follow Solidity style guide
- Use latest stable Solidity version
- Include comprehensive tests
- Document all functions with NatSpec comments

## Testing

### Running Tests

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test

# Blockchain tests
cd blockchain
npx truffle test

# Integration tests
cd tests
pytest test_integration/
```

### Test Coverage

- Maintain minimum 80% code coverage
- Write unit tests for all new features
- Include integration tests for critical paths

## Documentation

- Update README.md for user-facing changes
- Update API.md for API changes
- Add inline comments for complex logic
- Update architecture diagrams if needed

## Division-Specific Guidelines

### Communications Division
- Focus on clear, accessible documentation
- Ensure internationalization support

### Human Development Division
- Prioritize user education and onboarding
- Create comprehensive tutorials

### Support & Resource Division
- Implement robust error handling
- Provide helpful error messages

### Action & Project Division
- Ensure efficient task execution
- Optimize performance

### Integrity & Quality Division
- Maintain high code quality standards
- Comprehensive testing

### Membership & Voice Division
- Implement inclusive features
- Support accessibility standards

### Strategic Direction Division
- Consider long-term scalability
- Plan for future extensibility

## Review Process

All pull requests require:
- At least one approval from a maintainer
- All CI checks passing
- No merge conflicts
- Updated documentation

## Questions?

If you have questions, please:
1. Check existing documentation
2. Search existing issues
3. Create a new issue with the `question` label

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be recognized in our CHANGELOG.md and contributors list.

Thank you for contributing to the International Plebeian Academy!
