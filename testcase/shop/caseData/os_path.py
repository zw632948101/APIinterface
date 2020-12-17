import os



# os.path.realpath(__file__) 获取当前操作的文件路径
import os
object_path = os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]
evaluate_001 = os.path.join(object_path + r'\shop\caseData\evaluate_001.gif')
evaluate_002 = os.path.join(object_path + r'\shop\caseData\evaluate_002.jpg')
case_data = os.path.join(object_path + r'\shop\caseData')
if __name__ == '__main__':

    print(object_path)
    print("图片路径: \n{0}\n{1}".format(evaluate_001,evaluate_002))