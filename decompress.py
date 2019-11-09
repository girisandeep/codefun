
def main():
    # assert multiply("sandeep", 1) == "sandeep", "multiply can't handle 1"
    # assert multiply("sandeep", 2) == "sandeepsandeep", "multiply can't handle 2"
    # assert multiply("sandeep", 0) == "", "multiply can't handle 0"
    check("3[abc]4[ab]c", "abcabcabcababababc", "Not working for simple case.")
    check("2[3[a]b]", "aaabaaab", "Not working for 2[3[a]b].")
    check("10[a]", "aaaaaaaaaa", "Not working for 10[a].")

class Decomp:
    def __init__(self, s):
        self.input_string = s
        self.pos = 0

    def consume_number_part(self):
        text_part = ''
        number_part = ''
        is_prev_num = False
        while self.pos < len(self.input_string):
            ch = self.input_string[self.pos]
            if ch == '[' or ch == ']':
                break;
            elif ch >= '0' and ch <= '9':
                if is_prev_num:
                    number_part += ch
                else:
                    number_part = ch
                is_prev_num = True
            else:
                if is_prev_num:
                    text_part += number_part
                    number_part = ''
                text_part += ch
                is_prev_num = False
            self.pos += 1
        
        if number_part == '':
            number_part = None
        else:
            number_part = int(number_part)
        # print('text_part, number_part, pos, output:', text_part, number_part, pos)
        return (text_part, number_part)

    def consume_brackets_body(self):
        output = ''
        while self.pos < len(self.input_string):
            (text_part, number_part) = self.consume_number_part()
            
            result = ''
            output += text_part
            if number_part and self.pos < len(self.input_string):
                self.pos += 1
                string = self.consume_brackets_body()
                result = string * number_part
                output += result
            elif self.pos < len(self.input_string) and self.input_string[self.pos] == ']':
                self.pos += 1
                break;
        # print('consume_brackets_body (output, pos): ', output, pos)
        return output;

    def decompress_stack(self):
        stack = []
        text_part = ''
        number_part = ''
        is_prev_num = False
        while self.pos < len(self.input_string):
            ch = self.input_string[self.pos]
            if ch == '[':
                stack.append((text_part, number_part))
                text_part = ''
                number_part = ''
            elif ch == ']':
                (ptext_part, pnumber_part) = stack.pop()
                text_part = ptext_part + (text_part+number_part)*int(pnumber_part)
                number_part = ''
            elif ch >= '0' and ch <= '9':
                if is_prev_num:
                    number_part += ch
                else:
                    number_part = ch
                is_prev_num = True
            else:
                if is_prev_num:
                    text_part += number_part
                    number_part = ''
                text_part += ch
                is_prev_num = False
            self.pos += 1
        return text_part + number_part

def check(s, exp, msg):
    d = Decomp(s)
    result = d.decompress_stack()
    if result == exp:
        print("Test is successful for ", s)
    else:
        print("Failed ", s, ": Expected ", exp, " but got ", result)
        # print(msg)

# def multiply(string, num):
#     result = ""
#     for i in range(num):
#         result += string
#     return result

if __name__ == '__main__':
    main()
