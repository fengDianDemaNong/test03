import openai
openai.api_key = ""
COMPLETIONS_MODEL = "text-davinci-003"
EMBEDDING_MODEL = "text-embedding-ada-002"


# def completion(prompt):
#     completions = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.8,
#     )
#
#     message = completions.choices[0].text
#     return message
# print(completion("你好啊"))





prompt = """Answer the question as truthfully as possible using the provided text, and if the answer is not contained within the text below, say "I don't know"

Context:
The men's high jump event at the 2020 Summer Olympics took place between 30 July and 1 August 2021 at the Olympic Stadium.
33 athletes from 24 nations competed; the total possible number depended on how many nations would use universality places 
to enter athletes in addition to the 32 qualifying through mark or ranking (no universality places were used in 2021).
Italian athlete Gianmarco Tamberi along with Qatari athlete Mutaz Essa Barshim emerged as joint winners of the event following
a tie between both of them as they cleared 2.37m. Both Tamberi and Barshim agreed to share the gold medal in a rare instance
where the athletes of different nations had agreed to share the same medal in the history of Olympics. 
Barshim in particular was heard to ask a competition official "Can we have two golds?" in response to being offered a 
'jump off'. Maksim Nedasekau of Belarus took bronze. The medals were the first ever in the men's high jump for Italy and 
Belarus, the first gold in the men's high jump for Italy and Qatar, and the third consecutive medal in the men's high jump
for Qatar (all by Barshim). Barshim became only the second man to earn three medals in high jump, joining Patrik Sjöberg
of Sweden (1984 to 1992).

Q: Who won the 2020 Summer Olympics men's high jump?
A:"""

result=openai.Completion.create(
    prompt=prompt,
    temperature=0,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    model=COMPLETIONS_MODEL
)["choices"][0]["text"].strip(" \n")

print(result)
