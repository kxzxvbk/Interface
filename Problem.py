import os
ROOT_DIR = './data'
JUDGE_DIR = os.path.join(ROOT_DIR, 'judgement')
MULTIPLE_CHOICE_DIR = os.path.join(ROOT_DIR, 'multiple_choice')


class Problem:
    def __init__(self, path):
        self._path = path
        with open(path, 'r') as f:
            contents = f.read()
            self._question, self._answer = self.__split_content(contents)

    def __split_content(self, contents):
        # TODO
        # 用某种方式从所有读入的字符串中，分离问题和答案
        # 此处找到最后一个非结尾回车换行，并由此分开
        length = len(contents)
        i = length - 1
        while i > 0:
            if contents[i] == '\n' and i != length - 1:
                break
            i = i - 1
        if i == 0:
            raise RuntimeError('The format of problem: {} seems bad.'.format(self._path))
        question = contents[:i]
        answer = contents[i:]
        return question, answer

    def get_question(self):
        return self._question

    def get_answer(self):
        return self._answer


if __name__ == '__main__':
    li = os.listdir(JUDGE_DIR)
    error_array = []
    for filename in li:
        temp_path = os.path.join(JUDGE_DIR, filename)
        try:
            problem = Problem(temp_path)
        except RuntimeError:
            error_array.append(temp_path)

    li = os.listdir(MULTIPLE_CHOICE_DIR)
    for filename in li:
        temp_path = os.path.join(MULTIPLE_CHOICE_DIR, filename)
        try:
            problem = Problem(temp_path)
        except RuntimeError:
            error_array.append(temp_path)

    if len(error_array) == 0:
        print('Every files are in right format(without RE)')

    else:
        print('Runtime occurs when processing these files: ')
        print(error_array)
