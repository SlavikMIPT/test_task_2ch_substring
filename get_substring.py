#!/usr/bin/python3
def get_2ch_substring(in_str: str):
    """
    Finds the longest substring consisting of no more than two different characters.
    :param in_str: Input string terminated by '\0'.(For easy porting to C / C ++.)
    Terminator will be added automatically if input string doesn't have it.
    :type in_str: str
    :return: The longest substring consisting of no more than two different characters.
        If more than one substring has been found - closest to the beginning of the input string.
    :rtype: str
    """
    if not isinstance(in_str, str):
        raise TypeError('Input object is not str!')
    in_str = str(in_str)
    # For easy porting to C/C++
    in_str = in_str if in_str.endswith('\0') else in_str + '\0'
    if in_str[0] == '\0':
        return ''

    cur_start, cur_end = 0, 0  # offset of the beginning and end of the current substring.
    out_start, out_end = 0, 0  # offset of the beginning and end of the longest substring at the current moment.
    cur_chars_in_substr = [None, in_str[0]]  # chars used in the current substring, last encountered is the last one
    new_char_in_substr_offset = 0  # start of the one-character substring nearest to the cur_end
    """
    Move the cur_end pointer from the beginning to the end in the loop by 1 character per iteration:
        - cur_char = in_str[cur_end]
        - if cur_end points to a character that is not in cur_chars_in_substr or to '\0':
            - if ((cur_end - 1) - cur_start) is greater (out_end - out_start):
                - save the beginning and end of out_start, out_end = cur_start, cur_end
            - if cur_char == '\0':
                - return the substring with the start out_start and end out_end
            - cur_start = new_char_in_substr_offset - move the start of the current substring
                        to the start of the one-character substring nearest to the cur_end
            - new_char_in_substr_offset = cur_end - save the moment of character change
            - cur_chars_in_substr[0], cur_chars_in_substr[1] = cur_chars_in_substr[1], cur_char
        - else if cur_end points to a symbol equal to cur_chars_in_substr[0]('the oldest one'):
            - swap cur_chars_in_substr [0] and cur_chars_in_substr [1]
            - new_char_in_substr_offset = cur_end - save the moment of character change
        - cur_end += 1
    """
    while True:
        cur_char = in_str[cur_end]
        if cur_char not in cur_chars_in_substr or cur_char == '\0':
            if ((cur_end - 1) - cur_start) > (out_end - out_start):
                out_start, out_end = cur_start, (cur_end - 1)
            if cur_char == '\0':
                return in_str[out_start:out_end + 1]
            cur_start = new_char_in_substr_offset
            new_char_in_substr_offset = cur_end
            cur_chars_in_substr[0], cur_chars_in_substr[1] = cur_chars_in_substr[1], cur_char
        elif cur_char == cur_chars_in_substr[0]:
            cur_chars_in_substr[0], cur_chars_in_substr[1] = cur_chars_in_substr[1], cur_chars_in_substr[0]
            new_char_in_substr_offset = cur_end
        cur_end += 1
