import argparse

parser= argparse.ArgumentParser(description='simple Calculator')
parser.add_argument('num1',type=float,help='1st number')
parser.add_argument('num2',type=float,help='2nd number')
parser.add_argument('operation', choices=['add','sub','mul','div'],help='operations')
# args= parser.parse_args()

if(args.operation == 'add'):
    print(f'the result is {args.num1 + args.num2}')
elif(args.operation == 'sub'):
    print(f'the result is {args.num1 - args.num2}')
elif(args.operation == 'mul'):
    print(f'the result is {args.num1 * args.num2}')
elif(args.operation == 'div'):
    print(f'the result is {args.num1 / args.num2}')
