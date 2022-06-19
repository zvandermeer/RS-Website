import json
from typing import Dict

#input file path to the json where the answers are coming from
file_path = r"test.json"

test_input = {'csrfmiddlewaretoken': ['RqtSdaPK0HCkFWGWDA2IvxK5uTDsa1xGacs0ObB803i6Gx17uheKXmtAJwnzZRtV'], 'name': ['jeff'], 'q1': ['2', '3'], 'q2': ['2', '4'], 'q3': ['1'], 'q4': ['3'], 'q5': ['2'], 'q6': ['1'], 'q7': ['1'], 'q8': ['2'], 'q9': ['1'], 'q10': ['1'], 'q11': ['1']}
final_information = {}

religions = ["Basedism", "Hinduism", "Buddhism", "Sikhism", "Christianity", "Islam", "Judaism"]

religion_pro_cons = {
    "Basedism" : {
        "pro" : [],
        "con" : []
    },
    "Hinduism" : {
        "pro" : [],
        "con" : []
    },
    "Buddhism" : {
        "pro" : [],
        "con" : []
    },
    "Sikhism" : {
        "pro" : [],
        "con" : []
    },
    "Christianity" : {
        "pro" : [],
        "con" : []
    },
    "Islam" : {
        "pro" : [],
        "con" : []
    },
    "Judaism" : {
        "pro" : [],
        "con" : []
    }
}

questions = [
    "What happens after death?",
    "How many deities are there?",
    "Types and amount of prayer?",
    "What kind of restrictions are you alright with?",
    "Do you want to travel/go on a pilgrimage?",
    "Perfered type of meeting place for your relgious gatherings",
    "Does sitting with people of the opposite sex distract you from the service?",
    "Do you want your place of worship to open during non-service times for personal prayer?",
    "Perfered method of joining a religion",
    "How do you think the world/universe was created?",
    "Do you wish to attain spiritual enlightment through you or religious authorities?"
]

quiz = {
    1 : ["Reincarnation", "Go to a holy place", "Nothing"],
    2 : ["One (Monotheistic)", "More than one God (Polytheistic)", "More than one aspect of one God", "None"],
    3 : ["Regimented prayer schedule", "Recommended prayer", "Meditation", "Group prayer"],
    4 : ["Eating And Drinking Restrictions", "Fasting", "Who you can marry", "Pre-marital sex", "Virtually None", "Cutting hair", "Gender Identity/Sexuality"],
    5 : ["Yes", "No"],
    6 : ["Worships in a building of religious significance of a specific week day each week", "Often happens in a building of religious significance but sometimes happens in an informal setting, on a specific day of the week", "Worship is not on a specific day, or no common gathering place"],
    7 : ["Yes", "No"],
    8 : ["Yes", "No"],
    9 : ["Start showing up", "Specific ritual", "Through birth or a special council"],
    10 : ["No specific way", "The heavens and earth were created in six days, and on the seventh day, God rested.", "The God(s) created it and it is just an extension of the God(s)"],
    11 : ["Through the clergy", "Personal Relationship"]
}

ans_key = {
    1 : [[0,1,2,3], [4,5,6], []],
    2 : [[3,4,5,6], [0], [1], [2]],
    3 : [[5], [6,4], [0,2,1], [0]],
    4 : [[5,6], [5,4], [5,6], [4,5,6], [0], [3], [1,2,3,4,5,6]],
    5 : [[0,1,4,5,6], [2,3]],
    6 : [[4,5,6], [0,2], [1,3]],
    7 : [[1,3], [0,2,4,5,6]],
    8 : [[0,1,2,3], [4,5,6]],
    9 : [[0,1,2], [3,4,5], [6]],
    10 : [[2], [4,5,6], [0,1,3]],
    11 : [[4], [0,1,2,3,5,6]]
}

def translate_to_stupid(fin):
    #[[selected answers], {question num : [possible answers]}]
    final = []
    for i in fin:
        if "q" in i:
            select_ans = [int(item) for item in fin[i]]
            question_num = int(i[1:])
            pos_ans = list(range(1,len(ans_key[int(question_num)]) + 1))
            #print(select_ans, question_num, pos_ans)
            final.append([select_ans, {question_num : pos_ans}])
    return final


def get_rel(num):
    return religions[num]

def add_answer(question : dict) -> None:
    (ans_num, query) = question
    for i in query.keys():
        query_num = i
        break
    new_info = []
    #print(query, "query", ans_num, "ans_num")
    for i in query.values():
        for j in i:
            for k in query.keys():
                key = k
                break
            new_info.append(j in ans_num)
    final_information[query_num] = new_info



def make_pro_con_dict() -> None:
    for index, j in enumerate(final_information.values()):
        key = index + 1
        for ind, i in enumerate(ans_key[key]):
            if j[ind]:
                for rel in i:
                    religion = get_rel(rel)
                    religion_pro_cons[religion]["pro"].append([key,ind])
                    #print(get_rel(rel), "pro")

            else:
                for rel in i:
                    religion = get_rel(rel)
                    religion_pro_cons[religion]["con"].append([key, ind])
                    #print(get_rel(rel), "con")

def get_pro_con_ans(coord):
    (question,ans) = coord
    answer = quiz[question][ans]
    title = questions[question - 1]
    return_value = {title : answer}
    return return_value

def test_thing():
    for i in religion_pro_cons:
        print(i)
        print("Pros")
        for j in religion_pro_cons[i]["pro"]:
            print(get_pro_con_ans(j))
        print("Cons")
        for j in religion_pro_cons[i]["con"]:
            print(get_pro_con_ans(j))

def make_under(word: str) -> str:
    return len(word) * "-"

def get_result() -> str:
    result = ""
    for i in religion_pro_cons:
        result += f"{i}\n{make_under(i)}\nPros\n"
        #key_list = []
        for j in religion_pro_cons[i]["pro"]:
            pro_dict = get_pro_con_ans(j)
            #print(pro_dict)
            key = list(pro_dict.keys())[0]
            #print(key, pro_dict)
            val = pro_dict[key]
            result += f"""  {key}
    -{val}\n"""
        result += f"Cons\n"
        for j in religion_pro_cons[i]["con"]:
            con_dict = get_pro_con_ans(j)
            key = list(con_dict.keys())[0]
            val = con_dict[key]
            result += f"""  {key}
    -{val}\n"""
        result += "\n"
    return result[:-2]

def add_answers(answers: list) -> None:
    #print(answers)
    for i in answers:
    #    print(i, "i")
        add_answer(i)

def make_answers(fin : dict) -> list:
    return translate_to_stupid(fin)

def get_top() -> list:
    count = 0
    top = []
    for i in religion_pro_cons:
        cur_count = len(religion_pro_cons[i]["pro"])
        if cur_count > count:
            count = cur_count
            top = [i]
        elif cur_count == count:
            top.append(i)
    if len(top) > 1:
        lowest_con = 100
        best = []
        for i in top:
            cur_count = len(religion_pro_cons[i]["con"])
            if cur_count < lowest_con:
                lowest_con = cur_count
                best = [i]
            if cur_count == lowest_con:
                best.append(i)
        top = list(best)
    return top
    
        

def exec(form_input: dict) -> None:
    #add something to get answers in a list
    answers = make_answers(form_input)
    add_answers(answers)
    make_pro_con_dict()
    #print(f"final information: {final_information}")
    return [get_result(), get_top()]
    



#print(get_pro_con_ans([1,1]))

    
# test_question = [[1,2], {1 : [1,2,3]}]
# test_question2 = [[2], {2 : [1,2,3,4]}]
# test_question3 = [[1,2,3], {3 : [1,2,3,4,5,6]}]
# add_answer(test_question)
# add_answer(test_question2)
# add_answer(test_question3)
# print(final_information)
# make_pro_con_dict()
# # print(religion_pro_cons)
# # #test_thing()
# print(get_result())
# thing = translate_to_stupid(test_input)
# print(thing)
#print(exec(test_input))


#{1: [False, True, True], 2: [False, True, False, True], 3: [True, False, False, False], 4: [False, False, True, False, False, False, False], 5: [False, True], 6: [True, False, False], 7: [True, False], 8: [False, True], 9: [True, False, False], 10: [True, False, False], 11: [True, False]} 
#{1: [True, True, False], 2: [False, True, False, False], 3: [True, True, True, False, False, False]}