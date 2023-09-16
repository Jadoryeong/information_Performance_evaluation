from tkinter import *

def clicked():
    if radio.get() == 1:
        window_python = Toplevel()
        window_python.title('알고싶은 개념을 선택하세요')
        window_python.geometry("500x300")

        def python_clicked():
            if radio_python.get() == 1:
                window_coding = Toplevel()
                window_coding.title('코딩') 
                window_coding.geometry("500x300")
                lb_program = Label(window_coding, text = '프로그램 : 수행하여야 할 작업의 퍼리 절차와 방법을 지시하는 일연의 명령어 집합').grid(row = 0, column = 0)
                lb_programming = Label(window_coding, text = '프로그래밍 : 컴퓨터가 일을 할 수 있도록 컴퓨터가 이해하는 언어로 해야할 일을 기록하는 것').grid(row = 1, column = 0)
                lb_coding = Label(window_coding, text = '코딩 : 프로그래밍을 말하는 것으로 두 단어가 같은 의미').grid(row = 2, column = 0)

            elif radio_python.get() == 2:
                window_data_type = Toplevel()
                window_data_type.title('자료형')
                window_data_type.geometry("500x300")
                lb_data_type = Label(window_data_type, text = '자료를 쉽게 사용할 수 있도록 기능과 역할에 따라 자료를 구분했고 이것을 자료형이라고 합니다. \n 자료형으로는 정수형, 실수형, 문자형이 있습니다.').pack()
                lb_string = Label(window_data_type, text = '문자형(string) : 세상에 존재하는 어떤 것을 기호(한글, 영어 알파벳, 아라비아 숫자 등)로 표기한 것').pack()
                lb_number = Label(window_data_type, text = '정수형(integer) : 수를 나타내는 글자로 소수점이 없는 숫자').pack()
                lb_boolean = Label(window_data_type, text = '실수형(floating point) : 수를 나타내는 글자로 소수점이 있는 숫자').pack()
            
            elif radio_python.get() == 3:
                window_variable = Toplevel()
                window_variable.title('변수')
                window_variable.geometry("500x300")
                lb_variable = Label(window_variable, text = '변수 : 컴퓨터가 연산을 처리할 때 필요한 값이나 \n 처리한 결괏값을 저장하기 위하여 할당된 메모리 공간').pack()
                lb_variable1 = Label(window_variable, text = '변수의 선언 : 변수를 사용하기 전에 변수 이름과 어떤 유형의 값이 변수로 들어가는지 정의하는 것').pack()
            
            elif radio_python.get() == 4:
                window_operator = Toplevel()
                window_operator.title('연산자')
                window_operator.geometry("500x200")
                lb_operator = Label(window_operator, text = '연산자란 변수나 데이터를 연산할 때 사용되는 기호를 말한다.').place(x = 90, y = 20)
                
                def operator_clicked():
                    if radio_operator.get() == 0:
                        window_unary_operator = Toplevel()
                        window_unary_operator.title('단항연산자')
                        window_unary_operator.geometry("500x300")

                        image_unary_operator = PhotoImage(file = "unary_operator(1).png")
                        lb_unary_operator = Label(window_unary_operator, image = image_unary_operator)
                        lb_unary_operator.image = image_unary_operator
                        lb_unary_operator.place(x = 50, y = 70)
                        
                    elif radio_operator.get() == 1:
                        window_arithmetic_operator = Toplevel()
                        window_arithmetic_operator.title('산술연산자')
                        window_arithmetic_operator.geometry("500x300")

                        image_arithmetic_operator = PhotoImage(file = "arithmetic_operator.png")
                        lb_arithmetic_operator = Label(window_arithmetic_operator, image = image_arithmetic_operator)
                        lb_arithmetic_operator.image = image_arithmetic_operator
                        lb_arithmetic_operator.place(x = 50, y = 50)

                    elif radio_operator.get() == 2:
                        window_comparison_operator = Toplevel()
                        window_comparison_operator.title('비교연산자')
                        window_comparison_operator.geometry("500x300")

                        image_comparison_operator = PhotoImage(file = "comparison_operator.png")
                        lb_comparison_operator = Label(window_comparison_operator, image = image_comparison_operator)
                        lb_comparison_operator.image = image_comparison_operator
                        lb_comparison_operator.place(x = 50, y = 50)

                    elif radio_operator.get() == 3:
                        window_logical_operator = Toplevel()
                        window_logical_operator.title('논리연산자')
                        window_logical_operator.geometry("500x300")

                        image_logical_operator = PhotoImage(file = "logical_operator.png")
                        lb_logical_operator = Label(window_logical_operator, image = image_logical_operator)
                        lb_logical_operator.image = image_logical_operator
                        lb_logical_operator.place(x = 50, y = 50)
                    elif radio_operator.get() == 4:
                        window_assignment_operator = Toplevel()
                        window_assignment_operator.title('대입연산자')
                        window_assignment_operator.geometry("500x300")

                        image_assignment_operator = PhotoImage(file = "assignmet_operator.png")
                        lb_assignment_operator = Label(window_assignment_operator, image = image_assignment_operator)
                        lb_assignment_operator.image = image_assignment_operator
                        lb_assignment_operator.place(x = 50, y = 70)
                
                radio_operator = IntVar()

                button_unary_operator = Radiobutton(window_operator, text = '단항 연산자', variable = radio_operator, value = 0).place(x = 100, y = 70)
                button_arithmetic_operator = Radiobutton(window_operator, text = '산술 연산자', variable = radio_operator, value = 1).place(x= 200, y = 70)               
                button_comparison_operator = Radiobutton(window_operator, text = '비교 연산자', variable = radio_operator, value = 2).place(x = 300, y = 70)
                button_logical_operator = Radiobutton(window_operator, text = '논리 연산자', variable = radio_operator, value = 3).place(x = 150, y = 100)
                button_assignment_operator = Radiobutton(window_operator, text = '대입 연산자', variable = radio_operator, value = 4).place(x = 250, y = 100)

                operator_button_clicked = Button(window_operator, text = '선택', command = operator_clicked).place(x = 235, y = 150)

            elif radio_python.get() == 5:
                window_structure = Toplevel()
                window_structure.geometry("700x900")
                window_structure.title('구조')

                image_structure = PhotoImage(file = "structure.png")
                lb_structure = Label(window_structure, image = image_structure)
                lb_structure.image = image_structure
                lb_structure.place(x = 50, y = 0)

            elif radio_python.get() == 6:
                window_function = Toplevel()
                window_function.title('함수')
                window_function.geometry("850x500")

                image_function = PhotoImage(file = "function.png")
                lb_function = Label(window_function, image = image_function)
                lb_function.image = image_function
                lb_function.place(x = 50, y = 70)

                    
        radio_python = IntVar()

        button_coding = Radiobutton(window_python, text = "코딩", variable = radio_python, value = 1).pack()
        button_data_type = Radiobutton(window_python, text = "자료형", variable = radio_python, value = 2).pack()
        button_variable = Radiobutton(window_python, text = "변수", variable = radio_python, value = 3).pack()
        button_arithmetic_operator = Radiobutton(window_python, text = "연산자", variable = radio_python, value = 4).pack()
        button_structure = Radiobutton(window_python, text = "구조", variable = radio_python, value = 5).pack()
        button_function = Radiobutton(window_python, text = "함수", variable = radio_python, value = 6).pack()
        
        python_button_clicked = Button(window_python, text = '선택', command = python_clicked).pack()
        
    elif radio.get() == 2:
        window_physics1 = Toplevel()
        window_physics1.title('알고싶은 개념을 선택하세요')
        window_physics1.geometry("500x300")
        
        def physics1_clicked():
            if radio_physics1.get() == 1:
                window_movement_of_object = Toplevel()
                window_movement_of_object.title('물체의 운동')
                window_movement_of_object.geometry("700x500")
                
                image_movement_of_object = PhotoImage(file = "movement_of_object.png")
                lb_movement_of_object = Label(window_movement_of_object, image = image_movement_of_object)
                lb_movement_of_object.image = image_movement_of_object
                lb_movement_of_object.place(x = 50, y = 70)

            elif radio_physics1.get() == 2:
                window_Newton_laws_of_motion = Toplevel()
                window_Newton_laws_of_motion.title('뉴턴 운동 법칙')
                window_Newton_laws_of_motion.geometry("700x300")

                image_Newton_laws_of_motion = PhotoImage(file = "Newton_laws_of_motion.png")
                lb_Newton_laws_of_motion = Label(window_Newton_laws_of_motion, image = image_Newton_laws_of_motion)
                lb_Newton_laws_of_motion.image = image_Newton_laws_of_motion
                lb_Newton_laws_of_motion.place(x = 50, y = 70)

            elif radio_physics1.get() == 3:
                window_impulse_momentum_theorem = Toplevel()
                window_impulse_momentum_theorem.title('운동량과 충격량')
                window_impulse_momentum_theorem.geometry("700x500")

                image_impulse_momentum_theorem = PhotoImage(file = "impulse_momentum_theorem.png")
                lb_impulse_momentum_theorem = Label(window_impulse_momentum_theorem, image = image_impulse_momentum_theorem)
                lb_impulse_momentum_theorem.image = image_impulse_momentum_theorem
                lb_impulse_momentum_theorem.place(x = 50, y = 70)

            elif radio_physics1.get() == 4:
                window_Thermodynamics1 = Toplevel()
                window_Thermodynamics1.title('열역학 제 1 법칙')
                window_Thermodynamics1.geometry("700x300")

                image_Thermodynamics1 = PhotoImage(file = "Thermodynamics1.png")
                lb_Thermodynamics1 = Label(window_Thermodynamics1, image = image_Thermodynamics1)
                lb_Thermodynamics1.image = image_Thermodynamics1
                lb_Thermodynamics1.place(x = 50, y = 70)

            elif radio_physics1.get() == 5:
                window_Thermodynamics2 = Toplevel()
                window_Thermodynamics2.title('열역학 제 2 법칙')
                window_Thermodynamics2.geometry("900x500")

                image_Thermodynamics2 = PhotoImage(file = "Thermodynamics2.png")
                lb_Thermodynamics2 = Label(window_Thermodynamics2, image = image_Thermodynamics2)
                lb_Thermodynamics2.image = image_Thermodynamics2
                lb_Thermodynamics2.place(x = 50, y = 70)


        radio_physics1 = IntVar()   

        button_movement_of_object = Radiobutton(window_physics1, text = "물체의 운동", variable = radio_physics1, value = 1).pack()
        button_Newton_laws_of_motion = Radiobutton(window_physics1, text = "뉴턴 운동 법칙", variable = radio_physics1, value = 2).pack()
        button_impulse_momentum_theorem = Radiobutton(window_physics1, text = "운동량과 충격량", variable = radio_physics1, value = 3).pack()
        button_Thrmodynamics_1 = Radiobutton(window_physics1, text = "열역학 제 1 법칙", variable = radio_physics1, value = 4).pack()
        button_Thrmodynamics_2 = Radiobutton(window_physics1, text = "열역학 제 2 법칙", variable = radio_physics1, value = 5).pack()

        physics1_button_clicked = Button(window_physics1, text = '선택', command = physics1_clicked).pack()

    elif radio.get() == 3:
        window_math1 = Toplevel()
        window_math1.title('알고싶은 개념을 선택하세요')
        window_math1.geometry("500x300")

        def math1_clicked():
            if radio_math1.get() == 1:
                window_Exponent = Toplevel()
                window_Exponent.title('지수')
                window_Exponent.geometry("900x500")
                image_Exponent = PhotoImage(file = "Exponent.png")
                lb_Exponent = Label(window_Exponent, image = image_Exponent)
                lb_Exponent.image = image_Exponent
                lb_Exponent.place(x = 50, y = 70)

                window_Logarithm = Toplevel()
                window_Logarithm.title('로그')
                window_Logarithm.geometry("900x700")
                image_Logarithm = PhotoImage(file = "Logarithm.png")
                lb_Logarithm = Label(window_Logarithm, image = image_Logarithm)
                lb_Logarithm.image = image_Logarithm
                lb_Logarithm.place(x = 50, y = 70)

            elif radio_math1.get() == 2:
                window_Exponential_function = Toplevel()
                window_Exponential_function.title('지수함수')
                window_Exponential_function.geometry("900x350")
                image_Exponential_function = PhotoImage(file = "Exponential_function.png")
                lb_Exponential_function = Label(window_Exponential_function, image = image_Exponential_function)
                lb_Exponential_function.image = image_Exponential_function
                lb_Exponential_function.place(x = 50, y = 70)

                window_Logarithmic_function = Toplevel()
                window_Logarithmic_function.title('로그함수')
                window_Logarithmic_function.geometry("900x350")
                image_Logarithmic_function = PhotoImage(file = "Logarithmic_function.png")
                lb_Logarithmic_function = Label(window_Logarithmic_function, image = image_Logarithmic_function)
                lb_Logarithmic_function.image = image_Logarithmic_function
                lb_Logarithmic_function.place(x = 50, y = 70)

            elif radio_math1.get() == 3:
                window_trigonometric_function = Toplevel()
                window_trigonometric_function.title('삼각함수')
                window_trigonometric_function.geometry("850x900")
                image_trigonometric_function = PhotoImage(file = "trigonometric_function.png")
                lb_trigonometric_function = Label(window_trigonometric_function, image = image_trigonometric_function)
                lb_trigonometric_function.image = image_trigonometric_function
                lb_trigonometric_function.place(x = 50, y = 20)

            elif radio_math1.get() == 4:
                window_trigonometric_function_graph = Toplevel()
                window_trigonometric_function_graph.title('삼각함수 그래프')
                window_trigonometric_function_graph.geometry("700x900")
                image_trigonometric_function_graph = PhotoImage(file = "trigonometric_function_graph.png")
                lb_trigonometric_function_graph = Label(window_trigonometric_function_graph, image = image_trigonometric_function_graph)
                lb_trigonometric_function_graph.image = image_trigonometric_function_graph
                lb_trigonometric_function_graph.place(x = 50, y = 20)
                
                def trigonometric_function_graph_draw():
                    import math
                    from turtle import Turtle, Screen

                    RESOLUTION = 0.1

                    def plot(x_points, y_points):
                        for i, y in enumerate(y_points):
                            if abs(y) <= 2.0:
                                t.goto(x_points[i], y)
                                t.pendown()
                            else:
                                t.penup()
                        t.penup()

                    screen = Screen()
                    screen.setworldcoordinates(0, -1.5, 2 * math.pi / RESOLUTION, 1.5)

                    t = Turtle()

                    t.write("파란색 - cos 그래프 \n빨간색 sin그래프 \n초록색 tan그래프")

                    t.penup()

                    x = range(int(2 * math.pi / RESOLUTION))

                    t.color("blue")
                    plot(x, (math.cos(n * RESOLUTION) for n in x))

                    t.color("red")
                    plot(x, (math.sin(n * RESOLUTION) for n in x))

                    t.color("dark green")
                    plot(x, (math.tan(n * RESOLUTION) for n in x))

                    screen.exitonclick()
                
                button_trigonometric_function_graph_draw = Button(window_trigonometric_function_graph, text = '그래프 보기',command = trigonometric_function_graph_draw).place(x = 300, y = 750)

        radio_math1 = IntVar()

        button_Exponent_Logarithm = Radiobutton(window_math1, text = "지수 ∙ 로그", variable = radio_math1, value = 1).pack()
        button_Exponential_function_Logarithmic_function = Radiobutton(window_math1, text = "지수함수  ∙ 로그함수", variable = radio_math1, value = 2).pack()
        button_trigonmetric_function = Radiobutton(window_math1, text = "삼각함수", variable = radio_math1, value = 3).pack()
        button_trigonmetric_function_graph = Radiobutton(window_math1, text = "삼각함수 그래프", variable = radio_math1, value = 4).pack()

        math1_button_clicked = Button(window_math1, text = '선택', command = math1_clicked).pack()

root = Tk()
root.title("원하는 주제를 선택해 주세요")
root.geometry("500x300")

radio = IntVar()

button_python = Radiobutton(root, text = "파이썬", value = 1, variable = radio).pack()
button_physics1 = Radiobutton(root, text = "물리I", value = 2, variable = radio).pack()
button_math1 = Radiobutton(root, text = "수학I", value = 3, variable = radio).pack()

button = Button(text = '선택', command = clicked)
button.pack()
