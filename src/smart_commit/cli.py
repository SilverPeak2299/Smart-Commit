import keyring
import click
import subprocess
from google import genai
from google.genai import types

def get_git_dif():
    try:
        output = subprocess.check_output(["git", "diff", "--staged"])
        return output.decode("utf-8")
    except subprocess.CalledProcessError:
        return ""


def get_commit_msg(git_diff: str, API_KEY):
    client = genai.Client(api_key=API_KEY)
    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-05-20",
        config=types.GenerateContentConfig(
            system_instruction="Generate a conventional commit message from the provided git diff. Use modern conversion and styling. Keep it under 50 characters, present tense, no period."),
        contents= git_diff
    )
    
    return response.candidates[0].content.parts[0].text
    
    
def commit_with_message(message):
    try:
        result = subprocess.run(
            ['git', 'commit', '-m', message],
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

@click.command()
def main():
    API_KEY = keyring.get_password("smart-commit", "api_key")
    
    if API_KEY is None:
        print("API key not found")
        return
    
    git_diff = get_git_dif()
    
    commit_msg = get_commit_msg(git_diff, API_KEY)
    
    print(f"Generated Commit Msg: \n{commit_msg}")
    
    while True:
            choice = input("(c)ommit, (e)dit, (r)egenerate, or (q)uit:\n").lower().strip()
            
            if choice == 'c':
                success, output = commit_with_message(commit_msg)
                if success:
                    print("Committed successfully!")
                else:
                    print(f"❌ Commit failed: {output}")
                break
                
            elif choice == 'e':
                commit_msg = input(f"Edit message: {commit_msg}\n> ") or commit_msg
                
            elif choice == 'r':
                print("Regenerating...")
                commit_msg = get_commit_msg(git_diff, API_KEY)
                print(f"New message: {commit_msg}")
                
            elif choice == 'q':
                print("Cancelled.")
                break
            else:
                print("Please choose c, e, r, or q")
    
    
