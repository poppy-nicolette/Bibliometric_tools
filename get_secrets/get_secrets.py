#get_secrets.py
import os
from dotenv import load_dotenv


def get_secrets():
    """
    This function loads the secrets from the .env file and stores them in global variables.
    Be sure to set the environment variables in your .env file before running this script.
    And add the .env file to your .gitignore file to keep your secrets safe!
    Inputs: None
    Outputs: None
    """
    #load secret .env file
    load_dotenv()

    #store credentials
    _key = os.getenv('SECRET_API_KEY')
    _email = os.getenv('EMAIL')
    #etc = os.getenv('Whatever else you might need')

    #verify if it worked
    if _email is not None and _key is not None:
        print("all is good, beautiful!")

    #you can pass this function to other functions that need the secrets
    return _key, _email

def main():
    get_secrets()

if __name__ == "__main__":
    main()
    print("You key and email have now been passed. Be aware of this potential security risk.")
