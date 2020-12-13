import random
import json
from nltk.tokenize import TweetTokenizer


def train_model():
    label_list = []
    response_list = []

    context_list = []

    label_response_dict = {}

    total_sarcasm_tokens = 0
    total_non_sarcasm_tokens = 0

    sarcasm_tokens = {}
    non_sarcasm_tokens = {}



    with open("data/train.jsonl", encoding="utf-8") as json_file:
        
        data = json.loads("[" + json_file.read().replace("}\n{", "},\n{") + "]")
        ############################################ ------------------------------

        # print(type(data))   # <class 'list'>
        temp = 0
        tokenizer = TweetTokenizer()


        for p in data:#["label"]:
            #print(p)
            #print(type(p))  # <class 'dict'>
            temp += 1
            label_list.append(p["label"])



            response = p["response"].replace("@USER", "")
            response_list.append(response)
            
            
            words = tokenizer.tokenize(response.lower())

            if(p["label"] == "SARCASM"):
                for word in words:
                    total_sarcasm_tokens += 1
                    if word in sarcasm_tokens:
                        sarcasm_tokens[word] += 1
                    else:
                        sarcasm_tokens[word] = 1
            else:
                for word in words:
                    total_non_sarcasm_tokens += 1
                    if word in non_sarcasm_tokens:
                        non_sarcasm_tokens[word] += 1
                    else:
                        non_sarcasm_tokens[word] = 1

            
            context_list.append(p["context"])

            # print(p.keys())
                    # dict_keys(['label', 'response', 'context'])


    # print(label_list[0])
    # print(response_list[0], "\n")
    # print(context_list[0])

    # print(total_sarcasm_tokens)
    # print(len(sarcasm_tokens))

    # print(total_non_sarcasm_tokens)
    # print(len(non_sarcasm_tokens))

    return sarcasm_tokens, non_sarcasm_tokens, total_sarcasm_tokens, total_non_sarcasm_tokens

    
##json_file = open("data/1.txt", "r", encoding="utf-8")
##
##for p in json_file:
##    print(p)
##    print(type(p))
##
##json_file.close()



##num_of_output = 1800
##
##YES = "SARCASM"
##NO = "NOT_SARCASM"
##
##
##output_file = open("answer.txt", "w")
##
##
##for i in range(1, num_of_output):
##
##    rand_num = random.random()
##   # print(round(rand_num))
##
##    if round(rand_num) ==1:
##        output = "twitter_" + str(i) + "," + str(YES) + "\n"
##    else:
##        output = "twitter_" + str(i) + "," + str(NO) + "\n"
##
##    output_file.write(output)
##
##output = "twitter_" + str(num_of_output) + "," + str(YES)
##
##output_file.write(output)
##
##output_file.close()
##    















