import argparse
from out.output import Output
from scrapper.ScrapperFactory import ScrapperChooser


parser = argparse.ArgumentParser(description='Quizme2doc create a document of questions from a quizme url')
parser.add_argument('--url', help='a quizme url')
parser.add_argument('--highlight', action='store_true', help='mark this option if you want to get the answers highlighted in the output file')
parser.add_argument('--out', help='output location of the quiz file in docx format')

args = parser.parse_args()
scrapper = ScrapperChooser(args.url)
scrapper.run()
questions, quiz_name = scrapper.questions, scrapper.quiz_title
Output(args.out, args.highlight, quiz_name, questions).exec()



