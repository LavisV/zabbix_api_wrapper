# Security Guidelines

This document outlines security best practices for using the Zabbix API Wrapper.

## Configuration Security

### Never Commit Sensitive Data

- The `config.py` file is git-ignored and should never be committed
- API tokens, server URLs, and credentials must remain local
- Use `config.py.template` as a reference, not as a working configuration

### API Token Management

1. **Use Environment Variables in Production**
   - Set tokens via environment variables rather than hardcoding
   - Use different tokens for different environments
   - Rotate tokens regularly

2. **Token Permissions**
   - Create API tokens with minimal required permissions
   - Use read-only tokens when possible for automation scripts
   - Review and audit token usage regularly

3. **Token Storage**
   - Never store tokens in version control
   - Use secure secret management systems in production (e.g., HashiCorp Vault, AWS Secrets Manager)
   - Avoid logging tokens or including them in error messages

### Network Security

1. **SSL/TLS**
   - Always use HTTPS (`verify_ssl=True`) in production environments
   - Verify SSL certificates to prevent man-in-the-middle attacks
   - Only disable SSL verification in local development environments

2. **Network Isolation**
   - Restrict Zabbix API access to trusted networks when possible
   - Use VPN or private networks for production API access
   - Implement firewall rules to limit access

### Code Security

1. **Input Validation**
   - Validate all user inputs before making API calls
   - Sanitize parameters to prevent injection attacks
   - Handle API errors gracefully without exposing sensitive information

2. **Error Handling**
   - Avoid logging sensitive data in error messages
   - Don't expose full API responses in logs if they contain sensitive information
   - Use appropriate log levels (debug, info, warning, error)

3. **Dependencies**
   - Keep dependencies up to date
   - Review dependency security advisories regularly
   - Use `pip audit` or similar tools to check for vulnerabilities

## Reporting Security Issues

If you discover a security vulnerability, please report it responsibly:

1. Do not open a public issue
2. Contact the maintainer directly
3. Provide details about the vulnerability and steps to reproduce

## Best Practices Checklist

- [ ] `config.py` is in `.gitignore` and not committed
- [ ] API tokens are stored securely (environment variables or secret management)
- [ ] SSL verification is enabled in production
- [ ] Tokens have minimal required permissions
- [ ] Different tokens are used for different environments
- [ ] Tokens are rotated regularly
- [ ] Network access to Zabbix API is restricted
- [ ] Dependencies are kept up to date
- [ ] Error messages don't expose sensitive information
- [ ] Logs don't contain API tokens or sensitive data
