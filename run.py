import argparse
from out.output import Output
from scrapper.scrapper import Scrapper

parser = argparse.ArgumentParser(description='Quizme2doc create a document of questions from a quizme url')
parser.add_argument('--url',help='a quizme url')
parser.add_argument('--highlight',action='store_true',help='mark this option if you want to get the answers highlighted in the output file')
parser.add_argument('--out',help='output location of the quiz file in docx format')


args = parser.parse_args()
scrapper=Scrapper
q_collect , quiz_name =scrapper(args.url).make()
Output(args.out,args.highlight,quiz_name,q_collect).exec()

print(q_collect)
