import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category, db
from sqlalchemy.sql.expression import func
QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, DELETE')
        return response
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

    @app.route('/questions', methods=['GET'])
    def get_questions():
        page = request.args.get('page', 1, type=int)
        category_array = []
        start = (page - 1) * 10
        end = start + 10
        questions = Question.query.all()
        category_list = Category.query.all()
        questions_count = Question.query.count()

        for x in category_list:
            category_array.append(x.type)
        return jsonify({
                "questions": format_questions(questions)[start:end],
                "total_questions":questions_count,
                "categories": category_array,
                "current_category": "1"
            
        })

    @app.route('/questions/<int:question_id>', methods=["DELETE"])
    def detele_question(question_id):
        Question.query.filter(Question.id == question_id).delete()
        db.session.commit()
        return jsonify({
            "message":"question deletedess"
        })

    @app.route('/categories', methods=['GET'])
    def get_category_list():
        category_list = Category.query.all()
        category_array = {}
        for x in category_list:
            category_array[x.id]=x.type
        return jsonify({
            "categories":category_array
        })
    @app.route('/questions', methods=['POST'])
    def add_new_question():
        client_data = request.get_json()
        question =client_data['question']
        answer =client_data['answer']
        difficulty =client_data['difficulty']
        category =client_data['category']
        question_data = Question(question=question,answer=answer, difficulty=difficulty, category=category )
        db.session.add(question_data)
        db.session.commit()
        return jsonify({
            "categories":"category_array"
        }) 
 
    @app.route('/questions/search', methods=['POST'])
    def search_question():
        data = request.get_json()
        search_term =data['searchTerm']
        category_array = []
        search_condition = '%{0}%'.format(search_term)
        search_question = Question.query.filter(Question.question.ilike(search_condition)).all()
        category_list = Category.query.all()
        questions_count = Question.query.filter(Question.question.ilike(search_condition)).count()

        for x in category_list:
            category_array.append(x.type)
        return jsonify({
                "questions": format_questions(search_question),
                "total_questions":questions_count,
                "categories": category_array,
                "current_category": "1"
            
        })

    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_question_by_category(category_id):
        category_array = []
        questions = Question.query.filter(Question.category == category_id).all()
        questions_count = Question.query.filter(Question.category == category_id).count()
        category_list = Category.query.all()
        for x in category_list:
            category_array.append(x.type)
        return jsonify({
                "questions": format_questions(questions),
                "total_questions":questions_count,
                "categories": category_array,
                "current_category": category_id
            
        })

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

    @app.route('/quizzes', methods=['POST'])
    def question_quiz():
        data = request.get_json()
        previous_questions =data['previous_questions']
        quiz_category =data['quiz_category']['id']
        if quiz_category == 0:
            question_data = Question.query.order_by(func.random()).all()
        else:
            question_data = Question.query.filter(Question.category == quiz_category).order_by(func.random()).all()
        question = Question.query.get(10)
        current_question = get_random_question(question_data, previous_questions)
        return current_question
 
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
      "success": False, 
      "error": 422,
      "message": "unable to process the request"
      }), 422
    @app.errorhandler(404)
    def not_found(error):
     return jsonify({
        "success": False, 
        "error": 404,
        "message": "The requested resource is not found in this server"
        }), 404
    @app.errorhandler(405)
    def not_found(error):
     return jsonify({
        "success": False, 
        "error": 405,
        "message": "The requested Method is not allowed"
        }), 405
    @app.errorhandler(400)
    def not_found(error):
     return jsonify({
        "success": False, 
        "error": 400,
        "message": "Bad input detected"
        }), 400
    return app

