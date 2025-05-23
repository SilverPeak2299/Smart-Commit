import keyring
import click
import subprocess

def get_git_dif():
    try:
        output = subprocess.check_output(["git", "diff", "--staged"])
        return output.decode("utf-8")
    except subprocess.CalledProcessError:
        return ""

@click.command()
def main():
    API_KEY = keyring.get_password("smart-commit", "api_key")
    
    if API_KEY is None:
        print("API key not found")
        return
    
    git_diff = get_git_dif()
    
    print(git_diff)
        
    
