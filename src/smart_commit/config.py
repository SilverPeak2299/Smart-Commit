import click
import keyring

@click.command()
@click.argument("api_key", required=True)
def main(api_key: str):
    
    # Using OS password manager to store the API key securely
    keyring.set_password("smart-commit", "api_key", api_key)
    print("API key set successfully.")