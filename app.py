

import argparse
import src.main as m






if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hello! I am going to read arugments back out!")
    parser.add_argument("args", nargs="*", help="Arguments to echo")

    args = parser.parse_args()
    print(args)
    
    m.main(args.args)