from flask import jsonify
def format_questions(question):
        question_obj = []
        for  x in question:
            question_obj.append({
                "id": x.id,
                "question": x.question,
                "answer": x.answer,
                "difficulty": x.difficulty,
                "category": x.category
            })
        return question_obj
def get_random_question(question_arr, viewd_questions):
          for  x in question_arr:
                if x.id not in viewd_questions:
                    id = x.id,
                    question = x.question,
                    answer = x.answer,
                    difficulty = x.difficulty,
                    category  = x.category
                    break
          
          return jsonify({"question":{"id": str(id[0]), "question":question[0], "answer":answer[0], "difficulty":difficulty[0], "category":category}})
