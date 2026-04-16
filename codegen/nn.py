import os
from django.conf import settings

base_output_path = os.path.join(settings.BASE_DIR, 'codegen','OuputFiles')
   
def generate(s,lan):
    if lan=="Python":
        lang_path=os.path.join(base_output_path, 'Python')
        if s=="sum" or s=="sum"or s=="sub" or s=="Sum"or s=="ADD"or s=="SUM":
            with open(os.path.join(lang_path, 'Add.txt'), 'r+') as file:
               content = file.read()
            return content
        elif s=="sub" or s=="Sub"or s=="Substraction" or s=="Substract"or s=="diff"or s=="Difference" or s=="DIFF" or s=="difference":
            with open(os.path.join(lang_path, 'Sub.txt'), 'r+') as file:
               content = file.read()
            return content
        elif s=="mul" or s=="Mul"or s=="Multiplication" or s=="Multiply"or s=="prod"or s=="Product" or s=="PROD" or s=="product" or s=="multiplication" or s=="multiply":
            with open(os.path.join(lang_path, 'Mul.txt'), 'r+') as file:
               content = file.read()
            return content
        elif s=="div" or s=="Div"or s=="Division" or s=="Divide"or s=="quot"or s=="Quotient" or s=="QUOT" or s=="quotient":
            with open(os.path.join(lang_path, 'Div.txt'), 'r+') as file:
               content = file.read()
            return content
        elif s=="table" or s=="Table" or s=="Multiples" or s=="multiples":
            with open(os.path.join(lang_path, 'Table.txt'), 'r+') as file:
               content = file.read()
            return content
        else:
            return "Sorry, I can't generate code for that query yet."
    elif lan=="Java":
        lang_path=os.path.join(base_output_path, 'Java')
        if s=="sum" or s=="sum"or s=="sub" or s=="Sum"or s=="ADD"or s=="SUM":
            with open(os.path.join(lang_path, 'Add.txt'), 'r+') as file:
               content = file.read()
            return content
        elif s=="sub" or s=="Sub"or s=="Substraction" or s=="Substract"or s=="diff"or s=="Difference" or s=="DIFF" or s=="difference":
            with open(os.path.join(lang_path, 'Sub.txt'), 'r+') as file:
               content = file.read()
            return content
        elif s=="mul" or s=="Mul"or s=="Multiplication" or s=="Multiply"or s=="prod"or s=="Product" or s=="PROD" or s=="product" or s=="multiplication" or s=="multiply":
            with open(os.path.join(lang_path, 'Mul.txt'), 'r+') as file:
               content = file.read()
            return content
        elif s=="div" or s=="Div"or s=="Division" or s=="Divide"or s=="quot"or s=="Quotient" or s=="QUOT" or s=="quotient":
            with open(os.path.join(lang_path, 'Div.txt'), 'r+') as file:
               content = file.read()
            return content
        elif s=="table" or s=="Table" or s=="Multiples" or s=="multiples":
            with open(os.path.join(lang_path, 'Table.txt'), 'r+') as file:
               content = file.read()
            return content
        else:
            return "Sorry, I can't generate code for that query yet."
    elif lan=="C":
        lang_path=os.path.join(base_output_path, 'C')
        if s=="sum" or s=="sum"or s=="sub" or s=="Sum"or s=="ADD"or s=="SUM":
            with open(os.path.join(lang_path, 'Add.txt'), 'r+') as file:
               content = file.read()
            return content
        elif s=="sub" or s=="Sub"or s=="Substraction" or s=="Substract"or s=="diff"or s=="Difference" or s=="DIFF" or s=="difference":
            with open(os.path.join(lang_path, 'Sub.txt'), 'r+') as file:
               content = file.read()
            return content
        elif s=="mul" or s=="Mul"or s=="Multiplication" or s=="Multiply"or s=="prod"or s=="Product" or s=="PROD" or s=="product" or s=="multiplication" or s=="multiply":
            with open(os.path.join(lang_path, 'Mul.txt'), 'r+') as file:
               content = file.read()
            return content
        elif s=="div" or s=="Div"or s=="Division" or s=="Divide"or s=="quot"or s=="Quotient" or s=="QUOT" or s=="quotient":
            with open(os.path.join(lang_path, 'Div.txt'), 'r+') as file:
               content = file.read()
            return content
        elif s=="table" or s=="Table" or s=="Multiples" or s=="multiples":
            with open(os.path.join(lang_path, 'Table.txt'), 'r+') as file:
               content = file.read()
            return content
        else:
            return "Sorry, I can't generate code for that query yet."
        

    