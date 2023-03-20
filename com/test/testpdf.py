import pdfplumber
import pandas as pd
import openai
openai.api_key = "p"
COMPLETIONS_MODEL = "text-davinci-003"
EMBEDDING_MODEL = "text-embedding-ada-002"


def readpdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        content = ''
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            page_content = '\n'.join(page.extract_text().split('\n')[:-1])
            content = content + page_content
            # print("=========分页分隔============")
            # print(page_content)
        return content


def write2csv(dict,path,fine_name):
    pd.DataFrame(dict)
    pd.to_csv("{path}/{fine_name}".format(path=path,fine_name=fine_name))


def request_gpt(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.8,
    )

    message = completions.choices[0].text
    return message



str=""""""
dict={"title":"","content ":str}
path="D:\\data\\idea_data\\test03\\testfile"
file_name="test01"

if __name__ == '__main__':
    pdf_path='D:\\data\\idea_data\\test02\\testfile\\test.pdf'
    content=readpdf(pdf_path)

    q_str="""
      给你一篇文章：
       {content}
      请帮我描述一下，这篇文章将的主要内容
    """.format(content=content)
    print(content)
    # print(request_gpt(q_str))


