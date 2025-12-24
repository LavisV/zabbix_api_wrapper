# Zabbix API Wrapper

A Python wrapper for the Zabbix API, providing a clean and intuitive interface for interacting with Zabbix monitoring systems.
Please note that this is very much a WIP, not all methods have been tested at this point in time.

## Features

- Complete coverage of Zabbix API methods
- Resource-based architecture for easy navigation
- Support for multiple environments (production, development, local)
- Flexible configuration options (hardcoded or environment variables)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/LavisV/zabbix_api_wrapper
    cd zabbix-api-wrapper
    ```

2. Copy the configuration template:

    ```bash
    cp config.py.template config.py
    ```

3. Edit `config.py` with your Zabbix server details and API tokens.

## Configuration

The `config.py` file is git-ignored and contains your personal Zabbix API credentials. Two configuration approaches are supported:

### Option 1: Hard-coded Values (Simple)

Edit `config.py` and replace the placeholder values:

```python
if self.environment == "dev":
    self.zabbix_server = "https://your-zabbix-server.com/zabbix/api_jsonrpc.php"
    self.api_token = "your-actual-api-token-here"
```

### Option 2: Environment Variables (Recommended)

Set environment variables for your tokens:

```bash
# Linux/Mac
export ZABBIX_PROD_TOKEN="your-production-token"
export ZABBIX_DEV_TOKEN="your-development-token"
export ZABBIX_LOCAL_TOKEN="your-local-token"

# Windows PowerShell
$env:ZABBIX_PROD_TOKEN="your-production-token"
$env:ZABBIX_DEV_TOKEN="your-development-token"
$env:ZABBIX_LOCAL_TOKEN="your-local-token"
```

Then in `config.py`, the code will automatically use these environment variables. You can also pass the token directly when initializing the client:

```python
client = ZabbixClient(environment="dev", api_token="your-token")
```

### Configuration Options

For each environment, you can configure:

- `zabbix_server`: Full URL to your Zabbix API endpoint
- `api_token`: Your Zabbix API token (from environment variable or hardcoded)
- `timeout`: Request timeout in seconds (default: 30 for prod, 60 for dev, 10 for local)
- `verify_ssl`: Whether to verify SSL certificates (recommended: True for prod, False for dev/local)

## Usage

```python
from client import ZabbixClient

# Initialize client (defaults to "dev" environment)
client = ZabbixClient(environment="dev")

# Or specify a custom config
from config import ZabbixConfig
custom_config = ZabbixConfig(environment="prod")
client = ZabbixClient(config=custom_config)

# Use the API resources
hostgroups = client.host_group.get()
hosts = client.hosts.get()
templates = client.templates.get()
```

## Available Resources

All Zabbix API resources are available as attributes on the client:

- `actions`, `alerts`, `apiinfo`, `auditlogs`
- `authentication`, `autoregistration`, `configuration`
- `connector`, `correlation`, `dashboard`
- `discovered_host`, `discovered_service`, `discovery_check`, `discovery_rule`
- `events`, `graphs`, `graph_item`, `graph_prototype`
- `high_availability_node`, `history`
- `hosts`, `host_group`, `host_interface`, `host_prototype`
- `housekeeping`, `icon_map`, `images`
- `items`, `item_prototype`, `lld_rule`
- `maintenance`, `maps`, `media_type`, `mfa`, `module`
- `problems`, `proxies`, `proxy_group`
- `regular_expression`, `reports`, `roles`, `scripts`
- `services`, `settings`, `sla`, `tasks`
- `templates`, `template_dashboard`, `template_group`
- `tokens`, `trends`, `triggers`, `trigger_prototype`
- `users`, `user_directory`, `user_group`, `user_macro`
- `value_map`, `web_scenario`

## Security Notes

- Never commit `config.py` to version control (it's already in `.gitignore`)
- Use environment variables for production deployments
- Rotate API tokens regularly
- Use SSL verification (`verify_ssl=True`) in production environments
- Keep your API tokens secure and never share them

## Contributing

This is a learning project. Contributions and suggestions are welcome!

## License

No license, do what you want with this.
