import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help='test argument 1', type=str)
    parser.add_argument('--arg2', help='test argument 2', action="store_true")  # set False if not specified
    parser.add_argument('--arg3', help='test argument 3', type=int, choices=[0, 1, 2])  # optional
    args = parser.parse_args()

    print(args.arg1, args.arg2, args.arg3)
    
